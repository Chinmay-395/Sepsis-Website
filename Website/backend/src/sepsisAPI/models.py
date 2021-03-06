from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.core import serializers

import uuid

from profiles_api.models import UserProfile
# Create your models here.


class Doctor(models.Model):
    doc = models.ForeignKey(
        UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    phd = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.doc.name}'


class Patient(models.Model):
    NO_SEPSIS = 'NO_SEPSIS'
    SEPSIS_PREDICTED = 'SEPSIS_PREDICTED'
    SEVERE_SEPSIS = 'SEVERE_SEPSIS'
    SEPTIC_SHOCK = 'SEPTIC_SHOCK'
    CURED = 'CURED'
    SEPSIS_STATUS = (
        (NO_SEPSIS, NO_SEPSIS),
        (SEPSIS_PREDICTED, SEPSIS_PREDICTED),
        (SEVERE_SEPSIS, SEVERE_SEPSIS),
        (SEPTIC_SHOCK, SEPTIC_SHOCK),
        (CURED, CURED),
    )

    pat = models.ForeignKey(
        UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(blank=True, null=True)
    GENDER_TYPE_CHOICES = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
    )
    gender = models.CharField(max_length=255,
                              choices=GENDER_TYPE_CHOICES, null=True)
    address = models.TextField(null=True, blank=True)
    doctor = models.ForeignKey(
        Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    # This will
    grp_id = models.UUIDField(default=uuid.uuid4, editable=False)
    status = models.CharField(
        max_length=20, choices=SEPSIS_STATUS, default=NO_SEPSIS)

    def __str__(self):
        return f'{self.pat.name}'


class SepsisOfPatient(models.Model):
    patient = models.ForeignKey(Patient,
                                on_delete=models.SET_NULL, null=True, blank=True)

    heart_rate = models.FloatField(null=True, blank=True, default=0)
    oxy_saturation = models.FloatField(null=True, blank=True, default=0)
    temperature = models.FloatField(null=True, blank=True, default=0)
    blood_pressure = models.FloatField(null=True, blank=True, default=0)
    resp_rate = models.FloatField(null=True, blank=True, default=0)
    mean_art_pre = models.FloatField(null=True, blank=True, default=0)

    def __str__(self):
        return f'{self.patient} sepsis-ID:{self.id} --> {self.heart_rate}  {self.oxy_saturation}  {self.mean_art_pre}'


def user_is_patient_or_doctor(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == "DOCTOR":
            print("I RAN")
            print("The instance at doctor", instance)
            Doctor.objects.create(doc=instance)
            print("doc created")
        elif instance.user_type == "PATIENT":
            print("The instance at patient", instance)
            Patient.objects.create(pat=instance)
            # SepsisOfPatient.objects.create(patient=instance)
            print("pat created")
        else:
            print("NOTHING")
    elif created == False:
        print("the user Updated")
        print("sender >>>>>", sender)
        print("CHECKING DOC OR PATIENT", sender)
        print("instance user_type >>>>>", instance)
        print("instance email >>>>>>", instance.email)


""" This signal will dispatch the to check for user's role 
    Gets triggerd when UserProfile is created or updated
"""
post_save.connect(user_is_patient_or_doctor, sender=UserProfile)


def create_patient_schemas(sender, instance, created, **kwargs):
    if created:
        """[#This is assumed] 
            Check to see if doctor is avaiable 
            Every doctor can attend 3 patient simultaneously 
        """
        docs = Doctor.objects.all()
        flag = 1  # this will indicate initially all the docs are unavaible
        for doc in docs:
            if doc.patient_set.all().count() < 3:
                print(f"{doc} is avaiable")
                print("The patient is", instance)
                print("patient-ID ", instance.id)
                instance.doctor = doc
                SepsisOfPatient.objects.create(patient=instance)
                instance.save()
                print("The doctor assigned to you is", doc)
                flag = 0
                break
            else:
                flag = 1  # this will indicate all the docs are unavaible

        """ What if all the doctors aren't available """
        if flag == 1:
            latest_doctor = Doctor.objects.last()
            """ 
            • What if there are no doctors at all? 
            ans: Then the field would be None/empty. 
                 The admin has to actually physically assign the doctor
            """
            if latest_doctor == None:
                pass
            else:
                instance.doctor = latest_doctor
                print("The doctor assigned to you is", instance.doctor)
                print(f"{latest_doctor.id} available")
            SepsisOfPatient.objects.create(patient=instance)
            instance.save()

    if created == False:
        print("--------------------------------- you are updating", instance.id)


""" This signal will dispatch all the data regarding "Patient Model" 
    Thereby adding assigning doctor to a patient and formulating all the
    tables for sepsis tracking.
"""
post_save.connect(create_patient_schemas, sender=Patient)


def broadcast_patient_sepsis_to_the_group(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        pat = instance.patient
        pat_grp_id = str(pat.grp_id)
        serialized_obj = serializers.serialize('json', [instance, ])
        jsonified_sepsis_data = eval(serialized_obj)[0]['fields']
        instance.save()
        print(f"THE SEPSIS DATA SAVED IS \n {jsonified_sepsis_data}")
        async_to_sync(channel_layer.group_send)(
            pat_grp_id,
            {
                "type": 'echo.message',
                "data": jsonified_sepsis_data
            }
        )


# post_save.connect(broadcast_patient_sepsis_to_the_group,
#                   sender=SepsisOfPatient)

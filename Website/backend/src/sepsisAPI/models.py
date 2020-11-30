from django.db import models
from django.db.models.signals import pre_save, post_save
from profiles_api.models import UserProfile
# Create your models here.


class Doctor(models.Model):
    doc = models.ForeignKey(
        UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    phd = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(null=True, blank=True)

    def doc_id(self):
        return f'{self.id}'

    def __str__(self):
        return f'{self.doc.name}'


class Patient(models.Model):
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
            instance.doctor = latest_doctor
            SepsisOfPatient.objects.create(patient=instance)
            instance.save()
            print("The doctor assigned to you is", instance.doctor)
            print(f"{latest_doctor.id} available")

    if created == False:
        print("--------------------------------- you are updating", instance.id)


""" This signal will dispatch all the data regarding "Patient Model" 
    Thereby adding assigning doctor to a patient and formulating all the
    tables for sepsis tracking.
"""
post_save.connect(create_patient_schemas, sender=Patient)

# def create_patient_sepsis_schemas(sender,instance,created,**kwargs):
#     if created:

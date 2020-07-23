from django.db import models
from django.db.models.signals import pre_save, post_save
from profiles_api.models import UserProfile
# Create your models here.


class Doctor(models.Model):
    doc = models.OneToOneField(
        UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    phd = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.doc} Doctor'


class Patient(models.Model):
    pat = models.OneToOneField(
        UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(blank=True, null=True)
    GENDER_TYPE_CHOICES = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
    )
    gender = models.CharField(max_length=255,
                              choices=GENDER_TYPE_CHOICES, null=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.pat} Patient'


class SepsisOfPatient(models.Model):
    patient = models.ForeignKey(Patient,
                                on_delete=models.SET_NULL, null=True, blank=True)
    doctor = models.ForeignKey(
        Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    heart_rate = models.FloatField(null=True, blank=True, default=0)
    oxy_saturation = models.FloatField(null=True, blank=True, default=0)
    temperature = models.FloatField(null=True, blank=True, default=0)
    blood_pressure = models.FloatField(null=True, blank=True, default=0)
    resp_rate = models.FloatField(null=True, blank=True, default=0)
    mean_art_pre = models.FloatField(null=True, blank=True, default=0)

    def __str__(self):
        return f'the id {self.id} {self.heart_rate}  {self.oxy_saturation}  {self.mean_art_pre}'


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
            print("pat created")
        else:
            print("NOTHING")
    elif created == False:
        print("the user Updated")
        print("sender >>>>>", sender)
        print("CHECKING DOC OR PATIENT", sender)
        print("instance user_type >>>>>", instance)
        print("instance email >>>>>>", instance.email)


post_save.connect(user_is_patient_or_doctor, sender=UserProfile)


def create_patient_schemas(sender, instance, created, **kwargs):
    if created:
        docs = Doctor.objects.all()
        print("All the doctors", docs)
        # current_pat = sender.id
        print("SENDER ", instance.id)
    if created == False:
        print("---------------------------------")
        print("THE INSTANCE",)


post_save.connect(create_patient_schemas, sender=Patient)

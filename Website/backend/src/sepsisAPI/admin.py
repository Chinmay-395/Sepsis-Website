from django.contrib import admin
from .models import (Doctor,
                     Patient,
                     SepsisOfPatient,
                     )
# Register your models here.


class DoctorAdmin(admin.ModelAdmin):
    fields = ['doc', 'phd', 'address']
    list_display = ['doc', 'phd', 'address']


class PatientAdmin(admin.ModelAdmin):
    fields = ['pat', 'age', 'gender', 'doctor']
    list_display = ['pat', 'age', 'gender', 'doctor']
    list_filter = (
        'doctor',
    )


class SepsisOfPatientAdmin(admin.ModelAdmin):
    fields = ['patient',
              'heart_rate',
              'oxy_saturation',
              'temperature', 'blood_pressure',
              'resp_rate', 'mean_art_pre', ]

    list_display = ['patient', 'heart_rate', 'oxy_saturation',
                    'temperature', 'blood_pressure', 'resp_rate',
                    'mean_art_pre', ]

    list_filter = ['patient', ]


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(SepsisOfPatient, SepsisOfPatientAdmin)

from rest_framework.serializers import (
    ModelSerializer, HyperlinkedIdentityField, RelatedField, SlugRelatedField,
    StringRelatedField, PrimaryKeyRelatedField, CharField, SerializerMethodField)
from .models import Doctor, Patient, SepsisOfPatient
from profiles_api.models import UserProfile


class PatientSerializer(ModelSerializer):
    pat = SerializerMethodField()
    doctor = SerializerMethodField()
    # SerializerMethodField()
    sep_data = SerializerMethodField()  # CharField(read_only=True, source="patient")

    class Meta:
        model = Patient
        fields = ['id', 'pat', 'doctor', 'sep_data']
        # depth = 2

    def get_pat(self, obj):
        print("patient->>>>>>>>>>>>", str(obj.pat))
        return str(obj.pat)

    def get_doctor(self, obj):
        print("doctor->>>>>>>>>>>>", str(obj.doctor))
        return str(obj.doctor)

    def get_sep_data(self, obj):
        print("sepsis->>>>>>>>>>>>", str(obj.sepsisofpatient_set.all()))
        list_sepsis_data = obj.sepsisofpatient_set.values('id', 'heart_rate', 'oxy_saturation', 'temperature',
                                                          'blood_pressure', 'resp_rate', 'mean_art_pre')
        print("LIST THE SEPSIS DATA", list_sepsis_data)
        return list_sepsis_data  # str(obj.sepsisofpatient_set.all())


class DoctorSerializer(ModelSerializer):
    doc_name = CharField(read_only=True, source="doc.name")
    patient_set_name = SerializerMethodField()

    class Meta:
        model = Doctor

        fields = ['id', 'doc_name',
                  'patient_set', 'patient_set_name']

    def get_patient_set_name(self, obj):
        ''' <obj> refers to the object of Doctor-Model '''
        print("patient->>>>>>>>>>>>", str(obj.patient_set.all())
              )  # give the list of patient pertaining to the doctor
        pat_list = []
        for patient in obj.patient_set.all():
            """ <patient> is an object of the doctor whose
                object has been send into the function
            """

            x = patient
            y = patient.pat.name
            print(patient)
            print("====================", type(x))
            print("====================", type(y))
            print("NAME IS>>>>>>>>>>>>>", y)
            pat_list.append(y)  # pat_list += [y]

        print(pat_list)
        return pat_list  # str(obj)


class SepsisPatientSerializer(ModelSerializer):
    class Meta:
        model = SepsisOfPatient
        fields = ["id", "heart_rate", "oxy_saturation", "temperature",
                  "blood_pressure", "resp_rate", "mean_art_pre", "patient"]  # "__all__"

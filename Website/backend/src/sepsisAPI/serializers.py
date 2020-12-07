from rest_framework.serializers import (
    ModelSerializer, HyperlinkedIdentityField, RelatedField, SlugRelatedField,
    StringRelatedField, PrimaryKeyRelatedField, CharField, SerializerMethodField)
from .models import Doctor, Patient, SepsisOfPatient
from profiles_api.models import UserProfile
import json
import ast


class PatientSerializer(ModelSerializer):
    pat = SerializerMethodField()
    doctor = SerializerMethodField()
    sep_data = SerializerMethodField()  # CharField(read_only=True, source="patient")

    class Meta:
        model = Patient
        fields = ['id', 'pat', 'doctor', 'sep_data']
        # depth = 2

    def get_pat(self, obj):
        """ gives that patient whose object is running 
            for example:-
            patient_id = 1 <------> patient_name = Naruto Uzumaki
            patient_id = 2 <------> patient_name = Sasuke Uchiha
        """
        # print("patient->>>>>>>>>>>>", str(obj.pat))
        return str(obj.pat)

    def get_doctor(self, obj):
        print("doctor->>>>>>>>>>>>", str(obj.doctor))
        return str(obj.doctor)

    def get_sep_data(self, obj):
        # print("sepsis->>>>>>>>>>>>", str(obj.sepsisofpatient_set.all()))
        list_sepsis_data = obj.sepsisofpatient_set.values('heart_rate', 'oxy_saturation', 'temperature',
                                                          'blood_pressure', 'resp_rate', 'mean_art_pre')
        # print("LIST THE SEPSIS DATA", list_sepsis_data)
        return list_sepsis_data  # str(obj.sepsisofpatient_set.all())


class DoctorSerializer(ModelSerializer):
    doc_name = CharField(read_only=True, source="doc.name")
    # patient_set_name = SerializerMethodField()
    doctor = SerializerMethodField()
    each_pat_json = SerializerMethodField()

    class Meta:
        model = Doctor

        fields = ['id', 'doc_name',  # 'patient_set', 'patient_set_name',
                  'doctor', 'each_pat_json']

    def get_doctor(self, obj):
        print("doctor's id ->>>>>>>>>>>>", str(obj.id))
        print("doctor ->>>>>>>>>>>>", str(obj))
        return obj.id

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
            ''' getting the value sepsis data
                for each patient
                sepValue = x.sepsisofpatient_set.all()
                print(sepValue)
            '''

            patient_iside_obj_name = patient.pat.name
            # print(patient)
            # print("====================", type(x))
            # print("====================", type(patient_iside_obj_name))
            # print("NAME IS>>>>>>>>>>>>>", patient_iside_obj_name)
            # pat_list += [patient_iside_obj_name]
            pat_list.append(patient_iside_obj_name)

        print("CHECKOUT PAT_LIST", pat_list)
        return pat_list  # str(obj)

    def get_each_pat_json(self, obj):
        data_list = []
        new_list = []
        for patient in obj.patient_set.all():
            pat_id = patient.id
            pat_name = patient.pat.name
            data = json.dumps({'patient_id': pat_id, 'patient_name': pat_name})
            print("TJE DATA", data)
            # data_list.append(data)
            x = ast.literal_eval(data)
            data_list.append(x)
            print(x)
            # new_list += x
            # data_list = json.loads(data)
        print("THE DATA I want ++++++++++>", data_list)
        # print("THE DATA I want ++++++++++>", new_list)
        return data_list


class SepsisPatientSerializer(ModelSerializer):

    class Meta:
        model = SepsisOfPatient
        fields = ["heart_rate", "oxy_saturation", "temperature",
                  "blood_pressure", "resp_rate", "mean_art_pre",
                  "patient",
                  ]  # "__all__"

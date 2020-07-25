from rest_framework.serializers import (
    ModelSerializer, HyperlinkedIdentityField, RelatedField,
    StringRelatedField, PrimaryKeyRelatedField, CharField)
from .models import Doctor, Patient, SepsisOfPatient
from profiles_api.models import UserProfile


class DoctorUserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('email', 'name')
        depth = 1


class DoctorListSerializer(ModelSerializer):
    # each_patient = HyperlinkedIdentityField(many=True,read_only=True,view_name=)
    patient_set = RelatedField(source='patient.pat', many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'phd', 'patient_set']  # "__all__"
        depth = 2


class PatientListSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = ['pat', 'doctor', 'id']


class PatientsOfDoctor(ModelSerializer):
    # pat = CharField(read_only=True,source"")
    class Meta:
        model = Doctor
        fields = ['id', 'doc', 'phd']

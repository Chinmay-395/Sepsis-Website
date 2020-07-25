from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from profiles_api.models import UserProfile

from .models import Doctor, Patient, SepsisOfPatient
from .serializers import (DoctorUserProfileSerializer, PatientsOfDoctor,
                          DoctorListSerializer, PatientListSerializer)
# Create your views here.


class UserProfileDoctorList(ListAPIView):
    queryset = UserProfile.objects.filter(
        user_type="DOCTOR").values('email', 'name')
    # queryset = Doctor.objects.all().values('')
    serializer_class = DoctorUserProfileSerializer


class PatientList(ListAPIView):
    queryset = Patient.objects.all().order_by('-id')  # .values('doctor')
    serializer_class = PatientListSerializer


class DoctorList(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorListSerializer


class ListPatientsOfDoctors(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = PatientsOfDoctor


class DoctorPatientDetailView(ListAPIView):
    pass

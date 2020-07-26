from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from profiles_api.models import UserProfile

from .models import Doctor, Patient, SepsisOfPatient
from .serializers import (
    DoctorSerializer, PatientSerializer, SepsisPatientSerializer)
# Create your views here.


class DoctorModelViewSets(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    http_method_names = ['get']


class PatientModelViewSets(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    http_method_names = ['get']


class SepsisPatientModelViewSets(ModelViewSet):
    queryset = SepsisOfPatient.objects.all()
    serializer_class = SepsisPatientSerializer

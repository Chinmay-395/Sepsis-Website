from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from profiles_api.models import UserProfile

from .models import Doctor, Patient, SepsisOfPatient
from .serializers import (
    DoctorSerializer, PatientSerializer, SepsisPatientSerializer)
from .permissions import (DoctorProfileView, PatientProfileView)
# Create your views here.


class DoctorModelViewSets(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (DoctorProfileView,)
    http_method_names = ['get']


class PatientModelViewSets(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (PatientProfileView,)
    http_method_names = ['get']


class SepsisPatientModelViewSets(ModelViewSet):
    queryset = SepsisOfPatient.objects.all()
    serializer_class = SepsisPatientSerializer
    authentication_classes = (TokenAuthentication,)

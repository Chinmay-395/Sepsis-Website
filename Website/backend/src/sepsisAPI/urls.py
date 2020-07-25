from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from .views import (DoctorModelViewSets, PatientModelViewSets)
from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('profile', UserProfileViewSet)

router_sepsis = DefaultRouter()
router_sepsis.register('docsdoc', DoctorModelViewSets, basename='docs')
router_sepsis.register('patspat', PatientModelViewSets, basename='pats')

urlpatterns = [
    # path('doctors/', UserProfileDoctorList.as_view(), name='doc-list'),
    # path('patients/', UserProfilePatientList.as_view(), name='pat-list'),
    # path('docList/', DoctorList.as_view(),),
    # path('patList/', PatientList.as_view(),),
    # path('pats_doc/', ListPatientsOfDoctors.as_view(), name='pat_doc')
    path('', include(router_sepsis.urls))
]

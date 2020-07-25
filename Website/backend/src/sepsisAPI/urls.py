from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from .views import (DoctorList, ListPatientsOfDoctors,
                    UserProfileDoctorList, PatientList)
from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('profile', UserProfileViewSet)

router_sepsis = DefaultRouter()
router_sepsis.register('docsdoc', ListPatientsOfDoctors, basename='docs')

urlpatterns = [
    path('doctors/', UserProfileDoctorList.as_view(), name='doc-list'),
    path('docList/', DoctorList.as_view(),),
    path('patList/', PatientList.as_view(),),
    # path('pats_doc/', ListPatientsOfDoctors.as_view(), name='pat_doc')
    path('', include(router_sepsis.urls))
]

from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from .views import (DoctorModelViewSets, PatientModelViewSets,
                    SepsisPatientModelViewSets)
from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('profile', UserProfileViewSet)

router_sepsis = DefaultRouter()
router_sepsis.register('docsdoc', DoctorModelViewSets, basename='docs')
router_sepsis.register('patspat', PatientModelViewSets, basename='pats')
router_sepsis.register(
    'sepsisData', SepsisPatientModelViewSets, basename='sep_pats')
urlpatterns = [
    path('', include(router_sepsis.urls))
]

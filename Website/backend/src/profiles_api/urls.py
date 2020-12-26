from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api.views import (
    UserProfileViewSet, UserLoginApiView, UserProfilePartialUpdateView)


router = DefaultRouter()
router.register('profile', UserProfileViewSet,)
# router.register('profile_detail', UserProfileDetailViewSet,)
# basename="profile_uri"

app_name = 'profiles_api'

urlpatterns = [
    path('login/', UserLoginApiView.as_view(), name="log_in"),
    path('update-partial/<int:pk>/',
         UserProfilePartialUpdateView.as_view(), name="user-partial-update"),
    path('', include(router.urls,),)
]

# name="auth"

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api.views import (UserProfileViewSet, UserLoginApiView,)


router = DefaultRouter()
router.register('profile', UserProfileViewSet,)
# basename="profile_uri"

app_name = 'profiles_api'

urlpatterns = [
    path('login/', UserLoginApiView.as_view()),
    path('', include(router.urls,),)
]

# name="auth"

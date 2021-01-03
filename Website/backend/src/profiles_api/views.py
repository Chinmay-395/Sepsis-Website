from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework import (status, viewsets)
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authtoken.models import Token
# from Created app
from profiles_api import serializers, models, permissions

# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

    # def partial_update(self, request, pk=None):
    #     user = self.request.UserProfile.objects.get(id=pk)
    #     print(f"user {user}")

    # def update(self, request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return super().update(request, *args, **kwargs)
    # renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfilePartialUpdateView(GenericAPIView, UpdateModelMixin):
    serializer_class = serializers.UserDetailSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    # def partial_update(self, request, pk=None):
    #     serializer = serializers.UserDetailSerializer(
    #         request.user, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response(serializer.data)


class UserLoginApiView(ObtainAuthToken):
    """ handle creating user authentication tokens """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        print("THE USER from userLoginApiView>>>>>>>>>", user)
        print("THE USER-ID from userLoginApiView>>>>>>>>>", user.id)
        """ if the user is a doctor then I will send doc-id
            and if the user is a patient then i will send pat-id
            as user_type_id 
        """
        if user.user_type == 'DOCTOR':
            x = models.UserProfile.objects.get(id=user.id)
            userprofile_id = x.id
            y = x.doctor_set.values('id')
            user_type_id = y[0]['id']
            print("THE USER-ID of DOC", userprofile_id)
            print("USER's doc-id", user_type_id)

        elif user.user_type == 'PATIENT':
            x = models.UserProfile.objects.get(id=user.id)
            userprofile_id = x.id
            y = x.patient_set.values('id')
            user_type_id = y[0]['id']
            print("THE USER-ID of PATIENT", userprofile_id)
            print("USER's pat-id", user_type_id)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'name': user.name,
            'user_type': user.user_type,
            # the following code is commented, since it is referenced before assigned
            'user_type_id': user_type_id
        })

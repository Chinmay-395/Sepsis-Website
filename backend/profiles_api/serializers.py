from rest_framework import serializers
from profiles_api import models
from rest_framework.serializers import (
    ModelSerializer, HyperlinkedIdentityField, RelatedField, SlugRelatedField,
    StringRelatedField, PrimaryKeyRelatedField, CharField, SerializerMethodField)
# from sepsisAPI.models import Doctor, Patient, SepsisOfPatient


class UserProfileSerializer(serializers.ModelSerializer):
    # idOfTheUser = SerializerMethodField()

    class Meta:
        model = models.UserProfile
        fields = ('id', 'name', 'email', 'password', 'user_type', 'photo')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            },
            # 'user_type': {
            #     'default': "PATIENT"
            # }
        }

    # def get_idOfTheUser(self, obj):
    #     print("BOX-----------", obj)

    def create(self, validate_data):
        print("Validated data-----", validate_data)
        # if validate_data['photo'] == None:
        #     user = models.UserProfile.objects.create_user(
        #         email=validate_data['email'],
        #         name=validate_data['name'],
        #         password=validate_data['password'],
        #         user_type=validate_data['user_type'],
        #     )
        user = models.UserProfile.objects.create_user(
            email=validate_data['email'],
            name=validate_data['name'],
            password=validate_data['password'],
            user_type=validate_data['user_type'],
            photo=validate_data['photo']
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        print(f"\n The validated data {validated_data} \n")
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = [
            "id",
            'name',
            'email',
            'user_type',
            'photo'
        ]
        # extra_kwargs = {
        #     'name': {'read_only': True},
        #     'email': {'read_only': True},
        #     'user_type': {'read_only': True}
        # }

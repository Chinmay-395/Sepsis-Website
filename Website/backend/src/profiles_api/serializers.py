from rest_framework import serializers
from profiles_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id', 'name', 'email', 'password', 'user_type')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            },
            # 'user_type': {
            #     'default': "PATIENT"
            # }
        }

    def create(self, validate_data):
        print("Validated data-----", validate_data)
        user = models.UserProfile.objects.create_user(
            email=validate_data['email'],
            name=validate_data['name'],
            password=validate_data['password'],
            user_type=validate_data['user_type']
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = [
            'name',
            'email'
        ]
        extra_kwargs = {'name': {'read_only': True},
                        'email': {'read_only': True}}

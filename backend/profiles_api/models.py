from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager)
from django.conf import settings


class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None, user_type=None, photo=None):
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,
                          user_type=user_type, photo=photo)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database Model for users in the system """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USER_TYPE_CHOICES = (
        ('DOCTOR', 'DOCTOR'),
        ('PATIENT', 'PATIENT'),
    )
    user_type = models.CharField(max_length=255,
                                 choices=USER_TYPE_CHOICES, null=True)
    photo = models.ImageField(upload_to='photos', null=True, blank=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full nam of the user"""
        return self.name

    def req_get_user_type(self):
        return self.user_type

    def __str__(self):
        return f'{self.name}'  # {self.email} as {self.user_type}

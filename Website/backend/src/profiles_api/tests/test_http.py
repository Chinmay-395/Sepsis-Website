from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

AUTH_URL = reverse('profiles_api:userprofile-list')
# userprofile


class AuthenticationTest(APITestCase):
    def test_user_can_sign_up(self):
        payload = {
            "name": "test_userDoc_786",
            "email": "testDoc_user786@gmail.com",
            "password": "test",
            "user_type": "DOCTOR"
        }
        res = self.client.post(AUTH_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

AUTH_URL = reverse('profiles_api:userprofile-list')
# userprofile


"""[Tests in the the doctor's perspective]
"""

PASSWORD = "test"


def create_user_as_doctor(email='user@example.com', name="example_user",
                          password=PASSWORD, user_type="DOCTOR"):
    return get_user_model().objects.create_user(
        email=email,
        name=name,
        password=password,
        user_type=user_type
    )


def create_user_as_patient(email='user_patient@example.com', name="example_patient_user",
                           password=PASSWORD, user_type="PATIENT"):
    return get_user_model().objects.create_user(
        email=email,
        name=name,
        password=password,
        user_type=user_type
    )


class AuthenticationTest(APITestCase):
    def test_user_can_sign_up_as_doctor(self):
        payload = {
            "name": "test_userDoc_786",
            "email": "testDoc_user786@gmail.com",
            "password": PASSWORD,
            "user_type": "DOCTOR"
        }
        response = self.client.post(AUTH_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.last()
        self.assertEqual(response.data['id'], user.id)
        self.assertEqual(response.data['email'], user.email)
        self.assertEqual(response.data['user_type'], user.user_type)

    def test_user_can_login_in_as_doctor(self):
        user = create_user_as_doctor()
        response = self.client.post(reverse('profiles_api:log_in'), data={
            'username': user.email,
            'password': PASSWORD,
        })

        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_user_can_sign_up_as_patient(self):
        payload = {
            "name": "test_userPat_786",
            "email": "testPat_user786@gmail.com",
            "password": PASSWORD,
            "user_type": "PATIENT"
        }
        response = self.client.post(AUTH_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.last()
        self.assertEqual(response.data['id'], user.id)
        self.assertEqual(response.data['email'], user.email)
        self.assertEqual(response.data['user_type'], user.user_type)

    def test_user_can_login_in_as_patient(self):
        user = create_user_as_patient()
        response = self.client.post(reverse('profiles_api:log_in'), data={
            'username': user.email,
            'password': PASSWORD,
        })

        self.assertEqual(status.HTTP_200_OK, response.status_code)

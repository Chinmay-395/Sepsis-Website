from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from io import BytesIO

from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
AUTH_URL = reverse('profiles_api:userprofile-list')
# userprofile


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


def create_photo_file():
    data = BytesIO()
    Image.new('RGB', (100, 100)).save(data, 'PNG')
    data.seek(0)
    return SimpleUploadedFile('photo.png', data.getvalue())


class AuthenticationTest(APITestCase):
    """The following Tests are in the the doctor's perspective"""

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

    """The following Tests are in the the patient's perspective"""

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

    def test_user_can_sign_up_as_patient_with_image(self):
        photo_file = create_photo_file()
        payload = {
            "name": "test_userPat_786",
            "email": "testPat_user786@gmail.com",
            "password": PASSWORD,
            "user_type": "PATIENT",
            'photo': photo_file,
        }
        response = self.client.post(AUTH_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.last()
        self.assertEqual(response.data['id'], user.id)
        self.assertEqual(response.data['email'], user.email)
        self.assertEqual(response.data['user_type'], user.user_type)

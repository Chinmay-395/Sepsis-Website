from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

AUTH_URL = reverse('profiles_api:userprofile-list')
# userprofile

"""[Tests in the the doctor's perspective]
"""

PASSWORD = "test"


def create_user_as_doctor(email='user@example.com', name="example_user", password=PASSWORD, user_type="Doctor"):
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

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


# Create your tests here.


class RegistrationTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(
            reverse("users:register"),
            data={
                "username": 'salih',
                "first_name": "salih",
                "last_name": "bilol",
                "email": "salih@gmail.com",
                "password": "qwqw1212",
            }
        )

        user = User.objects.get(username='salih')

        self.assertEqual(user.first_name, "salih")
        self.assertEqual(user.last_name, "salih")
        self.assertEqual(user.email, "salih")
        self.assertNotEqual(user.password, "qwqw1212")
        self.assertTrue(user.check_password('qwqw1212'))

    def test_required_fields(self):
        response = self.client.post(
            data={
                "first_name": "salih",
                "emil": "salih@gmail.com",
            }
        )

        user_count = User.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "username", "This field is required.")
        self.assertFormError(response, "form", "password", "This field is required.")

    def test_invalid_email(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                "username": 'salih',
                "first_name": "salih",
                "last_name": "bilol",
                "email": "salih@gmail.com",
                "password": "qwqw1212",
            }
        )
        user_count = User.objects.count()
        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "email", "This field is required.")


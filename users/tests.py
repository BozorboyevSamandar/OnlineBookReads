from django.contrib.auth import get_user
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

    def test_unique_username(self):
        # create user
        user = User.objects.create(username='salih', first_name='salih')
        user.set_password('qwqw1212')
        user.save()

        # try to create another user with that same username
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
        # check that the second user was to create
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

        # check that the form contains the error message
        self.assertEqual(response, 'form', 'username', "A user with that username already exists.")


class LoginTestCase(TestCase):
    def test_successful_login(self):
        user = User.objects.create(username='salih', first_name='bilal')
        user.set_password('qwqw1212')
        user.save()

        self.client.post(
            reverse('users:login'),
            data={
                "username": 'salih',
                "password": 'qwqw1212',
            }
        )

        user = get_user(self.client)

        self.assertTrue(user.is_authenticated)

    def test_worng_credentials(self):
        user = User.objects.create(username='salih', first_name='bilal')
        user.set_password('qwqw1212')
        user.save()

        self.client.post(
            reverse('users:login'),
            data={
                "username": 'wrong-username',
                "password": 'qwqw1212',
            }
        )

        user = get_user(self.client)

        self.assertTrue(user.is_authenticated)

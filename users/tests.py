from django.contrib.auth import get_user
from users.models import CustomUser
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

        user = CustomUser.objects.get(username='salih')

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

        user_count = CustomUser.objects.count()

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
        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "email", "This field is required.")

    def test_unique_username(self):
        # create user
        user = CustomUser.objects.create(username='salih', first_name='salih')
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
        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 1)

        # check that the form contains the error message
        self.assertEqual(response, 'form', 'username', "A user with that username already exists.")


class LoginTestCase(TestCase):
    def setUp(self):
        self.db_user = CustomUser.objects.create(username='salih', first_name='salih', last_name='bilal')
        self.db_user.set_password('qwqw1212')
        self.db_user.save()

    def test_successful_login(self):
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
        self.client.post(
            reverse('users:login'),
            data={
                "username": 'wrong-username',
                "password": 'qwqw1212',
            }
        )

        user = get_user(self.client)

        self.assertTrue(self, user.is_authenticated)

    def test_logout(self):
        self.client.login(username='salih', password='qwqw1212')

        self.client.get(reverse('users:logout'))

        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)


class ProfileTestCase(TestCase):
    def test_login_required(self):
        response = self.client.get(reverse('users:profile'))

        self.assertEqual(response.url, reverse('users:login'))

    def test_profile_details(self):
        user = User.objects.create(username='salih', first_name='bilal', last_name='bilal', email='sb@gmail.com')
        user.set_password('qwqw1212')
        user.save()

        self.client.login(username='salih', password='qwqw1212')
        response = self.client.get(reverse('users:profile'))

        self.assertContains(response, user.username)
        self.assertContains(response, user.first_name)
        self.assertContains(response, user.last_name)
        self.assertContains(response, user.email)

    def test_user_profile(self):
        user = CustomUser.objects.create(
            username='Salih',
            first_name='Salih',
            last_name='Bilal',
            email='salih@gmail.com',
        )

        user.set_password('qwqw1212')
        user.save()
        self.client.login(username='Salih', password='qwqw1212')

        response = self.client.post(
            reverse('users:profile-edit'),
            data={
                "username": "Salih",
                "first_name": "Salih",
                "last_name": 'Jon',
                'email': 'user@gmail.com'
            }

        )
        user = CustomUser.objects.get(pk=user.pk)

        self.assertEqual(user.last_name, 'Jon')
        self.assertEqual(user.email, 'user@gmail.com')

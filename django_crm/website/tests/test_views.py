from django.test import TestCase, Client
from parameterized import parameterized
from django.urls import reverse
from django.contrib.auth.models import User

from ..froms import SignUpForm
from .test_utils import load_data, csv_to_list_of_tuples


class RegistrationTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user_data = load_data("user.json")

    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        form = SignUpForm(self.user_data)
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse("register"), self.user_data)
        users = User.objects.all()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(users.count(), 1)
        self.assertEqual(users[0].username, self.user_data['username'])


class AuthTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user_data = load_data("user.json")
        form = SignUpForm(self.user_data)
        form.save()

    def test_valid_user_login(self):
        response = self.client.post(reverse("home"),
                                    data={"username": self.user_data["username"],
                                          "password": self.user_data["password1"]})
        print(response)
        self.assertEqual(response.status_code, 302)

    @parameterized.expand(csv_to_list_of_tuples("invalid_login.csv"))
    def test_invalid_user_login(self, username, password):
        response = self.client.post(reverse("home"), follow=True, data={"username": username,
                                                           "password": password})
        self.assertFalse(response.context["user"].is_active)

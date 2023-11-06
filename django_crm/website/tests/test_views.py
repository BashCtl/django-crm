from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from ..froms import SignUpForm

user_data = {
    "username": "johnny",
    "first_name": "John",
    "last_name": "Wick",
    "email": "jowick@test.com",
    "password1": "superduper23",
    "password2": "superduper23"
}


class RegistrationTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user_data = user_data

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
        self.user_data = user_data
        form = SignUpForm(self.user_data)
        form.save()

    def test_valid_user_login(self):
        response = self.client.post(reverse("home"),
                                    data={"username": self.user_data["username"],
                                          "password": self.user_data["password1"]})
        self.assertEqual(response.status_code, 302)

import os

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

TEST_USER = os.environ["TEST_USER"]
TEST_USER_PASSWORD = os.environ["TEST_USER_PASSWORD"]


class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username=TEST_USER, password=TEST_USER_PASSWORD
        )
        self.client = Client()

    def test_profile_edit_page(self):
        url_path = reverse("application:profile_edit")
        response = self.client.get(url_path)
        self.assertEqual(response.status_code, 302)
        self.client.login(username=TEST_USER, password=TEST_USER_PASSWORD)
        assert self.user.is_authenticated
        response = self.client.get(url_path)
        self.assertEqual(response.status_code, 200)

    def test_discover_people_page(self):
        url_path = reverse("application:discover")
        response = self.client.get(url_path)
        self.assertEqual(response.status_code, 302)
        self.client.login(username=TEST_USER, password=TEST_USER_PASSWORD)
        assert self.user.is_authenticated
        response = self.client.get(url_path)
        self.assertEqual(response.status_code, 200)

    # maybe we already have this one?
    # def test_user_logout(self):
    #     update_session(self.client, self.student.username, user_type=UserType.STUDENT)
    #     response = self.client.get(reverse("dashboard:logout"))
    #     self.assertRedirects(response, reverse("landingpage:index"))
    #     # test invalid access
    #     response = self.client.get(reverse("dashboard:dashboard"))
    #     self.assertRedirects(response, reverse("landingpage:index"))


class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("account:login")
        self.user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="testpass"
        )

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_valid_login(self):
        data = {"username": "testuser", "password": "testpass"}
        response = self.client.post(self.url, data, follow=True)
        self.assertRedirects(response, reverse("application:profile_edit"))

    def test_invalid_login(self):
        data = {"username": "testuser", "password": "wrongpass"}
        response = self.client.post(self.url, data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")

        # self.assertContains(response, 'Please enter a correct username and password.')

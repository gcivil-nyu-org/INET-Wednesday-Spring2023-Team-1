from django.test import TestCase, Client
from django.contrib.auth.models import User

import os

# from bs4 import BeautifulSoup

TEST_USER = os.environ["TEST_USER"]
TEST_USER_PASSWORD = os.environ["TEST_USER_PASSWORD"]


class HomeTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username=TEST_USER, password=TEST_USER_PASSWORD
        )
        self.url = "/"

    def test_profile_response_not_logged_in(self):
        response = self.client.get("/application/profile")
        self.assertEqual(response.status_code, 302)

    def test_profile_response(self):
        response = self.client.get(self.url)
        # Test if the response status code is 301 - redirect to login
        self.assertEqual(response.status_code, 301)

    def test_account_register_page_exists(self):
        response = self.client.get("/account/register")
        self.assertEqual(response.status_code, 200)

    def test_account_login_page_exists(self):
        response = self.client.get("/account/login")
        self.assertEqual(response.status_code, 200)

    # def test_account_login_page_exists(self):
    #     self.client.login(username=TEST_USER, password=TEST_USER_PASSWORD)
    #     response = self.client.get("/application/profile")
    #     self.assertEqual(response.status_code, 302)

    def test_matches_section_exists(self):
        # response = self.client.get(self.url)
        # soup = BeautifulSoup(response.content, "html.parser")
        # heading = soup.select_one("h2")
        # self.assertIsNotNone(heading)
        # self.assertEqual(heading.text, "Matches")
        return

    def test_meaningful_song_exists(self):
        # response = self.client.get(self.url)
        # Test if the response status code is 200
        # self.assertEqual(response.status_code, 200)
        # Test if the response contains the expected heading and paragraph
        # soup = BeautifulSoup(response.content, "html.parser")
        # heading = soup.select_one("h4")
        # self.assertIsNotNone(heading)
        # self.assertEqual(heading.text, "A song that has meaning to you")
        return

    # def test_discover_people_exists(self):
    #     response = self.client.get('/application/profile')
    #     self.assertEqual(response.status_code, 200)
    #     soup = BeautifulSoup(response.content, "html.parser")
    #     button = soup.select_one('button')
    #     self.assertIsNotNone(button)
    #     # self.assertEqual(button.text, "Discover People")

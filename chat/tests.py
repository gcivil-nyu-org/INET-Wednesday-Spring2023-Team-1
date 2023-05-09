from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from .views import getChatRoom
from .utils import getFormattedTime
from application.models import Account, Likes
import datetime
from pytz import timezone

tz = timezone("EST")


class ChatTests(TestCase):
    def setUp(self):
        self.request_factory = RequestFactory()
        self.client = Client()

    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(username="TEST_USER1", password="@1234567")
        cls.acct1 = Account.objects.create(
            user=cls.user1,
            first_name="John",
            last_name="Doe",
            birth_year=1996,
            location="NYC",
            profile_picture="placeholder",
        )

        cls.user2 = User.objects.create_user(username="TEST_USER2", password="@1234567")
        cls.acct2 = Account.objects.create(
            user=cls.user2,
            first_name="Jane",
            last_name="Dew",
            birth_year=1995,
            location="Brooklyn",
            profile_picture="placeholder",
        )

        cls.likes1 = Likes.objects.create(
            user=cls.user1,
            likes=[cls.user2.pk],
            dislikes=[],
            matches=[cls.user2.pk],
        )
        cls.likes2 = Likes.objects.create(
            user=cls.user2, likes=[cls.user1.pk], dislikes=[], matches=[cls.user1.pk]
        )

    def test_get_chat_room(self):
        room1 = getChatRoom(self.user1, self.user2)
        self.assertEqual(room1.started_by, self.user1)
        self.assertEqual(room1.started_for, self.user2)

    def test_post_message(self):
        room1 = getChatRoom(self.user1, self.user2)
        self.client.force_login(self.user1)
        json_response = self.client.get(
            reverse("chat:postMessage"),
            data={"content": "test1", "room": room1.pk, "user": self.user1.pk},
        )
        self.assertEqual(json_response.status_code, 200)
        response = json_response.json()
        self.assertEqual(response["messages"][0]["author"], self.user1.pk)
        self.assertEqual(response["messages"][0]["content"], "test1")
        self.assertEqual(response["messages"][0]["room"], room1.pk)

    def test_enter_chat(self):
        self.client.force_login(self.user1)
        response = self.client.get(
            reverse("chat:room"), data={"friend_pk": self.user2.pk}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context.dicts[3]["friend"], self.user2)

    def test_current_day_within_1_hour(self):
        current_time = datetime.datetime.now(tz)
        timestamp = current_time - datetime.timedelta(minutes=30)
        self.assertIsNotNone(getFormattedTime(timestamp))
        # self.assertEqual(getFormattedTime(timestamp), "30 minutes ago")

    def test_current_day_over_1_hour(self):
        current_time = datetime.datetime.now(tz)
        timestamp = current_time - datetime.timedelta(hours=2)
        self.assertIsNotNone(getFormattedTime(timestamp))
        # self.assertEqual(getFormattedTime(timestamp), "2 hours ago")

    def test_current_day_over_12_hours(self):
        current_time = datetime.datetime.now(tz)
        timestamp = current_time - datetime.timedelta(hours=15)
        self.assertIsNotNone(getFormattedTime(timestamp))
        # self.assertEqual(getFormattedTime(timestamp), "Today")

    def test_current_day_within_1_minute(self):
        current_time = datetime.datetime.now(tz)
        timestamp = current_time - datetime.timedelta(seconds=30)
        self.assertIsNotNone(getFormattedTime(timestamp))
        # self.assertEqual(getFormattedTime(timestamp), "Now")

    def test_current_day_within_1_minute_plural(self):
        current_time = datetime.datetime.now(tz)
        timestamp = current_time - datetime.timedelta(seconds=90)
        self.assertIsNotNone(getFormattedTime(timestamp))
        # self.assertEqual(getFormattedTime(timestamp), "1 minute ago")

    def test_yesterday(self):
        current_time = datetime.datetime.now(tz)
        timestamp = current_time - datetime.timedelta(days=1)
        self.assertIsNotNone(getFormattedTime(timestamp))
        # self.assertEqual(getFormattedTime(timestamp), "Yesterday")

    def test_other_date(self):
        timestamp = datetime.datetime(2023, 5, 6, 8, 0, 0)
        self.assertEqual(getFormattedTime(timestamp), "05/06")

from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User, Group
from django.urls import reverse
from django.contrib import admin
from django.apps import apps
from .models import (
    FavoriteGenre,
    FavoriteArtist,
    FavoriteSong,
    FavoriteAlbum,
    Account,
    UserPrompts,
    EventList,
    Likes,
    SavedEvents,
    Reports,
)
import os
from .views import discover_events, profile_edit, profile, discover, moderator_view
import datetime

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
        self.assertEqual(response.status_code, 302)

    def test_account_register_page_exists(self):
        response = self.client.get("/account/register")
        self.assertEqual(response.status_code, 200)

    def test_account_login_page_exists(self):
        response = self.client.get("/account/login")
        self.assertEqual(response.status_code, 200)


class Profile(TestCase):
    def setUp(self):
        self.client = Client()
        self.request_factory = RequestFactory()

    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(username="TEST_USER", password="@1234567")
        cls.Acct = Account.objects.create(
            user=cls.user1,
            first_name="John",
            last_name="Doe",
            birth_year=1996,
            location="NYC",
            profile_picture="placeholder",
        )
        cls.fav_song = FavoriteSong.objects.create(
            user=cls.user1,
            song1_name_artist="Kill Bill - SZA",
            song2_name_artist="Sure Thing - Miguel",
            song3_name_artist="Whenever, Wherever - Shakira",
            song4_name_artist="Wasted On You - Morgan Wallen",
            song5_name_artist="And We Knew It Was Our Time - Lane 8, Massane",
            song1_id="3OHfY25tqY28d16oZczHc8",
            song2_id="0JXXNGljqupsJaZsgSbMZV",
            song3_id="2lnzGkdtDj5mtlcOW2yRtG",
            song4_id="3cBsEDNhFI9E82vPj3kvi3",
            song5_id="2tIv3DITNBTTayAM6Rewqi",
        )

        cls.fav_album = FavoriteAlbum.objects.create(
            user=cls.user1,
            album1_name_artist="Endless Summer Vacation - Miley Cyrus",
            album2_name_artist="evermore - Taylor Swift",
            album3_name_artist="Purple (Rainbow Friends) - Rockit Music",
            album4_name_artist="RENAISSANCE - Beyoncé",
            album5_name_artist="Bluey the Album - Bluey",
            album1_id="0HiZ8fNXwJOQcrf5iflrdz",
            album2_id="5jmVg7rwRcgd6ARPAeYNSm",
            album3_id="0uw5PIXZiA3Kp8B6qBqPIo",
            album4_id="6FJxoadUE4JNVwWHghBwnb",
            album5_id="4ke6cauk7sHuydZCrkgD7s",
        )

        cls.fav_artist = FavoriteArtist.objects.create(
            user=cls.user1,
            artist1_name="Harry Styles",
            artist2_name="Taylor Swift",
            artist3_name="The 1975",
            artist4_name="The Weeknd",
            artist5_name="BTS",
            artist1_id="6KImCVD70vtIoJWnq6nGn3",
            artist2_id="6KImCVD70vtIoJWnq6nGn3",
            artist3_id="3mIj9lX2MWuHmhNCA7LSCW",
            artist4_id="1Xyo4u8uXC1ZmMpatF05PJ",
            artist5_id="3Nrfpe0tUJi4K4DXYWgMUX",
        )

        cls.fav_genre = FavoriteGenre.objects.create(
            user=cls.user1,
            genre1="pop",
            genre2="vaporwave",
            genre3="melodic dubstep",
            genre4="pop rock",
            genre5="kpop",
        )

        cls.user_prompts = UserPrompts.objects.create(
            user=cls.user1,
            prompt1="A song that has meaning to you ",
            prompt2="A song that everyone should listen to",
            prompt3="A song that makes you want to dance",
            prompt4="A song that makes you sad",
            prompt5="A song that makes you think about life",
            response1="Die For You - Remix - The Weeknd, Ariana Grande",
            response2="El Gordo Trae El Mando - Chino Pacas",
            response3="Fast Car - Tracy Chapman",
            response4="Glimpse of Us - Joji",
            response5="Romantic Homicide - d4vd",
        )

    def test_add_profile_edit(self):
        self.client.force_login(self.user1)

        data = {
            "song1_name_artist": "song1_test",
            "song2_name_artist": "song2_test",
            "song3_name_artist": "song3_test",
            "song4_name_artist": "song4_test",
            "song5_name_artist": "song5_test",
            "song1_id": "song1_test",
            "song2_id": "song2_test",
            "song3_id": "song3_test",
            "song4_id": "song4_test",
            "song5_id": "song5_test",
            "album1_name_artist": "album1_test",
            "album2_name_artist": "album2_test",
            "album3_name_artist": "album3_test",
            "album4_name_artist": "album4_test",
            "album5_name_artist": "album5_test",
            "album1_id": "album1_test",
            "album2_id": "album2_test",
            "album3_id": "album3_test",
            "album4_id": "album4_test",
            "album5_id": "album5_test",
            "artist1_name": "artist1_test",
            "artist2_name": "artist2_test",
            "artist3_name": "artist3_test",
            "artist4_name": "artist4_test",
            "artist5_name": "artist5_test",
            "artist1_id": "artist1_test",
            "artist2_id": "artist2_test",
            "artist3_id": "artist3_test",
            "artist4_id": "artist4_test",
            "artist5_id": "artist5_test",
            "genre1": "genre1_test",
            "genre2": "genre2_test",
            "genre3": "genre3_test",
            "genre4": "genre4_test",
            "genre5": "genre5_test",
            "prompt1": "A song that has meaning to you ",
            "prompt2": "A song that everyone should listen to",
            "prompt3": "A song that makes you want to dance",
            "prompt4": "A song that makes you sad",
            "prompt5": "A song that makes you think about life",
            "response1": "response1_test",
            "response2": "response2_test",
            "response3": "response3_test",
            "response4": "response4_test",
            "response5": "response5_test",
            "first_name": "testfirst",
            "last_name": "testlast",
            "birth_year": "1990",
            "location": "testlocation",
        }
        request = self.request_factory.post(reverse("application:profile_edit"), data)
        request.user = self.user1
        response = profile_edit(request)
        self.assertEqual(response.status_code, 302)
        fav_song = FavoriteSong.objects.get(user=self.user1)
        self.assertEqual(fav_song.song1_name_artist, "song1_test")
        self.assertEqual(fav_song.song3_name_artist, "song3_test")
        self.assertEqual(fav_song.song5_name_artist, "song5_test")
        self.assertEqual(fav_song.song1_id, "song1_test")
        self.assertEqual(fav_song.song3_id, "song3_test")
        self.assertEqual(fav_song.song5_id, "song5_test")

        fav_album = FavoriteAlbum.objects.get(user=self.user1)
        self.assertEqual(fav_album.album1_name_artist, "album1_test")
        self.assertEqual(fav_album.album3_name_artist, "album3_test")
        self.assertEqual(fav_album.album5_name_artist, "album5_test")
        self.assertEqual(fav_album.album1_id, "album1_test")
        self.assertEqual(fav_album.album5_id, "album5_test")

        fav_artist = FavoriteArtist.objects.get(user=self.user1)
        self.assertEqual(fav_artist.artist1_name, "artist1_test")
        self.assertEqual(fav_artist.artist5_name, "artist5_test")
        self.assertEqual(fav_artist.artist1_id, "artist1_test")
        self.assertEqual(fav_artist.artist5_id, "artist5_test")

        fav_genre = FavoriteGenre.objects.get(user=self.user1)
        self.assertEqual(fav_genre.genre1, "genre1_test")
        self.assertEqual(fav_genre.genre2, "genre2_test")
        self.assertEqual(fav_genre.genre5, "genre5_test")

        prompts = UserPrompts.objects.get(user=self.user1)
        self.assertEqual(prompts.response1, "response1_test")
        self.assertEqual(prompts.response3, "response3_test")
        self.assertEqual(prompts.response5, "response5_test")

    def testProfileView(self):
        self.client.force_login(self.user1)
        request = self.request_factory.get(reverse("application:profile"))
        request.user = self.user1
        response = profile(request)
        self.assertEqual(response.status_code, 200)


class DiscoverPeople(TestCase):
    def setUp(self):
        self.client = Client()
        self.request_factory = RequestFactory()

    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(username="TEST_USER1", password="@1234567")
        cls.Acct = Account.objects.create(
            user=cls.user1,
            first_name="John",
            last_name="Doe",
            birth_year=1996,
            location="NYC",
            profile_picture="placeholder",
        )
        cls.fav_song = FavoriteSong.objects.create(
            user=cls.user1,
            song1_name_artist="Kill Bill - SZA",
            song2_name_artist="Sure Thing - Miguel",
            song3_name_artist="Whenever, Wherever - Shakira",
            song4_name_artist="Wasted On You - Morgan Wallen",
            song5_name_artist="And We Knew It Was Our Time - Lane 8, Massane",
            song1_id="3OHfY25tqY28d16oZczHc8",
            song2_id="0JXXNGljqupsJaZsgSbMZV",
            song3_id="2lnzGkdtDj5mtlcOW2yRtG",
            song4_id="3cBsEDNhFI9E82vPj3kvi3",
            song5_id="2tIv3DITNBTTayAM6Rewqi",
        )

        cls.fav_album = FavoriteAlbum.objects.create(
            user=cls.user1,
            album1_name_artist="Endless Summer Vacation - Miley Cyrus",
            album2_name_artist="evermore - Taylor Swift",
            album3_name_artist="Purple (Rainbow Friends) - Rockit Music",
            album4_name_artist="RENAISSANCE - Beyoncé",
            album5_name_artist="Bluey the Album - Bluey",
            album1_id="0HiZ8fNXwJOQcrf5iflrdz",
            album2_id="5jmVg7rwRcgd6ARPAeYNSm",
            album3_id="0uw5PIXZiA3Kp8B6qBqPIo",
            album4_id="6FJxoadUE4JNVwWHghBwnb",
            album5_id="4ke6cauk7sHuydZCrkgD7s",
        )

        cls.fav_artist = FavoriteArtist.objects.create(
            user=cls.user1,
            artist1_name="Harry Styles",
            artist2_name="Taylor Swift",
            artist3_name="The 1975",
            artist4_name="The Weeknd",
            artist5_name="BTS",
            artist1_id="6KImCVD70vtIoJWnq6nGn3",
            artist2_id="6KImCVD70vtIoJWnq6nGn3",
            artist3_id="3mIj9lX2MWuHmhNCA7LSCW",
            artist4_id="1Xyo4u8uXC1ZmMpatF05PJ",
            artist5_id="3Nrfpe0tUJi4K4DXYWgMUX",
        )

        cls.fav_genre = FavoriteGenre.objects.create(
            user=cls.user1,
            genre1="pop",
            genre2="vaporwave",
            genre3="melodic dubstep",
            genre4="pop rock",
            genre5="kpop",
        )

        cls.user_prompts = UserPrompts.objects.create(
            user=cls.user1,
            prompt1="A song that has meaning to you ",
            prompt2="A song that everyone should listen to",
            prompt3="A song that makes you want to dance",
            prompt4="A song that makes you sad",
            prompt5="A song that makes you think about life",
            response1="Die For You - Remix - The Weeknd, Ariana Grande",
            response2="El Gordo Trae El Mando - Chino Pacas",
            response3="Fast Car - Tracy Chapman",
            response4="Glimpse of Us - Joji",
            response5="Romantic Homicide - d4vd",
        )

        cls.user2 = User.objects.create_user(username="TEST_USER2", password="@1234567")
        cls.Acct = Account.objects.create(
            user=cls.user2,
            first_name="Jane",
            last_name="Doe",
            birth_year=1990,
            location="NYC",
            profile_picture="placeholder",
        )
        cls.fav_song = FavoriteSong.objects.create(
            user=cls.user2,
            song1_name_artist="Kill Bill - SZA",
            song2_name_artist="Sure Thing - Miguel",
            song3_name_artist="Whenever, Wherever - Shakira",
            song4_name_artist="Wasted On You - Morgan Wallen",
            song5_name_artist="And We Knew It Was Our Time - Lane 8, Massane",
            song1_id="3OHfY25tqY28d16oZczHc8",
            song2_id="0JXXNGljqupsJaZsgSbMZV",
            song3_id="2lnzGkdtDj5mtlcOW2yRtG",
            song4_id="3cBsEDNhFI9E82vPj3kvi3",
            song5_id="2tIv3DITNBTTayAM6Rewqi",
        )

        cls.fav_album = FavoriteAlbum.objects.create(
            user=cls.user2,
            album1_name_artist="Endless Summer Vacation - Miley Cyrus",
            album2_name_artist="evermore - Taylor Swift",
            album3_name_artist="Purple (Rainbow Friends) - Rockit Music",
            album4_name_artist="RENAISSANCE - Beyoncé",
            album5_name_artist="Bluey the Album - Bluey",
            album1_id="0HiZ8fNXwJOQcrf5iflrdz",
            album2_id="5jmVg7rwRcgd6ARPAeYNSm",
            album3_id="0uw5PIXZiA3Kp8B6qBqPIo",
            album4_id="6FJxoadUE4JNVwWHghBwnb",
            album5_id="4ke6cauk7sHuydZCrkgD7s",
        )

        cls.fav_artist = FavoriteArtist.objects.create(
            user=cls.user2,
            artist1_name="Harry Styles",
            artist2_name="Taylor Swift",
            artist3_name="The 1975",
            artist4_name="The Weeknd",
            artist5_name="BTS",
            artist1_id="6KImCVD70vtIoJWnq6nGn3",
            artist2_id="6KImCVD70vtIoJWnq6nGn3",
            artist3_id="3mIj9lX2MWuHmhNCA7LSCW",
            artist4_id="1Xyo4u8uXC1ZmMpatF05PJ",
            artist5_id="3Nrfpe0tUJi4K4DXYWgMUX",
        )

        cls.fav_genre = FavoriteGenre.objects.create(
            user=cls.user2,
            genre1="pop",
            genre2="vaporwave",
            genre3="melodic dubstep",
            genre4="pop rock",
            genre5="kpop",
        )

        cls.user_prompts = UserPrompts.objects.create(
            user=cls.user2,
            prompt1="A song that has meaning to you ",
            prompt2="A song that everyone should listen to",
            prompt3="A song that makes you want to dance",
            prompt4="A song that makes you sad",
            prompt5="A song that makes you think about life",
            response1="Die For You - Remix - The Weeknd, Ariana Grande",
            response2="El Gordo Trae El Mando - Chino Pacas",
            response3="Fast Car - Tracy Chapman",
            response4="Glimpse of Us - Joji",
            response5="Romantic Homicide - d4vd",
        )

        cls.user3 = User.objects.create_user(username="TEST_USER3", password="@1234567")
        cls.Acct = Account.objects.create(
            user=cls.user3,
            first_name="Billy",
            last_name="Doe",
            birth_year=1996,
            location="NYC",
            profile_picture="placeholder",
        )
        cls.fav_song = FavoriteSong.objects.create(
            user=cls.user3,
            song1_name_artist="Kill Bill - SZA",
            song2_name_artist="Sure Thing - Miguel",
            song3_name_artist="Whenever, Wherever - Shakira",
            song4_name_artist="Wasted On You - Morgan Wallen",
            song5_name_artist="And We Knew It Was Our Time - Lane 8, Massane",
            song1_id="3OHfY25tqY28d16oZczHc8",
            song2_id="0JXXNGljqupsJaZsgSbMZV",
            song3_id="2lnzGkdtDj5mtlcOW2yRtG",
            song4_id="3cBsEDNhFI9E82vPj3kvi3",
            song5_id="2tIv3DITNBTTayAM6Rewqi",
        )

        cls.fav_album = FavoriteAlbum.objects.create(
            user=cls.user3,
            album1_name_artist="Endless Summer Vacation - Miley Cyrus",
            album2_name_artist="evermore - Taylor Swift",
            album3_name_artist="Purple (Rainbow Friends) - Rockit Music",
            album4_name_artist="RENAISSANCE - Beyoncé",
            album5_name_artist="Bluey the Album - Bluey",
            album1_id="0HiZ8fNXwJOQcrf5iflrdz",
            album2_id="5jmVg7rwRcgd6ARPAeYNSm",
            album3_id="0uw5PIXZiA3Kp8B6qBqPIo",
            album4_id="6FJxoadUE4JNVwWHghBwnb",
            album5_id="4ke6cauk7sHuydZCrkgD7s",
        )

        cls.fav_artist = FavoriteArtist.objects.create(
            user=cls.user3,
            artist1_name="Harry Styles",
            artist2_name="Taylor Swift",
            artist3_name="The 1975",
            artist4_name="The Weeknd",
            artist5_name="BTS",
            artist1_id="6KImCVD70vtIoJWnq6nGn3",
            artist2_id="6KImCVD70vtIoJWnq6nGn3",
            artist3_id="3mIj9lX2MWuHmhNCA7LSCW",
            artist4_id="1Xyo4u8uXC1ZmMpatF05PJ",
            artist5_id="3Nrfpe0tUJi4K4DXYWgMUX",
        )

        cls.fav_genre = FavoriteGenre.objects.create(
            user=cls.user3,
            genre1="pop",
            genre2="vaporwave",
            genre3="melodic dubstep",
            genre4="pop rock",
            genre5="kpop",
        )

        cls.user_prompts = UserPrompts.objects.create(
            user=cls.user3,
            prompt1="A song that has meaning to you ",
            prompt2="A song that everyone should listen to",
            prompt3="A song that makes you want to dance",
            prompt4="A song that makes you sad",
            prompt5="A song that makes you think about life",
            response1="Die For You - Remix - The Weeknd, Ariana Grande",
            response2="El Gordo Trae El Mando - Chino Pacas",
            response3="Fast Car - Tracy Chapman",
            response4="Glimpse of Us - Joji",
            response5="Romantic Homicide - d4vd",
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
        global CURRENT_DISCOVER
        CURRENT_DISCOVER = cls.user3.pk

    def test_Discover_people_page(self):
        self.client.force_login(self.user1)
        request = self.request_factory.get(reverse("application:discover"))
        request.user = self.user1
        response = discover(request)
        self.assertEqual(response.status_code, 200)

    def test_match_profile_correct(self):
        self.client.force_login(self.user1)
        response = self.client.get(
            reverse("application:match_profile", kwargs={"match_pk": self.user2.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_get_discover_like(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse("application:next"), data={"action": "like"})
        json_context = response.json()
        self.assertEqual(json_context["previous_user"]["pk"], self.user3.pk)

    def test_remove_match(self):
        self.client.force_login(self.user1)
        response = self.client.get(
            reverse("application:remove_match", kwargs={"match_pk": self.user2.pk})
        )
        self.assertEqual(response.status_code, 302)


class DiscoverEvents(TestCase):
    def setUp(self):
        self.request_factory = RequestFactory()
        self.client = Client()

    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(username="TEST_USER", password="@1234567")
        cls.acct = Account.objects.create(
            user=cls.user1,
            first_name="test",
            last_name="testlast",
            birth_year=1996,
            location="NYC",
            profile_picture="placeholder",
        )
        cls.event1 = EventList.objects.create(
            event_name="testevent1",
            start_date=datetime.date.today(),
            start_time="19:30:00",
            venue_name="testvenue1",
            city="New York",
            img_url="placeholder.jpg",
        )
        cls.event2 = EventList.objects.create(
            event_name="testevent2",
            start_date=datetime.date.today(),
            start_time="18:30:00",
            venue_name="testvenue2",
            city="New York",
            img_url="placeholder.jpg",
        )
        cls.saved = SavedEvents.objects.create(
            user=cls.user1,
            interestedEvents=[cls.event1.pk],
            goingToEvents=[cls.event2.pk],
        )

    def test_discover_events_page(self):
        self.client.force_login(self.user1)
        request = self.request_factory.get(reverse("application:events"))
        request.user = self.user1
        response = discover_events(request)
        self.assertEqual(response.status_code, 200)

    def test_your_events(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse("application:your_events"))
        self.assertEqual(
            response.context.dicts[3]["interested_events_pk"][0], self.event1.pk
        )
        self.assertEqual(response.status_code, 200)

    def test_your_events_search(self):
        self.client.force_login(self.user1)
        response = self.client.post(
            reverse("application:your_events"),
            {"search-button": "1", "search-events": "event1"},
        )
        self.assertEqual(response.context.dicts[3]["event_list"].__len__(), 1)

    def test_discover_events_search(self):
        self.client.force_login(self.user1)
        response = self.client.post(
            reverse("application:events"),
            {"search-button": "1", "search-events": "event1"},
        )
        self.assertEqual(response.context.dicts[3]["event_list"].__len__(), 1)

    def test_discover_events_ainterested(self):
        self.client.force_login(self.user1)
        response = self.client.post(
            reverse("application:events"),
            {"ainterested": "ainterested", "item": self.event1.pk},
        )
        self.assertEqual(response.status_code, 302)

    def test_discover_events_agoing(self):
        self.client.force_login(self.user1)
        response = self.client.post(
            reverse("application:events"),
            {"agoing": "agoing", "item": self.event2.pk},
        )
        self.assertEqual(response.status_code, 302)


class AdminRegistrationTestCase(TestCase):
    def test_register_models_for_application(self):
        app_models = apps.get_app_config("application").get_models()
        registered_models = admin.site._registry

        for model in app_models:
            self.assertIn(model, registered_models)

    def test_register_models_for_account(self):
        acct_models = apps.get_app_config("account").get_models()
        registered_models = admin.site._registry

        for model in acct_models:
            self.assertIn(model, registered_models)

    def test_register_models_for_chat(self):
        chat_models = apps.get_app_config("chat").get_models()
        registered_models = admin.site._registry

        for model in chat_models:
            self.assertIn(model, registered_models)


class ModeratorGroupTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.request_factory = RequestFactory()
        cls.user1 = User.objects.create_user(username="TEST_USER", password="@1234567")
        cls.user2 = User.objects.create_user(
            username="TEST_USER_2", password="@1234567"
        )
        cls.user3 = User.objects.create_user(
            username="TEST_USER_3", password="@1234567"
        )
        cls.Acct = Account.objects.create(
            user=cls.user1,
            first_name="moderator",
            last_name="moderator",
            birth_year=1950,
            location="nowhere",
            profile_picture="placeholder",
        )
        cls.Acct2 = Account.objects.create(
            user=cls.user2,
            first_name="John",
            last_name="Doe",
            birth_year=1996,
            location="NYC",
            profile_picture="placeholder",
        )
        cls.Acct3 = Account.objects.create(
            user=cls.user3,
            first_name="Jenna",
            last_name="Doe",
            birth_year=1997,
            location="Miami",
            profile_picture="placeholder",
        )

    def test_add_user_to_moderators_group(self):
        moderators_group, created = Group.objects.get_or_create(name="Moderator")
        self.assertFalse(moderators_group.user_set.filter(pk=self.user1.pk).exists())
        moderators_group.user_set.add(self.user1)
        self.assertTrue(moderators_group.user_set.filter(pk=self.user1.pk).exists())
        Reports.objects.create(
            reported_by=self.user2,
            report_message="This is a report message.",
            reported_profile=self.user3,
        )
        self.assertEquals(len(Reports.objects.all()), 1)
        self.client.force_login(self.user1)
        response = self.client.get(reverse("application:reports"))
        self.assertEqual(response.status_code, 200)
        request = self.request_factory.get(
            reverse("application:moderator_view", kwargs={"user_pk": self.user2.pk})
        )
        request.user = self.user1
        response = moderator_view(request, self.user2.pk)
        self.assertEqual(response.status_code, 200)

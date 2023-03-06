from django.shortcuts import render, HttpResponse
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from .forms import SongEdit, ArtistEdit, AlbumEdit, GenreEdit, PromptEdit
from .models import (
    User,
    FavoriteSong,
    FavoriteGenre,
    FavoriteAlbum,
    FavoriteArtist,
    GenreList,
    UserPrompts,
)


def get_pic(artist_id, spotify):
    artist = spotify.artist(artist_id)
    images = artist["images"]
    img_url = images[1]["url"]
    return img_url


def home(request):
    return HttpResponse("Hello, world. You're at the NYUBeatBuddies application!")


def profile_edit(request):
    client_credentials_manager = SpotifyClientCredentials()
    token_dict = client_credentials_manager.get_access_token()
    token = token_dict["access_token"]

    genres = GenreList.objects.all()

    curr_user = User.objects.get(pk=1)

    if FavoriteSong.objects.filter(
        user=curr_user
    ):  # pre-populate edit form if data exists
        user_fav_songs = FavoriteSong.objects.get(user=curr_user)

        initial_songs = {
            "song1_name_artist": user_fav_songs.song1_name_artist,
            "song2_name_artist": user_fav_songs.song2_name_artist,
            "song3_name_artist": user_fav_songs.song3_name_artist,
            "song4_name_artist": user_fav_songs.song4_name_artist,
            "song5_name_artist": user_fav_songs.song5_name_artist,
            "song1_id": user_fav_songs.song1_id,
            "song2_id": user_fav_songs.song2_id,
            "song3_id": user_fav_songs.song3_id,
            "song4_id": user_fav_songs.song4_id,
            "song5_id": user_fav_songs.song5_id,
        }
    else:
        initial_songs = {}

    if FavoriteArtist.objects.filter(user=curr_user):
        user_fav_artists = FavoriteArtist.objects.get(user=curr_user)
        initial_artists = {
            "artist1_name": user_fav_artists.artist1_name,
            "artist2_name": user_fav_artists.artist2_name,
            "artist3_name": user_fav_artists.artist3_name,
            "artist4_name": user_fav_artists.artist4_name,
            "artist5_name": user_fav_artists.artist5_name,
            "artist1_id": user_fav_artists.artist1_id,
            "artist2_id": user_fav_artists.artist2_id,
            "artist3_id": user_fav_artists.artist3_id,
            "artist4_id": user_fav_artists.artist4_id,
            "artist5_id": user_fav_artists.artist5_id,
        }
    else:
        initial_artists = {}

    if FavoriteAlbum.objects.filter(user=curr_user):
        user_fav_albums = FavoriteAlbum.objects.get(user=curr_user)
        initial_albums = {
            "album1_name_artist": user_fav_albums.album1_name_artist,
            "album2_name_artist": user_fav_albums.album2_name_artist,
            "album3_name_artist": user_fav_albums.album3_name_artist,
            "album4_name_artist": user_fav_albums.album4_name_artist,
            "album5_name_artist": user_fav_albums.album5_name_artist,
            "album1_id": user_fav_albums.album1_id,
            "album2_id": user_fav_albums.album2_id,
            "album3_id": user_fav_albums.album3_id,
            "album4_id": user_fav_albums.album4_id,
            "album5_id": user_fav_albums.album5_id,
        }
    else:
        initial_albums = {}

    if FavoriteGenre.objects.filter(user=curr_user):
        user_fav_genres = FavoriteGenre.objects.get(user=curr_user)
        initial_genres = {
            "genre1": user_fav_genres.genre1,
            "genre2": user_fav_genres.genre2,
            "genre3": user_fav_genres.genre3,
            "genre4": user_fav_genres.genre4,
            "genre5": user_fav_genres.genre5,
        }
    else:
        initial_genres = {}

    if UserPrompts.objects.filter(user=curr_user):
        user_prompts = UserPrompts.objects.get(user=curr_user)

        initial_prompts = {
            "prompt1": user_prompts.prompt1,
            "prompt2": user_prompts.prompt2,
            "prompt3": user_prompts.prompt3,
            "prompt4": user_prompts.prompt4,
            "prompt5": user_prompts.prompt5,
            "response1": user_prompts.response1,
            "response2": user_prompts.response2,
            "response3": user_prompts.response3,
            "response4": user_prompts.response4,
            "response5": user_prompts.response5,
        }
    else:
        initial_prompts = {}

    if request.method == "GET":
        context = {
            "OAuth": token,
            "song_form": SongEdit(None, initial=initial_songs),
            "artist_form": ArtistEdit(None, initial=initial_artists),
            "album_form": AlbumEdit(None, initial=initial_albums),
            "genre_form": GenreEdit(None, initial=initial_genres),
            "prompt_form": PromptEdit(None, initial=initial_prompts),
            "genre_list": genres,
        }

    elif request.method == "POST":
        if "song1_id" in request.POST:  # check which submit button was pressed on page
            if FavoriteSong.objects.filter(  # check if favorite song object exists for user
                user=curr_user
            ):
                model_instance = FavoriteSong.objects.get(user=curr_user)
                form = SongEdit(request.POST, request.FILES, instance=model_instance)
            else:
                form = SongEdit(request.POST, request.FILES)
                form.user = curr_user

            if form.is_valid():
                profile_update = form.save(
                    commit=False
                )  # don't form yet, add user first
                profile_update.user = curr_user
                profile_update.save()

            context = {  # set request.POST to whatever form is being posted
                "OAuth": token,
                "song_form": SongEdit(request.POST or None, initial=initial_songs),
                "artist_form": ArtistEdit(None, initial=initial_artists),
                "album_form": AlbumEdit(None, initial=initial_albums),
                "genre_form": GenreEdit(None, initial=initial_genres),
                "prompt_form": PromptEdit(initial=initial_prompts),
                "genre_list": genres,
            }

        elif "album1_id" in request.POST:
            if FavoriteAlbum.objects.filter(
                user=curr_user
            ):  # check if favorite song object exists for user
                model_instance = FavoriteAlbum.objects.get(user=curr_user)
                form = AlbumEdit(request.POST, request.FILES, instance=model_instance)
            else:
                form = AlbumEdit(request.POST, request.FILES)
                form.user = curr_user

            if form.is_valid():
                profile_update = form.save(commit=False)
                profile_update.user = curr_user
                profile_update.save()

            context = {  # set request.POST to whatever form is being posted
                "OAuth": token,
                "song_form": SongEdit(None, initial=initial_songs),
                "artist_form": ArtistEdit(None, initial=initial_artists),
                "album_form": AlbumEdit(request.POST or None, initial=initial_albums),
                "genre_form": GenreEdit(None, initial=initial_genres),
                "prompt_form": PromptEdit(initial=initial_prompts),
                "genre_list": genres,
            }

        elif "genre1" in request.POST:
            if FavoriteGenre.objects.filter(
                user=curr_user
            ):  # check if favorite song object exists for user
                model_instance = FavoriteGenre.objects.get(user=curr_user)
                form = GenreEdit(request.POST, request.FILES, instance=model_instance)
            else:
                form = GenreEdit(request.POST, request.FILES)
                form.user = curr_user

            if form.is_valid():
                profile_update = form.save(commit=False)
                profile_update.user = curr_user
                profile_update.save()

            context = {  # set request.POST to whatever form is being posted
                "OAuth": token,
                "song_form": SongEdit(None, initial=initial_songs),
                "artist_form": ArtistEdit(None, initial=initial_artists),
                "album_form": AlbumEdit(None, initial=initial_albums),
                "genre_form": GenreEdit(request.POST or None, initial=initial_genres),
                "genre_list": genres,
            }

        elif "artist1_id" in request.POST:
            if FavoriteArtist.objects.filter(
                user=curr_user
            ):  # check if favorite song object exists for user
                model_instance = FavoriteArtist.objects.get(user=curr_user)
                form = ArtistEdit(request.POST, request.FILES, instance=model_instance)
            else:
                form = ArtistEdit(request.POST, request.FILES)
                form.user = curr_user

            if form.is_valid():
                profile_update = form.save(commit=False)
                profile_update.user = curr_user
                profile_update.save()

            context = {  # set request.POST to whatever form is being posted
                "OAuth": token,
                "song_form": SongEdit(None, initial=initial_songs),
                "artist_form": ArtistEdit(
                    request.POST or None, initial=initial_artists
                ),
                "album_form": AlbumEdit(None, initial=initial_albums),
                "genre_form": GenreEdit(None, initial=initial_genres),
                "prompt_form": PromptEdit(initial=initial_prompts),
                "genre_list": genres,
            }
        elif "response1" in request.POST:
            if UserPrompts.objects.filter(
                user=curr_user
            ):  # check if favorite song object exists for user
                model_instance = UserPrompts.objects.get(user=curr_user)
                form = PromptEdit(request.POST, request.FILES, instance=model_instance)
            else:
                form = PromptEdit(request.POST, request.FILES)
                form.user = curr_user

            if form.is_valid():
                profile_update = form.save(commit=False)
                profile_update.user = curr_user
                profile_update.save()

            context = {  # set request.POST to whatever form is being posted
                "OAuth": token,
                "song_form": SongEdit(None, initial=initial_songs),
                "artist_form": ArtistEdit(None, initial=initial_artists),
                "album_form": AlbumEdit(None, initial=initial_albums),
                "genre_form": GenreEdit(None, initial=initial_genres),
                "prompt_form": PromptEdit(
                    request.POST or None, initial=initial_prompts
                ),
                "genre_list": genres,
            }

    return render(request, "application/profile_edit.html", context)


def profile(request):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    curr_user = User.objects.get(pk=1)
    top_artists = FavoriteArtist.objects.get(user=curr_user)
    top_songs = FavoriteSong.objects.get(user=curr_user)
    top_albums = FavoriteAlbum.objects.get(user=curr_user)
    top_genres = FavoriteGenre.objects.get(user=curr_user)

    context = {
        # artists_list:
        "artist1_name": top_artists.artist1_name,
        "artist2_name": top_artists.artist2_name,
        "artist3_name": top_artists.artist3_name,
        "artist4_name": top_artists.artist4_name,
        "artist5_name": top_artists.artist5_name,
        "artist1_id": top_artists.artist1_id,
        "artist2_id": top_artists.artist2_id,
        "artist3_id": top_artists.artist3_id,
        "artist4_id": top_artists.artist4_id,
        "artist5_id": top_artists.artist5_id,
        # songs_list:
        "song1_name_artist": top_songs.song1_name_artist,
        "song2_name_artist": top_songs.song2_name_artist,
        "song3_name_artist": top_songs.song3_name_artist,
        "song4_name_artist": top_songs.song4_name_artist,
        "song5_name_artist": top_songs.song5_name_artist,
        "song1_id": top_songs.song1_id,
        "song2_id": top_songs.song2_id,
        "song3_id": top_songs.song3_id,
        "song4_id": top_songs.song4_id,
        "song5_id": top_songs.song5_id,
        # albums_list:
        "album1_name_artist": top_albums.album1_name_artist,
        "album2_name_artist": top_albums.album2_name_artist,
        "album3_name_artist": top_albums.album3_name_artist,
        "album4_name_artist": top_albums.album4_name_artist,
        "album5_name_artist": top_albums.album5_name_artist,
        "album1_id": top_albums.album1_id,
        "album2_id": top_albums.album2_id,
        "album3_id": top_albums.album3_id,
        "album4_id": top_albums.album4_id,
        "album5_id": top_albums.album5_id,
        # genres_list:
        "genre1": top_genres.genre1,
        "genre2": top_genres.genre2,
        "genre3": top_genres.genre3,
        "genre4": top_genres.genre4,
        "genre5": top_genres.genre5,
        # artist_images_list:
        "artist1_image_url": get_pic(top_artists.artist1_id, spotify),
        "artist2_image_url": get_pic(top_artists.artist2_id, spotify),
        "artist3_image_url": get_pic(top_artists.artist3_id, spotify),
        "artist4_image_url": get_pic(top_artists.artist4_id, spotify),
        "artist5_image_url": get_pic(top_artists.artist5_id, spotify),
    }

    return render(request, "application/profile.html", context)

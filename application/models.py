from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.postgres.fields import ArrayField


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_year = models.CharField(max_length=4, validators=[MinLengthValidator(4)])
    location = models.CharField(max_length=100)
    profile_picture = models.ImageField(
        upload_to="images/", default="images/placeholder.png"
    )

    def __str__(self):
        return f"{self.user.account.first_name} {self.user.account.last_name}"


class SavedEvents(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interestedEvents = ArrayField(models.IntegerField(null=True), null=True)
    goingToEvents = ArrayField(models.IntegerField(null=True), null=True)

    def __str__(self):
        return f"{self.user.account.first_name} {self.user.account.last_name}"


class FavoriteSong(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    song1_id = models.CharField(max_length=50)
    song1_name_artist = models.CharField(max_length=300)
    song2_id = models.CharField(max_length=50)
    song2_name_artist = models.CharField(max_length=300)
    song3_id = models.CharField(max_length=50)
    song3_name_artist = models.CharField(max_length=300)
    song4_id = models.CharField(max_length=50)
    song4_name_artist = models.CharField(max_length=300)
    song5_id = models.CharField(max_length=50)
    song5_name_artist = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.user.account.first_name} {self.user.account.last_name}"


class FavoriteArtist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    artist1_id = models.CharField(max_length=50)
    artist1_name = models.CharField(max_length=300)
    artist2_id = models.CharField(max_length=50)
    artist2_name = models.CharField(max_length=300)
    artist3_id = models.CharField(max_length=50)
    artist3_name = models.CharField(max_length=300)
    artist4_id = models.CharField(max_length=50)
    artist4_name = models.CharField(max_length=300)
    artist5_id = models.CharField(max_length=50)
    artist5_name = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.user.account.first_name} {self.user.account.last_name}"


class FavoriteAlbum(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    album1_id = models.CharField(max_length=50)
    album1_name_artist = models.CharField(max_length=300)
    album2_id = models.CharField(max_length=50)
    album2_name_artist = models.CharField(max_length=300)
    album3_id = models.CharField(max_length=50)
    album3_name_artist = models.CharField(max_length=300)
    album4_id = models.CharField(max_length=50)
    album4_name_artist = models.CharField(max_length=300)
    album5_id = models.CharField(max_length=50)
    album5_name_artist = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.user.account.first_name} {self.user.account.last_name}"


class GenreList(models.Model):
    genre_name = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.genre_name}"


class FavoriteGenre(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genre1 = models.CharField(max_length=300)
    genre2 = models.CharField(max_length=300)
    genre3 = models.CharField(max_length=300)
    genre4 = models.CharField(max_length=300)
    genre5 = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.user.account.first_name} {self.user.account.last_name}"


class PromptList(models.Model):
    prompt = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.prompt}"


class UserPrompts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prompt1 = models.CharField(max_length=300)
    prompt2 = models.CharField(max_length=300)
    prompt3 = models.CharField(max_length=300)
    prompt4 = models.CharField(max_length=300)
    prompt5 = models.CharField(max_length=300)
    response1 = models.CharField(max_length=300)
    response2 = models.CharField(max_length=300)
    response3 = models.CharField(max_length=300)
    response4 = models.CharField(max_length=300)
    response5 = models.CharField(max_length=300)
    response1_id = models.CharField(max_length=300)
    response2_id = models.CharField(max_length=300)
    response3_id = models.CharField(max_length=300)
    response4_id = models.CharField(max_length=300)
    response5_id = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.user.account.first_name} {self.user.account.last_name}"


class Likes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    likes = ArrayField(models.IntegerField(null=True), null=True)
    dislikes = ArrayField(models.IntegerField(null=True), null=True)
    matches = ArrayField(models.IntegerField(null=True), null=True)

    def __str__(self):
        return f"{self.user.account.first_name} {self.user.account.last_name}"


class EventList(models.Model):
    event_name = models.CharField(max_length=300)
    start_date = models.DateField()
    start_time = models.CharField(max_length=8)
    venue_name = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    img_url = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.event_name}-{self.start_date}"


class Reports(models.Model):
    reported_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reported_by"
    )
    report_message = models.CharField(max_length=500)
    reported_time = models.DateTimeField(auto_now_add=True)
    reported_profile = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reported_user"
    )

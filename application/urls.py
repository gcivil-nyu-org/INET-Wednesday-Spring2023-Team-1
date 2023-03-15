from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("profile/edit", views.profile_edit, name="profile_edit"),
    path("profile", views.profile, name="profile"),
    path("discover", views.discover, name="discover"),
]

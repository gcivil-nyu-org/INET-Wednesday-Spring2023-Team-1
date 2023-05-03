from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("profile/edit", views.profile_edit, name="profile_edit"),
    path("profile", views.profile, name="profile"),
    path("discover", views.discover, name="discover"),
    path("next", views.getDiscoverProfile, name="next"),
    path("discover_events", views.discover_events, name="events"),
    path("your_events", views.your_events, name="your_events"),
    path("profile/match/<int:match_pk>/", views.match_profile, name="match_profile"),
    path("moderator_view/<int:user_pk>/", views.moderator_view, name="moderator_view"),
    path(
        "profile/match/remove/<int:match_pk>/", views.remove_match, name="remove_match"
    ),
    path("reports", views.reports, name="reports"),
    path("submit_report", views.submit_report, name="submit_report"),
]

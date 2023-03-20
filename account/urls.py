from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register_request, name="register"),
    path("login", views.login_view, name="login"),
    path("activate/<uidb64>/<token>", views.activate, name="activate"),
    path("logout/", views.logout_view, name="logout"),
]

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth
from .views import registerView, ProfileView

urlpatterns = [
    path("login/", auth.LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path("logout/", auth.LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", registerView.as_view(), name="register"),
    path("profile/", ProfileView, name="profile")
]

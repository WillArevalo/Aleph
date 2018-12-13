"""Accounts URLs."""

# Django
from django.urls import path
from django.contrib.auth.decorators import login_required

# Views
from accounts import views

urlpatterns = [

    # Management
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='me/profile/',
        view=views.UpdateProfileHunterView.as_view(),
        name='update_hunter_profile'
    ),

    # Posts
    path(
        route='<str:username_slug>/',
        view=login_required(views.UserDetailView.as_view()),
        name='detail'
    ),
]
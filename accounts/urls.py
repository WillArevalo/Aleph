"""Accounts URLs."""

# Django
from django.urls import path
from django.contrib.auth.decorators import login_required

# Views
from accounts import views


urlpatterns = [

    # Management
    path(
        route='signup/hunter',
        view=views.SignupHunterView.as_view(),
        name='signuphunter'
    ),
    path(
        route='signup/prey',
        view=views.SignupPreyView.as_view(),
        name='signupprey'
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
        route='hunter/profile/',
        view=views.UpdateProfileHunterView.as_view(),
        name='update_hunter_profile'
    ),
    path(
        route='prey/profile/',
        view=views.UpdateProfilePreyView.as_view(),
        name='update_prey_profile'
    ),

    # Posts
    path(
        route='<str:username_slug>/',
        view=login_required(views.UserDetailView.as_view()),
        name='detail'
    ),
    path('', views.oauth, name='oauth'),
    path('otp-data', views.otpData, name='otp-data'),
    path('otp-form', views.otpForm, name='otp'),
    path('redirect', views.getAuthorizeCode, name='authorize-code'),
    path('access-token', views.getAccessToken, name='access-token'),
]
"""Accounts views."""

# Django
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth.models import User

# Forms
from accounts.forms import SignupHunterForm, SignupPreyForm

# Models

from accounts.models import ProfileHunter, ProfilePrey

# Create your views here.


class SignupHunterView(FormView):
    """Signup View."""
    template_name = 'accounts/signup.html'
    form_class = SignupHunterForm
    success_url = reverse_lazy('accounts:login')
    extra_context = {'is_hunter':True}
    def form_valid(self, form):
        """If the form is valid save the user"""
        form.save()
        return super().form_valid(form)


class SignupPreyView(FormView):
    """Signup View."""
    template_name = 'accounts/signup.html'
    form_class = SignupPreyForm
    success_url = reverse_lazy('accounts:login')
    extra_context = {'is_hunter':False}
    def form_valid(self, form):
        """If the form is valid save the user"""
        form.save()
        return super().form_valid(form)

class LoginView(auth_views.LoginView):
    """Login view"""
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout View."""

class UpdateProfileHunterView(LoginRequiredMixin, UpdateView):
    """Update a user's profile view"""
    template_name = 'accounts/update_profile.html'
    model = ProfileHunter
    fields = ['biography', 'phone_number', 'picture']
    context_object_name = 'profile'
    # Return success url
    def get_object(self):
        """Return user's profile"""
        return self.request.user.profilehunter
    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('accounts:detail', kwargs={'username_slug': username})

class UpdateProfilePreyView(LoginRequiredMixin, UpdateView):
    """Update a user's profile view"""
    template_name = 'accounts/update_profile.html'
    model = ProfilePrey
    fields = ['biography', 'phone_number', 'picture', 'profession']
    context_object_name = 'profile'
    # Return success url
    def get_object(self):
        """Return user's profile"""
        return self.request.user.profileprey
    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('accounts:detail', kwargs={'username_slug': username})


class UserDetailView(DetailView):
    """User detail view."""
    template_name = 'accounts/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username_slug'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_contex_data(self, **kwargs):
        context = super().get_contex_data(**kwargs)
        user = self.get_object()
        context['profile'] = ProfilePrey.objects.get(user=user)
        return context

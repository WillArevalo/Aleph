"""Abilities admin classes."""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# models
from django.contrib.auth.models import User
from vacancies.models import Vacancy
from accounts.models import ProfilePrey
from abilities.models import Ability


@admin.register(Ability)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('pk','skill')
	pass
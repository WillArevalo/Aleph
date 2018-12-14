# Account models

# Django
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from abilities.models import Ability

class ProfileHunter(models.Model):
    """
    ProfileHunter model

    Proxy Model that extends the base data with other information.
    """
    # Relation con la tabla user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Campos extendidos
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )

    is_hunter = models.BooleanField(default=True)
    # time
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username"""
        return self.user.username

class ProfilePrey(models.Model):
    """ProfilePrey model"""
    # Relation con la tabla user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Campos extendidos
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    profession = models.CharField(max_length=250)
    abilities = models.ManyToManyField(Ability)
    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )

    is_hunter = models.BooleanField(default=False)

    # time
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username"""
        return self.user.username

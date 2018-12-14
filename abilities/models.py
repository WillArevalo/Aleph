# Anilities models

# Django
from django.db import models
# Create your models here.

class Ability(models.Model):
    """Ability Model"""
    skill = models.CharField(max_length=150,unique=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return skill"""
        return self.skill

from django.db import models

# Create your models here.
from abilities.models import Ability
from accounts.models import ProfileHunter

class Vacancy(models.Model):
    """Vacancy Model"""
    name = models.CharField(max_length=255)
    description = models.TextField()
    hunter = models.ForeignKey(ProfileHunter, on_delete=models.CASCADE)
    requirements = models.ManyToManyField(Ability)

    def __str__(self):
        """Return name"""
        return self.name
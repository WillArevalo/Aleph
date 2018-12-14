from django import forms

from .models import Ability

class CreateAbilityForm(forms.ModelForm):
	class Meta:
		model = Ability
		fields = ['skill']
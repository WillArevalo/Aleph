"""Vacancies forms"""

# Django
from django import forms

# Models
from vacancies.models import Vacancy
from abilities.models import Ability


class VacancyForm(forms.ModelForm):
	"""Vacancy model form"""
	requirements = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            queryset=Ability.objects.all())

	class Meta:
		"""Form settings."""
		model = Vacancy
		fields = ('name','description','requirements','hunter')
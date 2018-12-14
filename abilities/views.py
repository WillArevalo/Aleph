from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from .models import Ability
from django.urls import reverse_lazy
# Create your views here.

class CreateAbilityView(LoginRequiredMixin, CreateView):
	"""vista para las habilidades"""
	template_name = 'abilities/new.html'
	form_class = forms.CreateAbilityForm
	success_url = reverse_lazy('abilities:list')
	context_objec_name = 'form'

	def get_context_data(self, **kwargs):
		"""agregando un contexto"""
		context = super().get_context_data(**kwargs)
		context['user'] = self.request.user.username
		return context

class AbilitiesListView(LoginRequiredMixin, ListView):
	template_name = 'abilities/list.html'
	model = Ability
	ordering = ('-created',)
	context_object_name = 'abilities'
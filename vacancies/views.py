# Django
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Forms
from vacancies.forms import VacancyForm
# Create your views here.


class CreateVacancyView(LoginRequiredMixin, CreateView):
    """Create New Vacancy View"""
    template_name = 'vacancies/new.html'
    form_class = VacancyForm
    success_url = reverse_lazy('vacancies:feed')
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        """Add User and profile to context."""
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profilehunter
        return context

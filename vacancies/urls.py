from django.urls import path

from . import views

urlpatterns = [
	path(
        route='new',
        view=views.CreateVacancyView.as_view(),
        name='createvacancy'
    ),
]
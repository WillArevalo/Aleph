from django.urls import path

from . import views

urlpatterns = [
	path(
        route='new',
        view=views.CreateVacancyView.as_view(),
        name='createvacancy'
    ),
    path(
    	route='feed',
    	view = views.VacanciesListView.as_view(),
    	name='feed'
    ),
]
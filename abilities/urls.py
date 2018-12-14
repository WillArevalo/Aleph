from django.urls import path
from . import views

urlpatterns =[
	path('new/',views.CreateAbilityView.as_view(), name = 'new'),
	path('list/',views.AbilitiesListView.as_view(),name='list'),
]
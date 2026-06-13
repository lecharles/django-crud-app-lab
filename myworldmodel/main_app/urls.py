from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('observations/', views.observations_index, name='observation-index'),
]
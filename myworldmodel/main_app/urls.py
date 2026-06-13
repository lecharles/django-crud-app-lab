from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('observations/', views.observations_index, name='observation-index'),
    path('observations/create/', views.ObservationCreate.as_view(), name='observation-create'),
    path('observations/<int:observation_id>/', views.observations_detail, name='observation-detail'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('observations/', views.observations_index, name='observation-index'),
    path('observations/create/', views.ObservationCreate.as_view(), name='observation-create'),
    path('observations/<int:observation_id>/', views.observations_detail, name='observation-detail'),
    path('observations/<int:pk>/update/', views.ObservationUpdate.as_view(), name='observation-update'),
    path('observations/<int:pk>/delete/', views.ObservationDelete.as_view(), name='observation-delete'),
    path('observations/<int:observation_id>/add-action/', views.add_action, name='add-action'),
    path('actions/<int:pk>/update/', views.ActionUpdate.as_view(), name='action-update'),
    path('actions/<int:pk>/delete/', views.ActionDelete.as_view(), name='action-delete'),
]
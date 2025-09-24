from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('allergies/details/<int:id>/', views.details, name='details'),
    path('<int:user_id>/', views.allergies, name='allergies'),  # Handles viewing and adding allergies
    path('allergies/<int:id>/update/', views.update_allergy, name='update_allergy'),
    path('allergies/<int:pk>/delete/', views.delete_allergy, name='delete_allergy'),
]


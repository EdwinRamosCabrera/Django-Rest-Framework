from django.urls import path
from .views import paciente_list, paciente_detail

urlpatterns = [
    path('pacientes/', paciente_list, name='paciente-list'),
    path('pacientes/<int:pk>/', paciente_detail, name='paciente-detail'),
]

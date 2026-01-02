from django.urls import path
from .views import paciente_list, paciente_detail, ListPacientes, PacienteDetail

urlpatterns = [
    path('pacientes/', paciente_list, name='paciente-list'),
    path('pacientes/lista/', ListPacientes.as_view(), name='paciente-list-as-view'),
    path('pacientes/<int:pk>/', paciente_detail, name='paciente-detail'),
    path('pacientes/lista/<int:pk>/', PacienteDetail.as_view(), name='paciente-detail-as-view'),
]

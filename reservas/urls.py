from django.urls import path
from .views import CitasListView, DetailCitaView

urlpatterns = [
    path('reservas/', CitasListView.as_view(), name='reserva-list'),
    path('reservas/<int:pk>/', DetailCitaView.as_view(), name='detail-reserva'),
]

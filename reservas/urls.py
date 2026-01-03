from django.urls import path
from .views import ReservaList, CreateReserva, DetailReserva

urlpatterns = [
    path('reservas/', ReservaList.as_view(), name='reserva-list'),
    path('reservas/crear/', CreateReserva.as_view(), name='create-reserva'),
    path('reservas/<int:pk>/', DetailReserva.as_view(), name='detail-reserva'),
]

from django.shortcuts import render
from .serializers import CitaSerializer
from .models import Cita
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

class CitasListView(ListAPIView, CreateAPIView):
    """
    Obtiene la lista de todas las citas medicas programadas o crea una nueva cita.
    """
    allowed_methods = ['GET', 'POST']
    serializer_class = CitaSerializer
    queryset = Cita.objects.all()

class DetailCitaView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = CitaSerializer
    queryset = Cita.objects.all()
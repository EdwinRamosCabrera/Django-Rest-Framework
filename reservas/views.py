from django.shortcuts import render
from .serializers import CitaSerializer
from .models import Cita
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

class ReservaList(ListAPIView, CreateAPIView):
    allowed_methods = ['GET']
    serializer_class = CitaSerializer
    queryset = Cita.objects.all()

class DetailReserva(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET']
    serializer_class = CitaSerializer
    queryset = Cita.objects.all()
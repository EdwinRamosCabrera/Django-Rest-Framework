from rest_framework import serializers
from .models import Cita, NotaMedica

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'

class NotaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaMedica
        fields = '__all__'
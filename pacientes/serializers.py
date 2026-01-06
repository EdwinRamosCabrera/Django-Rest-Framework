from rest_framework import serializers
from .models import Paciente, SeguroMedico, ExpedienteMedico
from reservas.serializers import CitaSerializer

class PacienteSerializer(serializers.ModelSerializer):

    citas = CitaSerializer(many=True, read_only=True) # many=True permite procesas varios elementos de ese mismo tipo, porque un paciente puede tener múltiples citas, read_only significa que este campo es solo de lectura y no se espera que se proporcione al crear o actualizar un paciente, solo se mostraran las citas asociadas al paciente.
    class Meta:
        model = Paciente
        fields = [
        'id',    
        'nombre',
        'apellido',    
        'fecha_nacimiento',
        'telefono',
        'correo',
        'direccion', 
        'historial_medico',
        'citas'
        ]

class SeguroMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeguroMedico
        fields = '__all__'

class ExpedienteMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpedienteMedico
        fields = '__all__'
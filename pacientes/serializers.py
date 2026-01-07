from rest_framework import serializers
from datetime import date
from .models import Paciente, SeguroMedico, ExpedienteMedico
from reservas.serializers import CitaSerializer

class PacienteSerializer(serializers.ModelSerializer):

    citas = CitaSerializer(many=True, read_only=True) # many=True permite procesas varios elementos de ese mismo tipo, porque un paciente puede tener múltiples citas, read_only significa que este campo es solo de lectura y no se espera que se proporcione al crear o actualizar un paciente, solo se mostraran las citas asociadas al paciente.

    edad = serializers.SerializerMethodField() # campo calculado, no existe en el modelo
    # SerializerMethodField busca un método en el serializer con el prefijo "get_" seguido del nombre del campo, en este caso "get_edad"
    class Meta:
        model = Paciente
        fields = [
        'id',    
        'nombre',
        'apellido',
        'edad',    
        'fecha_nacimiento',
        'telefono',
        'correo',
        'direccion', 
        'historial_medico',
        'citas'
        ]

    def get_edad(self, obj):
        edad_td = date.today() - obj.fecha_nacimiento # devuelve un objeto timedelta
        return edad_td.days // 365  # Devuelve la edad en años
        # return f'{edad_td.days // 365} años'} # devuelve la edad agregando años, pero eso debe hacerse en el frontend por el tema de idiomas

class SeguroMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeguroMedico
        fields = '__all__'

class ExpedienteMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpedienteMedico
        fields = '__all__'
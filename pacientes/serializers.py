from    rest_framework import serializers
from    .models import Paciente, SeguroMedico, ExpedienteMedico

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class SeguroMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeguroMedico
        fields = '__all__'

class ExpedienteMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpedienteMedico
        fields = '__all__'
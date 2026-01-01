from rest_framework import serializers
from .models import Doctor, Departamento, DoctorDisponible, NotasMedicas

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class DoctorDisponibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorDisponible
        fields = '__all__'

class NotasMedicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotasMedicas
        fields = '__all__'
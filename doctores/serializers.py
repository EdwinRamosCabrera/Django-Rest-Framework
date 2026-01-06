from rest_framework import serializers
from .models import Doctor, Departamento, DoctorDisponible, NotasMedicas

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
    
    def validate_correo(self, value):
        if '@example.com' not in value:
            raise serializers.ValidationError("El correo electrónico debe pertenecer al dominio '@example.com'.")
        return value
    
    def validate(self, attrs):
        if len(attrs['telefono']) > 10 and attrs['is_on_vacation']:
            raise serializers.ValidationError("Por favor, ingresa un número de teléfono válido y antes de salir de vacaciones.")
        return super().validate(attrs) # continua con la funcionalidad de la clase padre

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
from django.db import models


class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    calificacion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    direccion = models.TextField()
    biografia = models.TextField()

    def __str__(self):
        return f"{self.nombre}"
    
class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
class DoctorDisponible(models.Model):
    doctor = models.ForeignKey(Doctor, related_name="disponibilidades", on_delete=models.CASCADE)
    fecha_inicio= models.DateField()
    fecha_fin = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.doctor.nombre} - {self.fecha_inicio} - {self.fecha_fin}"

class NotasMedicas(models.Model):
    doctor = models.ForeignKey(Doctor, related_name="notas_medicas", on_delete=models.CASCADE)
    nota = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return f"Nota de {self.doctor.nombre} - {self.fecha.strftime('%Y-%m-%d')}"
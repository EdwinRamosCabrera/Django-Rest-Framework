from django.db import models
from pacientes.models import Paciente
from doctores.models import Doctor

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, related_name='citas', on_delete=models.CASCADE)  
    doctor = models.ForeignKey(Doctor, related_name='citas', on_delete=models.CASCADE)
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    motivo = models.TextField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"Cita de {self.paciente.nombre} {self.paciente.apellido} con Dr. {self.doctor.nombre} el {self.fecha_cita} a las {self.hora_cita}"
    
class NotaMedica(models.Model):
    cita = models.ForeignKey(Cita, related_name='notas_medicas', on_delete=models.CASCADE)
    nota = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return f"Nota para cita {self.cita.id} el {self.fecha}"

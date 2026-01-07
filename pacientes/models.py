from django.db import models

class Paciente(models.Model):
    '''
    Modelo que representa a un paciente en el sistema de gestión médica.
    Contiene información personal y médica básica del paciente.
    * Atributos:
    - nombre: Nombre del paciente.
    - apellido: Apellido del paciente.
    - fecha_nacimiento: Fecha de nacimiento del paciente.
    - telefono: Número de teléfono del paciente.
    - correo: Correo electrónico del paciente.
    - direccion: Dirección del paciente.
    - historial_medico: Historial médico del paciente.
    * Metodos:
    - __str__: Retorna una representación en cadena del paciente.
    '''
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    direccion = models.TextField()
    historial_medico = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class SeguroMedico(models.Model):
    paciente = models.ForeignKey(Paciente, related_name="seguros_medicos", on_delete=models.CASCADE)
    proveedor = models.CharField(max_length=100)
    numero_poliza = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_expiracion = models.DateField()

    def __str__(self):
        return f"{self.proveedor} - {self.numero_poliza} for {self.paciente.nombre}"
    
class ExpedienteMedico(models.Model):
    paciente = models.ForeignKey(Paciente, related_name="expedientes_medicos", on_delete=models.CASCADE)
    fecha_creacion = models.DateField()
    diagnostico = models.TextField()
    tratamiento = models.TextField()    
    fecha_actualizacion = models.DateField()

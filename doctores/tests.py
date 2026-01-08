from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from pacientes.models import Paciente
from doctores.models import Doctor

class DoctorViewSetTestCase(TestCase):
    def setUp(self):
        self.paciente = Paciente.objects.create( # definimos self para que pueda ser reusado y accesible en otros metodos de la clase
            nombre="Juan",
            apellido="Perez",
            fecha_nacimiento="1990-01-01",
            telefono="987654321",
            correo="juan.perez@example.com",
            direccion="Calle Falsa 123",
            historial_medico="Ninguno"
        )
        self.doctor = Doctor.objects.create(
            nombre="Ana",
            apellido="Gomez",
            calificacion="Regular",
            telefono="123456789",
            correo="ana.gomez@example.com",
            direccion="Avenida Siempre Viva 456",
            biografia="Especialista en cardiologia con 10 años de experiencia.",
            is_on_vacation=False
        )
       
        # El cliente nos va permitir simular request HTTP a nuestro codigo.
        self.client = APIClient() # APIClient define valor predeterminados para las cabeceras HTTP, como el tipo de contenido y la autenticacion y que nos sirven para hacer pruebas en las vistas de DRF.
    def test_list_should_return_200(self):
        url = reverse('doctor-citas', kwargs={"pk": self.doctor.id})  # Asegúrate de que el nombre de la URL coincida con el definido en tus rutas.
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
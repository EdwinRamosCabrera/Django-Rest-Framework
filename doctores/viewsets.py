from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Doctor
from .serializers import DoctorSerializer
from .permissions import IsDoctor
from reservas.serializers import CitaSerializer 

# ViewSet para el modelo Doctor (CRUD completo)
class DoctorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing doctor instances.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated, IsDoctor] # Solo usuarios autenticados y con rol de doctor pueden acceder.

    # Creacion de acciones personalizadas
    @action(detail=True, methods=['post'], url_path='set-on-vacation') # Al usar detail=True, esta acción se aplica a una instancia específica. Al usar viewsets unimos todas las vistas en una sola clase, por lo tanto, no se sabe si se está trabajando con una lista o con un detalle, por ello se especifica detail=True y este espera un id.
    def set_on_vacation(self, request, pk):
        """
        Custom action to toggle the vacation status of a doctor.
        """
        doctor = self.get_object() # Obtiene la instancia del doctor basado en el pk proporcionado en la URL, usa el ModelViewSet y a traves del queryset obtiene el objeto que tiene el pk correspondiente.
        doctor.is_on_vacation = True
        doctor.save()
        return Response({"status": "El doctor esta en vacaciones"})
    
    @action(detail=True, methods=['post'], url_path='set-off-vacation')
    def set_off_vacation(self, request, pk):
        """
        Custom action to toggle the vacation status of a doctor.
        """
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({"status": "El doctor NO esta en vacaciones"})
    
    @action(detail=True, methods=['get', 'post'], serializer_class=CitaSerializer)
    def citas(self, request, pk=None):
        """
        Custom action to retrieve appointments for a specific doctor.
        """
        doctor = self.get_object()

        if request.method == 'POST':
            # Logic to create a new appointment for the doctor
            data = request.data.copy()
            data['doctor'] = doctor.id
            serializer = CitaSerializer(data=data) # Sino le pasamos un nombre al parametro, el CitasSerializer va enterder el parametro vacio va ser una instancia de Citas, pero lo que estamos pasando es la informacion que el usuario esta enviando para crear una nueva cita.
            serializer.is_valid(raise_exception=True)
            serializer.save(doctor=doctor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if request.method == 'GET':
            # Logic to retrieve appointments for the doctor
            citas = doctor.citas.all() # Accede a todas las citas relacionadas con el doctor utilizando el related_name definido en el modelo Cita.
            serializer = CitaSerializer(citas, many=True) # many=True porque son multiples citas
            return Response(serializer.data)
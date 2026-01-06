from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Doctor
from .serializers import DoctorSerializer
from .permissions import IsDoctor

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
        doctor = self.get_object()
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
    

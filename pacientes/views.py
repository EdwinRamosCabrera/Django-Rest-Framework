from django.shortcuts import render
from .serializers import PacienteSerializer, SeguroMedicoSerializer, ExpedienteMedicoSerializer
from .models import Paciente, SeguroMedico, ExpedienteMedico
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# GET /api/pacientes/ => lista de pacientes
# POST /api/pacientes/ => Crear un nuevo paciente
# GET /api/pacientes/{id}/ => Detalle de un paciente por id
# PUT /api/pacientes/{id}/ => Modificación de un paciente por id

@api_view(['GET', 'POST']) # indica que este endpoint solo acepta peticiones GET
def paciente_list(request):
    if request.method == 'GET':
        pacientes = Paciente.objects.all() # mostramos todos los pacientes
        serializer = PacienteSerializer(pacientes, many=True) # serializamos los pacientes, y el serializer solo es compatible para serializar un item, many=True nos indica que los datos son muchos y que use el mismo serializer para cada uno los items de la lista que le pasamos
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PacienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) # Si los datos son invalidas no se va guardar los datos xq no se va continuar la ejecucion del codigo, por lo tanto ya no seria necesario colocar un if
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT', 'DELETE'])
def paciente_detail(request, pk):
    try:
        paciente = Paciente.objects.get(id=pk)
    except Paciente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PacienteSerializer(paciente)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = PacienteSerializer(paciente, data=request.data) # nos dice que se inicialice con el objeto paciente y se actualice con los datos que vienen en request.data
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        paciente.delete()
        return Response({'message':'Paciente eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)
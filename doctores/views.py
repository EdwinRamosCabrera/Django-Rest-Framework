from django.shortcuts import render
from .serializers import DoctorSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Doctor

@api_view(['GET'])
def doctor_list(request):
    doctores = Doctor.objects.all()
    serializer = DoctorSerializer(doctores, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_doctor(request):
    serializer = DoctorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'Doctor creado correctamente', 'doctor': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def doctor_detail(request, pk):
    try:
        doctor = Doctor.objects.get(id=pk)
    except Doctor.DoesNotExist:
        return Response({'Error':'Doctor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    serializer = DoctorSerializer(doctor)
    return Response(serializer.data)

@api_view(['PUT'])
def update_doctor(request, pk):
    try:
        doctor = Doctor.objects.get(id=pk)
    except Doctor.DoesNotExist:
        return Response({'Error':'Doctor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    serializer = DoctorSerializer(doctor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'Doctor actualizado correctamente', 'doctor': serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_doctor(request, pk):
    try:
        doctor = Doctor.objects.get(id=pk)
    except Doctor.DoesNotExist:
        return Response({'Error':'Doctor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    doctor.delete()
    return Response({'message':'Doctor eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PATCH'])
def modify_doctor(request, pk):
    try:
        doctor = Doctor.objects.get(id=pk)
    except Doctor.DoesNotExist:
        return Response({'Error':'Doctor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    serializer = DoctorSerializer(doctor, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'Doctor modificado correctamente', 'doctor': serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
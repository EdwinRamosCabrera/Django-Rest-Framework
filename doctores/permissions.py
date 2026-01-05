from rest_framework import permissions
from rest_framework import exceptions

class IsDoctor(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated or not request.user.groups.filter(name='doctors').exists():
            raise exceptions.PermissionDenied({'detail': "Usuario no autenticado o no tienes permisos para acceder a este recurso."})
        # Allow access only to users with 'doctor' role
        return request.user and request.user.is_authenticated and request.user.groups.filter(name='doctors').exists()
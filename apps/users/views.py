from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, GroupSerializer
from rest_framework.viewsets import GenericViewSet # type: ignore
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth.models import Group, Permission
from django.db import IntegrityError
from django.middleware.csrf import get_token

from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)

class LoginView(APIView):
    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)

        # Si es correcto añadimos a la request la información de sesión
        if user:
            login(request, user)
            # Obtener el token CSRF
            csrf_token = get_token(request)
            # Devolver el token CSRF en la respuesta
            response_data = {
                'user': UserSerializer(user).data,
                'csrf_token': csrf_token
            }
            return Response(response_data, status=status.HTTP_200_OK)

        # Si no es correcto devolvemos un error en la petición
        return Response(status=status.HTTP_404_NOT_FOUND)

class LogoutView(APIView):
    def post(self, request):
        # Borramos de la request la información de sesión
        logout(request)

        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)
    
# class SignupView(generics.CreateAPIView):
#     serializer_class = UserSerializer

#CRUD relacionado con USER
class UserModelViewSet(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    
    # Permisos para métodos específicos
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    
    # @action(detail=True, methods=['post'], permission_classes=['puede_ver_users'])
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            self.perform_create(serializer)
        except IntegrityError:
            return Response({'error': 'Ya existe un usuario con este correo.'}, status=status.HTTP_400_BAD_REQUEST)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, pk=None):
        # Lógica para el método GET (recuperar)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # Lógica para el método PUT (actualizar)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if 'groups' not in request.data:
            serializer.validated_data['groups'] = instance.groups.all()

        serializer.save()
        return Response(serializer.data)


    def partial_update(self, request, pk=None):
        # Lógica para el método PATCH (actualizar parcialmente)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        # Lógica para el método DELETE (eliminar)
        instance = self.get_object()
        instance.delete()
        return Response(status=204)
    
    @action(detail=True, methods=['post'])
    def add_group(self, request, pk=None):
        user = self.get_object()
        group_id = request.data.get('group_id')
        try:
            group = Group.objects.get(id=group_id)
            user.groups.add(group)
            return Response(status=status.HTTP_200_OK)
        except Group.DoesNotExist:
            return Response({'error': 'Group not found.'}, status=status.HTTP_404_NOT_FOUND)

class GroupModelViewSet(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        instance.delete()
        return Response(status=204)
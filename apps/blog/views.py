from rest_framework.viewsets import GenericViewSet # type: ignore
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from apps.blog.models import (
    Entrada, 
    Comentario, 
    Etiqueta, 
    Categoria, 
    CategoriaEntrada, 
    MeGustaEntrada, 
    MeGustaComentario, 
    EtiquetaEntrada
)
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.response import Response
from .serializers import (
    EntradaSerializer, 
    EtiquetaSerializer, 
    CategoriaSerializer, 
    ComentarioSerializer, 
    CategoriaEntradaSerializer, 
    MeGustaEntradaSerializer,
    MeGustaComentarioSerializer,
    EtiquetaEntradaSerializer
)

#CRUD relacionado con entrada
class MyEntradaViewSet(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    
    # Permisos para métodos específicos
    permission_classes = [IsAuthenticated]
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer
    

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
        # Lógica para el método GET (recuperar)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # Lógica para el método PUT (actualizar)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
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

class MyEtiquetaViewSet(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    # Permisos para métodos específicos
    permission_classes = [IsAuthenticated]
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer

    def list(self, request):
        # Lógica para el método GET (lista)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        # Lógica para el método POST (crear)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def retrieve(self, request, pk=None):
        # Lógica para el método GET (recuperar)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # Lógica para el método PUT (actualizar)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
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
    
class MyCategoriaViewSet(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    # Permisos para métodos específicos
    permission_classes = [IsAuthenticated]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def list(self, request):
        # Lógica para el método GET (lista)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        # Lógica para el método POST (crear)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def retrieve(self, request, pk=None):
        # Lógica para el método GET (recuperar)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # Lógica para el método PUT (actualizar)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
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

class MyComentarioViewSet(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    # Permisos para métodos específicos
    permission_classes = [IsAuthenticated]
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    def list(self, request):
        # Lógica para el método GET (lista)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        # Lógica para el método POST (crear)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def retrieve(self, request, pk=None):
        # Lógica para el método GET (recuperar)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # Lógica para el método PUT (actualizar)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
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

class MyCategoriaEntradaViewSet(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    # Permisos para métodos específicos
    permission_classes = [IsAuthenticated]
    queryset = CategoriaEntrada.objects.all()
    serializer_class = CategoriaEntradaSerializer

    def list(self, request):
        # Lógica para el método GET (lista)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        # Lógica para el método POST (crear)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def retrieve(self, request, pk=None):
        # Lógica para el método GET (recuperar)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # Lógica para el método PUT (actualizar)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
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

class MyMeGustaEntradaViewSet(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    # Permisos para métodos específicos
    permission_classes = [IsAuthenticated]
    queryset = MeGustaEntrada.objects.all()
    serializer_class = MeGustaEntradaSerializer

    def list(self, request):
        # Lógica para el método GET (lista)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        # Lógica para el método POST (crear)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def retrieve(self, request, pk=None):
        # Lógica para el método GET (recuperar)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # Lógica para el método PUT (actualizar)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
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

class MyMeGustaComentarioViewSet(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    # Permisos para métodos específicos
    permission_classes = [IsAuthenticated]
    queryset = MeGustaComentario.objects.all()
    serializer_class = MeGustaComentarioSerializer

    def list(self, request):
        # Lógica para el método GET (lista)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        # Lógica para el método POST (crear)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def retrieve(self, request, pk=None):
        # Lógica para el método GET (recuperar)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # Lógica para el método PUT (actualizar)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
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
    
class MyEtiquetaEntradaViewSet(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    # Permisos para métodos específicos
    permission_classes = [IsAuthenticated]
    queryset = EtiquetaEntrada.objects.all()
    serializer_class = EtiquetaEntradaSerializer

    def list(self, request):
        # Lógica para el método GET (lista)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        # Lógica para el método POST (crear)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def retrieve(self, request, pk=None):
        # Lógica para el método GET (recuperar)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # Lógica para el método PUT (actualizar)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
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


"""Users URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter # type: ignore

# Views
from apps.blog import views as viewset_views

router = DefaultRouter()

router.register(r'entradas', viewset_views.MyEntradaViewSet, basename='entradas')
router.register(r'etiquetas', viewset_views.MyEtiquetaViewSet, basename='etiquetas')
router.register(r'categorias', viewset_views.MyCategoriaViewSet, basename='categorias')
router.register(r'comentario', viewset_views.MyComentarioViewSet, basename='comentario')
router.register(r'categoriaentada', viewset_views.MyCategoriaEntradaViewSet, basename='categoriaentada')
router.register(r'megustaentrada', viewset_views.MyMeGustaEntradaViewSet, basename='megustaentrada')
router.register(r'megustacomentario', viewset_views.MyMeGustaComentarioViewSet, basename='megustacomentario')
router.register(r'etiquetaentrada', viewset_views.MyEtiquetaEntradaViewSet, basename='etiquetaentrada')

urlpatterns = [
    path('', include(router.urls))
]
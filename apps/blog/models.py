from django.db import models
from apps.users.models import CustomUser

# Create your models here.
class BaseModelos(models.Model):
  created = models.DateTimeField(auto_now=False, auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  activo  = models.BooleanField(default=True)
  
  class Meta:
    abstract = True

class Etiqueta(BaseModelos):
  nombre = models.CharField(max_length=50)

  class Meta:
        permissions = [
            ('add_etiqueta_custom', 'Crear MiModelo etiqueta'),
            ('change_etiqueta_custom', 'Puede editar MiModelo etiqueta'),
            ('delete_etiqueta_custom', 'Puede eliminar MiModelo etiqueta'),
            ('view_etiqueta_custom', 'Puede ver MiModelo etiqueta'),
        ]
        default_permissions = []

  def __str__(self):
    """Return Project title."""
    return f'{self.nombre}'

class Categoria(BaseModelos):
  nombre = models.CharField(max_length=50)

  def __str__(self):
    """Return Project title."""
    return f'{self.nombre}'
  
  class Meta:
        permissions = [
            ('add_categoria_custom', 'Crear MiModelo categoria'),
            ('change_categoria_custom', 'Puede editar MiModelo categoria'),
            ('delete_categoria_custom', 'Puede eliminar MiModelo categoria'),
            ('view_categoria_custom', 'Puede ver MiModelo categoria'),
        ]
        default_permissions = []

class Entrada(BaseModelos):
  autor      = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
  titulo     = models.CharField(max_length=350)
  contenido  = models.TextField()

  def __str__(self):
    """Return Project title."""
    return f'{self.autor} | {self.titulo}'
  
  class Meta:
        permissions = [
            ('add_entrada_custom', 'Crear MiModelo entrada'),
            ('change_entrada_custom', 'Puede editar MiModelo entrada'),
            ('delete_entrada_custom', 'Puede eliminar MiModelo entrada'),
            ('view_entrada_custom', 'Puede ver MiModelo entrada'),
        ]
        default_permissions = []

class Comentario(BaseModelos):
  user    = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)
  text    = models.CharField(max_length=500)

  def __str__(self):
    """Return Project title."""
    return f'{self.user} | {self.entrada}'
  
  class Meta:
        permissions = [
            ('add_comentario_custom', 'Crear MiModelo comentario'),
            ('change_comentario_custom', 'Puede editar MiModelo comentario'),
            ('delete_comentario_custom', 'Puede eliminar MiModelo comentario'),
            ('view_comentario_custom', 'Puede ver MiModelo comentario'),
        ]
        default_permissions = []

class MeGustaEntrada(BaseModelos):
  user    = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  entrada = models.OneToOneField(Entrada, on_delete=models.CASCADE)

  def __str__(self):
    """Return Project title."""
    return f'{self.user} | {self.entrada}'
  
  class Meta:
        permissions = [
            ('add_megustaentrada_custom', 'Crear MiModelo megustaentrada'),
            ('change_megustaentrada_custom', 'Puede editar MiModelo megustaentrada'),
            ('delete_megustaentrada_custom', 'Puede eliminar MiModelo megustaentrada'),
            ('view_megustaentrada_custom', 'Puede ver MiModelo megustaentrada'),
        ]
        default_permissions = []


class MeGustaComentario(BaseModelos):
  user       = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  comentario = models.OneToOneField(Comentario, on_delete=models.CASCADE)
  entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)

  def __str__(self):
    """Return Project title."""
    return f'{self.user} | {self.entrada}'


  class Meta:
        permissions = [
            ('add_megustacomentario_custom', 'Crear MiModelo megustacomentario'),
            ('change_megustacomentario_custom', 'Puede editar MiModelo megustacomentario'),
            ('delete_megustacomentario_custom', 'Puede eliminar MiModelo megustacomentario'),
            ('view_megustacomentario_custom', 'Puede ver MiModelo megustacomentario'),
        ]
        default_permissions = []

  
class EtiquetaEntrada(BaseModelos):
  entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)
  etiqueta  = models.ForeignKey(Etiqueta,  on_delete=models.CASCADE)

  def __str__(self):
    """Return Project title."""
    return f'{self.etiqueta} | {self.entrada}'
  
  class Meta:
        permissions = [
            ('add_etiquetaentrada_custom', 'Crear MiModelo etiquetaentrada'),
            ('change_etiquetaentrada_custom', 'Puede editar MiModelo etiquetaentrada'),
            ('delete_etiquetaentrada_custom', 'Puede eliminar MiModelo etiquetaentrada'),
            ('view_etiquetaentrada_custom', 'Puede ver MiModelo etiquetaentrada'),
        ]
        default_permissions = []


class CategoriaEntrada(BaseModelos):
  entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)
  categoria  = models.ForeignKey(Categoria,  on_delete=models.CASCADE)

  def __str__(self):
    """Return Project title."""
    return f'{self.categoria} | {self.entrada}'
  
  class Meta:
        permissions = [
            ('add_categoriaentrada_custom', 'Crear MiModelo categoriaentrada'),
            ('change_categoriaentrada_custom', 'Puede editar MiModelo categoriaentrada'),
            ('delete_categoriaentrada_custom', 'Puede eliminar MiModelo categoriaentrada'),
            ('view_categoriaentrada_custom', 'Puede ver MiModelo categoriaentrada'),
        ]
        default_permissions = []


  




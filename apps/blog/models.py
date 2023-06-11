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

  def __str__(self):
    """Return Project title."""
    return f'{self.nombre}'

class Categoria(BaseModelos):
  nombre = models.CharField(max_length=50)

  def __str__(self):
    """Return Project title."""
    return f'{self.nombre}'

class Entrada(BaseModelos):
  autor      = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
  titulo     = models.CharField(max_length=350)
  contenido  = models.TextField()

  def __str__(self):
    """Return Project title."""
    return f'{self.autor} | {self.titulo}'

class Comentario(BaseModelos):
  user    = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)
  text    = models.CharField(max_length=500)

  def __str__(self):
    """Return Project title."""
    return f'{self.user} | {self.entrada}'

class MeGustaEntrada(BaseModelos):
  user    = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  entrada = models.OneToOneField(Entrada, on_delete=models.CASCADE)

  def __str__(self):
    """Return Project title."""
    return f'{self.user} | {self.entrada}'


class MeGustaComentario(BaseModelos):
  user       = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  comentario = models.OneToOneField(Comentario, on_delete=models.CASCADE)
  entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)

  
class EtiquetaEntrada(BaseModelos):
  entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)
  etiqueta  = models.ForeignKey(Etiqueta,  on_delete=models.CASCADE)

  def __str__(self):
    """Return Project title."""
    return f'{self.etiqueta} | {self.entrada}'


class CategoriaEntrada(BaseModelos):
  entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)
  categoria  = models.ForeignKey(Categoria,  on_delete=models.CASCADE)

  def __str__(self):
    """Return Project title."""
    return f'{self.categoria} | {self.entrada}'


  




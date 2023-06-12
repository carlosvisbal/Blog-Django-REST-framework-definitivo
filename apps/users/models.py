from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=300, null=False)
    photo = models.ImageField(null=True, upload_to='users')
    nombre_completo = models.CharField(max_length=300)
    biografia = models.TextField()
    email = models.EmailField(unique=True, null=True, blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']  # new

    class Meta:
        verbose_name = "Usuario"

    def __str__(self):
        return str(self.username)
    

    class Meta:
        permissions = [
            ('add_customuser_custom', 'Crear MiModelo customuser'),
            ('change_customuser_custom', 'Puede editar MiModelo customuser'),
            ('delete_customuser_custom', 'Puede eliminar MiModelo customuser'),
            ('view_customuser_custom', 'Puede ver MiModelo customuser'),
        ]

        default_permissions = []
    





from django.db import models
from django.core.exceptions import ValidationError

class Registro(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    activo = models.BooleanField(default=True)

    def clean(self):
        if not self.nombre:
            raise ValidationError('El nombre no puede estar vacío.')

    def __str__(self):
        return self.nombre
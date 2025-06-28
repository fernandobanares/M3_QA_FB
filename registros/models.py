from django.db import models

class Registro(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre



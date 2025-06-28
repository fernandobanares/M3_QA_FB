from django.test import TestCase
from .models import Registro

class RegistroTest(TestCase):
    def test_crear_registro(self):
        registro = Registro.objects.create(nombre="Fernando", email="fer@example.com")
        self.assertEqual(registro.nombre, "Fernando")


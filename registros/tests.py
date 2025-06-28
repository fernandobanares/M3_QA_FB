from django.test import TestCase
from .models import Registro

class RegistroTest(TestCase):
    def test_crear_registro(self):
        registro = Registro.objects.create(nombre="Fernando", email="fer@example.com")
        self.assertEqual(registro.nombre, "Fernando")


class RegistroEmailTest(TestCase):

    def test_email_tiene_dominio_valido(self):
        casos = [
            ("Carlos", "carlos@gmail.com", "@gmail.com"),
            ("Laura", "laura@outlook.com", "@outlook.com"),
            ("Empresa", "empleado@miempresa.cl", "@miempresa.cl")
        ]

        for nombre, email, dominio in casos:
            with self.subTest(email=email):
                registro = Registro.objects.create(nombre=nombre, email=email)
                self.assertTrue(registro.email.endswith(dominio))


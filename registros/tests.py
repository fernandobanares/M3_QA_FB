from django.test import TestCase
from .models import Registro

class RegistroTest(TestCase):
    def test_crear_registro(self):
        registro = Registro.objects.create(nombre="Fernando", email="fer@example.com")
        self.assertEqual(registro.nombre, "Fernando")


class RegistroEmailTest(TestCase):
    
    def test_email_con_dominio_gmail(self):
        registro = Registro.objects.create(nombre="Carlos", email="carlos@gmail.com")
        self.assertTrue(registro.email.endswith("@gmail.com"))

    def test_email_con_dominio_outlook(self):
        registro = Registro.objects.create(nombre="Laura", email="laura@outlook.com")
        self.assertTrue(registro.email.endswith("@outlook.com"))

    def test_email_con_dominio_empresa(self):
        registro = Registro.objects.create(nombre="Empresa", email="empleado@miempresa.cl")
        self.assertTrue(registro.email.endswith("@miempresa.cl"))


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
                
class RegistroExtraTest(TestCase):
    def test_nombre_no_esta_vacio(self):
        registro = Registro.objects.create(nombre="Ana", email="ana@mail.com")
        self.assertNotEqual(registro.nombre, "")

    def test_email_contiene_arroba(self):
        registro = Registro.objects.create(nombre="Tomás", email="tomas@mail.com")
        self.assertIn("@", registro.email)

    def test_registro_es_string(self):
        registro = Registro.objects.create(nombre="Lucía", email="lucia@mail.com")
        self.assertEqual(str(registro), "Lucía")

    def test_lista_registros(self):
        Registro.objects.create(nombre="Uno", email="uno@mail.com")
        Registro.objects.create(nombre="Dos", email="dos@mail.com")
        self.assertEqual(Registro.objects.count(), 2)



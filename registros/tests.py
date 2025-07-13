from django.test import TestCase
from .models import Registro

class RegistroCRUDTest(TestCase):
    def test_crear_registro(self):
        registro = Registro.objects.create(nombre="Fernando", email="fer@example.com")
        self.assertEqual(registro.nombre, "Fernando")

    def test_listar_registros(self):
        Registro.objects.create(nombre="Uno", email="uno@mail.com")
        Registro.objects.create(nombre="Dos", email="dos@mail.com")
        registros = Registro.objects.all()
        self.assertEqual(registros.count(), 2)
        
    def test_actualizar_registro(self):
        registro = Registro.objects.create(nombre="Pedro", email="pedro@mail.com")
        registro.nombre = "Pedro Updated"
        registro.save()
        actualizado = Registro.objects.get(id=registro.id)
        self.assertEqual(actualizado.nombre, "Pedro Updated")
        
    def test_eliminar_registro(self):
        registro = Registro.objects.create(nombre="Ana", email="ana@mail.com")
        registro_id = registro.id
        registro.delete()
        #with self.assertRaises(Registro.DoesNotExist):
            Registro.objects.get(id=registro_id)

            

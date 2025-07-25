from django.test import TestCase
from .models import Registro
from django.core.exceptions import ValidationError

class RegistroCRUDTest(TestCase):
    def test_crear_registro(self):
        registro = Registro.objects.create(nombre="Fernando", email="fer@example.com")
        self.assertEqual(registro.nombre, "Fernando")
        
    def test_crear_nombre_vacio(self):
        registro = Registro(nombre="", email="test@mail.com")
        with self.assertRaises(ValidationError):
            registro.full_clean()

    def test_listar_registros(self):
        Registro.objects.create(nombre="Uno", email="uno@mail.com")
        Registro.objects.create(nombre="Dos", email="dos@mail.com")
        registros = Registro.objects.all()
        self.assertEqual(registros.count(), 2)
        
    def test_contar_registros_listados(self):
        Registro.objects.create(nombre="A", email="a@mail.com")
        Registro.objects.create(nombre="B", email="b@mail.com")
        registros = Registro.objects.all()
        self.assertEqual(len(registros), 2)
        
    def test_actualizar_registro(self):
        registro = Registro.objects.create(nombre="Pedro", email="pedro@mail.com")
        registro.nombre = "Pedro Updated"
        registro.save()
        actualizado = Registro.objects.get(id=registro.id)
        self.assertEqual(actualizado.nombre, "Pedro Updated")
        
    def test_cambiar_email(self):
        registro = Registro.objects.create(nombre="Ana", email="ana@old.com")
        registro.email = "ana@new.com"
        registro.save()
        actualizado = Registro.objects.get(id=registro.id)
        self.assertEqual(actualizado.email, "ana@new.com")
        
    def test_eliminar_registro(self):
        registro = Registro.objects.create(nombre="Ana", email="ana@mail.com")
        registro_id = registro.id
        registro.delete()
        with self.assertRaises(Registro.DoesNotExist):
            Registro.objects.get(id=registro_id)
            
    def test_acceso_registro_eliminado(self):
        registro = Registro.objects.create(nombre="Temp", email="temp@mail.com")
        registro_id = registro.id
        registro.delete()
        with self.assertRaises(Registro.DoesNotExist):
            Registro.objects.get(id=registro_id)
            
    def test_email_invalido(self):
        registro = Registro(nombre="Valeria", email="noesuncorreo")
        with self.assertRaises(ValidationError):
            registro.full_clean()


class RegistroValidacionTest(TestCase):
    def test_nombre_no_vacio(self):
        registro = Registro(nombre="", email="test@mail.com")
        with self.assertRaises(ValidationError):
            registro.full_clean()
        
from unittest.mock import patch, MagicMock       
        
class RegistroMockTest(TestCase):

    @patch("registros.models.Registro.__str__", return_value="MockedName")
    def test_mockear_str(self, mock_str):
        registro = Registro(nombre="Carmen", email="carmen@mail.com")
        resultado = str(registro)
        self.assertEqual(resultado, "MockedName")
        mock_str.assert_called_once()

    @patch("registros.models.Registro.save")
    def test_mockear_save(self, mock_save):
        registro = Registro(nombre="Mock", email="mock@mail.com")
        registro.save()
        mock_save.assert_called_once()

    @patch("registros.models.Registro.objects.get")
    def test_mockear_get(self, mock_get):
        mock_registro = MagicMock()
        mock_registro.nombre = "Simulado"
        mock_get.return_value = mock_registro

        resultado = Registro.objects.get(id=1)
        self.assertEqual(resultado.nombre, "Simulado")
        mock_get.assert_called_once_with(id=1)

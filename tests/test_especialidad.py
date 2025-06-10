import unittest
from modelo.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):
    def test_creacion_valida(self):
        e = Especialidad("Pediatría", ["lunes", "miércoles"])
        self.assertTrue(e.verificar_dia("lunes"))
        self.assertFalse(e.verificar_dia("martes"))
        salida = str(e)
        self.assertIn("Pediatría", salida)
        self.assertIn("lunes", salida)

    def test_lista_dias_vacia(self):
        with self.assertRaises(ValueError):
            Especialidad("Cardiología", [])

    def test_dia_invalido(self):
        with self.assertRaises(ValueError):
            Especialidad("Oncología", ["funday"])

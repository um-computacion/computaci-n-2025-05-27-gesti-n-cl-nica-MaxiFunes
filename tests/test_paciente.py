import unittest
from modelo.paciente import Paciente

class TestPaciente(unittest.TestCase):
    def test_creacion_valida(self):
        p = Paciente("Juan Pérez", "12345678", "12/12/2000")
        self.assertEqual(p.obtener_dni(), "12345678")
        self.assertIn("Juan Pérez", str(p))

    def test_dni_invalido(self):
        with self.assertRaises(ValueError):
            Paciente("Ana", "ABC123", "01/01/1990")

    def test_fecha_invalida(self):
        with self.assertRaises(ValueError):
            Paciente("Ana", "87654321", "31-12-2000")

    def test_fecha_futura(self):
        # Suponiendo que hoy es antes de 01/01/3000
        with self.assertRaises(ValueError):
            Paciente("Ana", "87654321", "01/01/3000")

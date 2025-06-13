import unittest
from modelo.receta import Receta
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from modelo.excepciones import RecetaInvalidaException

class TestReceta(unittest.TestCase):
    def setUp(self):
        self.p = Paciente("Ana", "456", "01/02/1990")
        e = Especialidad("Pediatría", ["lunes"])
        self.m = Medico("Dr. López", "M456", [e])

    def test_creacion_receta_valida(self):
        r = Receta(self.p, self.m, ["Paracetamol", "Ibuprofeno"])
        self.assertIn("Paracetamol", str(r))
        self.assertIn("Ibuprofeno", str(r))

    def test_receta_sin_medicamentos(self):
        with self.assertRaises(RecetaInvalidaException):
            Receta(self.p, self.m, [])

    def test_medicamento_vacio_en_lista(self):
        with self.assertRaises(RecetaInvalidaException):
            Receta(self.p, self.m, ["", "Aspirina"])

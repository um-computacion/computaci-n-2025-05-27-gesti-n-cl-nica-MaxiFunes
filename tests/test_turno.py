import unittest
from datetime import datetime, timedelta
from modelo.turno import Turno
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad

class TestTurno(unittest.TestCase):
    def setUp(self):
        self.p = Paciente("Juan", "123", "01/01/1990")
        e = Especialidad("Pediatría", ["lunes", "martes"])
        self.m = Medico("Dr. Pérez", "M123", [e])

    def test_creacion_turno_valido(self):
        fecha_futura = datetime.now() + timedelta(days=1)
        t = Turno(self.p, self.m, fecha_futura, "Pediatría")
        self.assertEqual(t.obtener_medico().obtener_matricula(), "M123")

    def test_turno_en_fecha_pasada(self):
        fecha_pasada = datetime.now() - timedelta(days=1)
        with self.assertRaises(ValueError):
            Turno(self.p, self.m, fecha_pasada, "Pediatría")

    def test_turno_especialidad_invalida(self):
        fecha_futura = datetime.now() + timedelta(days=1)
        with self.assertRaises(ValueError):
            Turno(self.p, self.m, fecha_futura, "")

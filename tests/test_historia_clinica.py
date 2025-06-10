import unittest
from datetime import datetime, timedelta
from modelo.historia_clinica import HistoriaClinica
from modelo.paciente import Paciente
from modelo.turno import Turno
from modelo.receta import Receta
from modelo.medico import Medico
from modelo.especialidad import Especialidad

class TestHistoriaClinica(unittest.TestCase):
    def setUp(self):
        self.p = Paciente("Carlos", "789", "10/10/1980")
        self.hc = HistoriaClinica(self.p)
        e = Especialidad("Cardiología", ["lunes"])
        self.m = Medico("Dr. G", "M789", [e])

    def test_agregar_y_obtener_turnos(self):
        fecha = datetime.now() + timedelta(days=2)
        t = Turno(self.p, self.m, fecha, "Cardiología")
        self.hc.agregar_turno(t)
        turnos = self.hc.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0].obtener_medico().obtener_matricula(), "M789")

    def test_agregar_y_obtener_recetas(self):
        r = Receta(self.p, self.m, ["Medicamento1"])
        self.hc.agregar_receta(r)
        recetas = self.hc.obtener_recetas()
        self.assertEqual(len(recetas), 1)
        self.assertIn("Medicamento1", str(recetas[0]))

    def test_historia_clinica_paciente_invalido(self):
        with self.assertRaises(ValueError):
            HistoriaClinica("NoEsPaciente") # type: ignore

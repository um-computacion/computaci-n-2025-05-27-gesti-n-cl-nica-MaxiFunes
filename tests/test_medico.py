import unittest
from modelo.medico import Medico
from modelo.especialidad import Especialidad

class TestMedico(unittest.TestCase):
    def test_creacion_valida_sin_especialidades(self):
        m = Medico("Dr. López", "M001")
        self.assertEqual(m.obtener_matricula(), "M001")

    def test_agregar_especialidad(self):
        m = Medico("Dr. López", "M001")
        e1 = Especialidad("Pediatría", ["lunes"])
        m.agregar_especialidad(e1)
        self.assertIn("Pediatría", str(m))

    def test_especialidad_duplicada(self):
        m = Medico("Dr. López", "M001")
        e1 = Especialidad("Pediatría", ["lunes"])
        e2 = Especialidad("Pediatría", ["martes"])
        m.agregar_especialidad(e1)
        with self.assertRaises(ValueError):
            m.agregar_especialidad(e2)

    def test_obtener_especialidad_para_dia(self):
        e1 = Especialidad("Pediatría", ["lunes"])
        e2 = Especialidad("Cardiología", ["martes"])
        m = Medico("Dr. López", "M001", [e1, e2])
        self.assertEqual(m.obtener_especialidad_para_dia("martes"), "Cardiología")
        self.assertIsNone(m.obtener_especialidad_para_dia("miércoles"))

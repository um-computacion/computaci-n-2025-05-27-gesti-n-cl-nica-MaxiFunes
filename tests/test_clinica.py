import unittest
from datetime import datetime, timedelta
from modelo.clinica import Clinica
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from modelo.excepciones import (
    PacienteNoEncontradoException,
    MedicoNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        # Crear paciente y médico válidos
        self.p = Paciente("Luis", "111", "01/01/1990")
        self.clinica.agregar_paciente(self.p)
        e = Especialidad("Pediatría", ["lunes", "martes"])
        self.m = Medico("Dr. Luis", "M111", [e])
        self.clinica.agregar_medico(self.m)

    def test_agregar_paciente_duplicado(self):
        with self.assertRaises(ValueError):
            self.clinica.agregar_paciente(Paciente("Luis", "111", "01/01/1990"))

    def test_agregar_medico_duplicado(self):
        with self.assertRaises(ValueError):
            self.clinica.agregar_medico(Medico("Dr. Luis", "M111"))

    def test_agendar_turno_exitoso(self):
        # Elegir día válido: próximo lunes
        proximo_lunes = datetime.now() + timedelta(days=(7 - datetime.now().weekday()) % 7 or 7)
        self.clinica.agendar_turno("111", "M111", "Pediatría", proximo_lunes.replace(hour=10, minute=0, second=0, microsecond=0))
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)

    def test_agendar_turno_paciente_no_existe(self):
        fecha = datetime.now() + timedelta(days=1)
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("999", "M111", "Pediatría", fecha)

    def test_agendar_turno_medico_no_existe(self):
        fecha = datetime.now() + timedelta(days=1)
        with self.assertRaises(MedicoNoEncontradoException):
            self.clinica.agendar_turno("111", "MXYZ", "Pediatría", fecha)

    def test_agendar_turno_medico_no_disponible_dia(self):
        # Elegir un día que no sea lunes o martes (miércoles)
        proximo_miercoles = datetime.now() + timedelta(days=(2 - datetime.now().weekday()) % 7 or 7)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("111", "M111", "Pediatría", proximo_miercoles)

    def test_agendar_turno_duplicado(self):
        proximo_lunes = datetime.now() + timedelta(days=(7 - datetime.now().weekday()) % 7 or 7)
        fecha = proximo_lunes.replace(hour=11, minute=0, second=0, microsecond=0)
        self.clinica.agendar_turno("111", "M111", "Pediatría", fecha)
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("111", "M111", "Pediatría", fecha)

    def test_emitir_receta_exitoso(self):
        self.clinica.emitir_receta("111", "M111", ["Med1", "Med2"])
        # Verificar que la historia clínica tenga la receta
        historia = self.clinica.obtener_historia_clinica_por_dni("111")
        self.assertEqual(len(historia.obtener_recetas()), 1)

    def test_emitir_receta_paciente_no_existe(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.emitir_receta("999", "M111", ["Med1"])

    def test_emitir_receta_medico_no_existe(self):
        with self.assertRaises(MedicoNoEncontradoException):
            self.clinica.emitir_receta("111", "MXYZ", ["Med1"])

    def test_emitir_receta_sin_medicamentos(self):
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("111", "M111", [])

    def test_obtener_historia_clinica_inexistente(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.obtener_historia_clinica_por_dni("999")
        
    def test_obtener_pacientes_y_medicos(self):
        pacientes = self.clinica.obtener_pacientes()
        medicos = self.clinica.obtener_medicos()
        self.assertEqual(len(pacientes), 1)
        self.assertEqual(len(medicos), 1)

from datetime import datetime
from typing import List, Dict
from .paciente import Paciente
from .medico import Medico
from .especialidad import Especialidad
from .turno import Turno
from .receta import Receta
from .historia_clinica import HistoriaClinica
from .excepciones import (
    PacienteNoEncontradoException,
    MedicoNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class Clinica:
    """
    Clase principal que gestiona pacientes, médicos, turnos y recetas.
    Validaciones y lógica:
      - Mantener diccionarios/mapeos de pacientes y médicos.
      - Verificar existencia antes de operar.
      - Traducir día de semana a español.
      - Revisar disponibilidad antes de agendar turno.
      - Guardar turnos y recetas en la historia clínica del paciente.
    """

    def __init__(self):
        self.__pacientes: Dict[str, Paciente] = {}
        self.__medicos: Dict[str, Medico] = {}
        self.__turnos: List[Turno] = []
        self.__historias_clinicas: Dict[str, HistoriaClinica] = {}

    # ---------- MÉTODOS DE REGISTRO ----------

    def agregar_paciente(self, paciente: Paciente):
        dni = paciente.obtener_dni()
        if dni in self.__pacientes:
            raise ValueError(f"Ya existe un paciente con DNI {dni}.")
        self.__pacientes[dni] = paciente
        self.__historias_clinicas[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico: Medico):
        matricula = medico.obtener_matricula()
        if matricula in self.__medicos:
            raise ValueError(f"Ya existe un médico con matrícula {matricula}.")
        self.__medicos[matricula] = medico

    # ---------- MÉTODOS DE VALIDACIÓN ----------

    def validar_existencia_paciente(self, dni: str):
        if dni not in self.__pacientes:
            raise PacienteNoEncontradoException(f"Paciente con DNI {dni} no encontrado.")

    def validar_existencia_medico(self, matricula: str):
        if matricula not in self.__medicos:
            raise MedicoNoEncontradoException(f"Médico con matrícula {matricula} no encontrado.")

    def validar_turno_no_duplicado(self, matricula: str, fecha_hora: datetime):
        # Verificar si ya existe un turno para ese médico y fecha/hora exacta
        for t in self.__turnos:
            if t.obtener_medico().obtener_matricula() == matricula and t.obtener_fecha_hora() == fecha_hora:
                raise TurnoOcupadoException("Ya existe un turno para ese médico en esa fecha y hora.")

    def obtener_dia_semana_en_espanol(self, fecha_hora: datetime) -> str:
        # Traducir manualmente:
        dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        return dias[fecha_hora.weekday()]

    def validar_especialidad_en_dia(self, medico: Medico, especialidad_solicitada: str, dia_semana: str):
        # Verifica si el médico atiende la especialidad ese día
        disponible = False
        for e in medico._Medico__especialidades: # type: ignore
            if e.obtener_especialidad().lower() == especialidad_solicitada.lower():
                if e.verificar_dia(dia_semana):
                    disponible = True
                break
        if not disponible:
            raise MedicoNoDisponibleException(f"El médico no atiende {especialidad_solicitada} el día {dia_semana}.")

    # ---------- MÉTODOS PRINCIPALES ----------

    def agendar_turno(self, dni: str, matricula: str, especialidad: str, fecha_hora: datetime):
        # 1) Verificar existencia de paciente y médico
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)

        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]

        # 2) Verificar que la especialidad esté en la lista del médico en ese día
        dia_semana = self.obtener_dia_semana_en_espanol(fecha_hora)
        self.validar_especialidad_en_dia(medico, especialidad, dia_semana)

        # 3) Verificar que no haya turno duplicado
        self.validar_turno_no_duplicado(matricula, fecha_hora)

        # 4) Crear y guardar Turno
        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.__turnos.append(turno)
        # Agregar a la historia clínica
        self.__historias_clinicas[dni].agregar_turno(turno)

    def emitir_receta(self, dni: str, matricula: str, medicamentos: list[str]):
        # 1) Verificar existencia de paciente y médico
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)

        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]

        # 2) Construir Receta (lanza RecetaInvalidaException si meds vacíos)
        receta = Receta(paciente, medico, medicamentos)

        # 3) Guardar en historia clínica
        self.__historias_clinicas[dni].agregar_receta(receta)

    # ---------- MÉTODOS DE CONSULTA ----------

    def obtener_pacientes(self) -> list[Paciente]:
        return list(self.__pacientes.values())

    def obtener_medicos(self) -> list[Medico]:
        return list(self.__medicos.values())

    def obtener_medico_por_matricula(self, matricula: str) -> Medico:
        self.validar_existencia_medico(matricula)
        return self.__medicos[matricula]

    def obtener_turnos(self) -> list[Turno]:
        return list(self.__turnos)

    def obtener_historia_clinica_por_dni(self, dni: str) -> HistoriaClinica:
        self.validar_existencia_paciente(dni)
        return self.__historias_clinicas[dni]

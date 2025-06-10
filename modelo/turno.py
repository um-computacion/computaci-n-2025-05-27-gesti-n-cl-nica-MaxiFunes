from datetime import datetime

class Turno:
    """
    Representa un turno médico.
    Validaciones:
      - paciente y medico deben ser objetos válidos (se asume validados antes de llamar al constructor).
      - fecha_hora debe ser instancia de datetime y no pasada.
      - especialidad no vacía.
    """
    def __init__(self, paciente, medico, fecha_hora: datetime, especialidad: str):
        if not hasattr(paciente, "obtener_dni"):
            raise ValueError("paciente inválido.")
        if not hasattr(medico, "obtener_matricula"):
            raise ValueError("médico inválido.")

        if not isinstance(fecha_hora, datetime):
            raise ValueError("fecha_hora debe ser un datetime válido.")
        if fecha_hora < datetime.now():
            raise ValueError("No se puede crear un turno en fecha pasada.")
        self.__fecha_hora = fecha_hora

        if not especialidad or not especialidad.strip():
            raise ValueError("La especialidad del turno no puede estar vacía.")
        self.__especialidad = especialidad.strip()

        self.__paciente = paciente
        self.__medico = medico

    def obtener_medico(self):
        return self.__medico

    def obtener_fecha_hora(self) -> datetime:
        return self.__fecha_hora

    def __str__(self) -> str:
        return (f"Turno(Paciente: {self.__paciente}, "
                f"Medico: {self.__medico}, "
                f"Especialidad: {self.__especialidad}, "
                f"FechaHora: {self.__fecha_hora.strftime('%d/%m/%Y %H:%M')})")

from datetime import datetime
from .excepciones import RecetaInvalidaException

class Receta:
    """
    Representa una receta médica.
    Validaciones:
      - paciente y medico deben ser objetos válidos (asumidos previos).
      - lista de medicamentos no vacía.
      - la fecha se asigna automáticamente con datetime.now()
    """
    def __init__(self, paciente, medico, medicamentos: list[str]):
        if not hasattr(paciente, "obtener_dni"):
            raise ValueError("paciente inválido.")
        if not hasattr(medico, "obtener_matricula"):
            raise ValueError("médico inválido.")
        if not medicamentos or not isinstance(medicamentos, list):
            raise RecetaInvalidaException("La lista de medicamentos no puede estar vacía.")
        for m in medicamentos:
            if not isinstance(m, str) or not m.strip():
                raise RecetaInvalidaException("Cada medicamento debe ser una cadena no vacía.")
        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = [m.strip() for m in medicamentos]
        self.__fecha = datetime.now()

    def __str__(self) -> str:
        meds = ", ".join(self.__medicamentos)
        fecha_str = self.__fecha.strftime("%d/%m/%Y %H:%M")
        return (f"Receta(Paciente: {self.__paciente}, "
                f"Medico: {self.__medico}, "
                f"Medicamentos: [{meds}], "
                f"Fecha: {fecha_str})")

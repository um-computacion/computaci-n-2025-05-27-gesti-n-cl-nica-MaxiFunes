class PacienteNoEncontradoException(Exception):
    """Se lanza cuando un paciente no existe en el sistema."""
    pass


class MedicoNoEncontradoException(Exception):
    """Se lanza cuando un médico no existe en el sistema."""
    pass


class MedicoNoDisponibleException(Exception):
    """Se lanza cuando el médico no atiende en ese día o especialidad."""
    pass


class TurnoOcupadoException(Exception):
    """Se lanza cuando ya existe otro turno para el mismo médico y fecha/hora."""
    pass


class RecetaInvalidaException(Exception):
    """Se lanza cuando la receta no puede crearse (por ejemplo, lista de medicamentos vacía)."""
    pass

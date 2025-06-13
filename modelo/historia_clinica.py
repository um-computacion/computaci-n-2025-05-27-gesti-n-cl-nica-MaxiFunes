from typing import List
from .paciente import Paciente

class HistoriaClinica:
    """
    Representa la historia clínica de un paciente:
      - Guarda lista de objetos Turno y Receta.
    Validaciones:
      - paciente debe existir (asumido por la creación en Clinica).
    """
    
    def __init__(self, paciente: Paciente):
        # Validar paciente
        if not isinstance(paciente, Paciente):
            raise ValueError("Paciente debe ser una instancia de la clase Paciente")
        
        self.__paciente = paciente
        self.__turnos: List = []
        self.__recetas: List = []
    
    def agregar_turno(self, turno):
        from .turno import Turno
        if not isinstance(turno, Turno):
            raise ValueError("Debe agregar un objeto Turno válido.")
        self.__turnos.append(turno)
    
    def obtener_turnos(self) -> List:
        return list(self.__turnos)
    
    def agregar_receta(self, receta):
        from .receta import Receta
        if not isinstance(receta, Receta):
            raise ValueError("Debe agregar un objeto Receta válido.")
        self.__recetas.append(receta)
    
    def obtener_recetas(self) -> List:
        return list(self.__recetas)
    
    def __str__(self) -> str:
        turnos_str = "\n  ".join(str(t) for t in self.__turnos) or "Sin turnos."
        recetas_str = "\n  ".join(str(r) for r in self.__recetas) or "Sin recetas."
        return (f"HistoriaClinica(Paciente: {self.__paciente})\n"
                f" Turnos:\n  {turnos_str}\n"
                f" Recetas:\n  {recetas_str}")

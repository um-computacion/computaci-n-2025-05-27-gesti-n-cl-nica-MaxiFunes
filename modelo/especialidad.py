class Especialidad:
    """
    Representa una especialidad médica con días de atención.
    Validaciones:
      - tipo no vacío.
      - lista de días no vacía, cada día en minúsculas y uno de: lunes, martes, miércoles, jueves, viernes, sábado, domingo.
    """
    DIAS_VALIDOS = {"lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"}

    def __init__(self, tipo: str, dias: list[str]):
        if not tipo or not tipo.strip():
            raise ValueError("El tipo de especialidad no puede estar vacío.")
        self.__tipo = tipo.strip()

        if not dias or not isinstance(dias, list):
            raise ValueError("La lista de días no puede estar vacía.")
        dias_normalizados = []
        for d in dias:
            if not isinstance(d, str):
                raise ValueError("Cada día debe ser una cadena de texto.")
            dia_lower = d.strip().lower()
            if dia_lower not in self.DIAS_VALIDOS:
                raise ValueError(f"Día inválido: {d}.")
            dias_normalizados.append(dia_lower)
        self.__dias = dias_normalizados

    def obtener_especialidad(self) -> str:
        return self.__tipo

    def verificar_dia(self, dia: str) -> bool:
        """
        Retorna True si la especialidad está disponible el día dado (no sensible a mayúsculas).
        """
        if not dia or not isinstance(dia, str):
            return False
        return dia.strip().lower() in self.__dias

    def __str__(self) -> str:
        dias_str = ", ".join(self.__dias)
        return f"{self.__tipo} (Días: {dias_str})"

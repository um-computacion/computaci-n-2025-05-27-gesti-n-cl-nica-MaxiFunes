from datetime import datetime
import re

class Paciente:
    """
    Representa un paciente de la clínica.
    Validaciones:
      - DNI solo dígitos, longitud mínima 1.
      - Fecha nacimiento en formato 'dd/mm/aaaa' válida y no futura.
    """
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        # Validar nombre no vacío
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del paciente no puede estar vacío.")
        self.__nombre = nombre.strip()

        # Validar DNI: solo dígitos
        if not dni or not dni.isdigit():
            raise ValueError("El DNI debe contener solo dígitos.")
        self.__dni = dni

        # Validar formato de fecha 'dd/mm/aaaa'
        try:
            fecha_obj = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
        except ValueError:
            raise ValueError("La fecha de nacimiento debe tener formato dd/mm/aaaa.")
        # Validar que no sea fecha futura
        if fecha_obj > datetime.now():
            raise ValueError("La fecha de nacimiento no puede ser futura.")
        self.__fecha_nacimiento = fecha_nacimiento

    def obtener_dni(self) -> str:
        return self.__dni

    def __str__(self) -> str:
        return f"{self.__nombre}, {self.__dni}, {self.__fecha_nacimiento}"

from modelo.clinica import Clinica
from interfaz.cli import CLI

def main():
    sistema = Clinica()
    interfaz = CLI(sistema)
    interfaz.iniciar()

if __name__ == "__main__":
    main()

# main.py
from Controlador.controlador import Controlador

if __name__ == "__main__":
    app = Controlador()
    try:
        app.ejecutar()
    finally:
        app.modelo.cerrar_conexion()

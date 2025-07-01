# main.py
from Controller.desviacion_Es_controller import Controlador

if __name__ == "__main__":
    app = Controlador()
    try:
        app.ejecutar()
    finally:
        app.modelo.cerrar_conexion()

from Model.desviacion_Es import Modelo
from View.desviacion_Es_view import Vista

class Controlador:
    def __init__(self):
        self.modelo = Modelo()
        self.vista = Vista()

    def ejecutar(self):
        while True:
            opcion = self.vista.mostrar_menu()

            if opcion == '1':
                datos = self.vista.pedir_datos_manual()
                if datos:
                    self.modelo.guardar_conjunto_datos("manual", datos)

            elif opcion == '2':
                datos_predefinidos = [76, 97, 87, 46, 86, 25, 96]
                self.modelo.guardar_conjunto_datos("predefinido", datos_predefinidos)

            elif opcion == '3':
                datos = self.modelo.leer_ultimo_conjunto()
                if not datos:
                    print("⚠️ No hay conjuntos guardados.")
                    continue

            elif opcion ==  'salir':
                print("👋¡Hasta luego!")
                break

            else:
                print("❌ Opción inválida. Intente de nuevo.")
                continue

            
            desviacion = self.modelo.calcular_desviacion_estandar()
            if desviacion is not None:
                self.vista.mostrar_resultado(desviacion, self.modelo.datos)
                self.vista.graficar_resultado(self.modelo.datos, desviacion)
            else:
                print("⚠️ No hay suficientes datos para calcular la desviación estándar.")

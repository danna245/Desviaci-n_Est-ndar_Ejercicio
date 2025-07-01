from Modelo.modelo import Modelo
from Vista.vista import Vista

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
                datos_predefinidos = [86, 87, 88, 86, 87, 85, 86]
                self.modelo.guardar_conjunto_datos("predefinido", datos_predefinidos)

            elif opcion == '3':
                datos = self.modelo.leer_ultimo_conjunto()
                if not datos:
                    print("⚠️ No hay conjuntos guardados.")
                    continue

            elif opcion == '0':
                print("👋 Programa finalizado.")
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

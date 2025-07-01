import matplotlib.pyplot as plt

class Vista:
    def mostrar_menu(self):
        print("\n==== MENÚ ====")
        print("1. Ingresar datos manualmente")
        print("2. Usar datos predefinidos")
        print("3. Leer último conjunto guardado")
        print("0. Salir")
        return input("Seleccione una opción: ")

    def pedir_datos_manual(self):
        entrada = input("Ingrese los números separados por comas: ")
        try:
            numeros = list(map(float, entrada.split(',')))
            return numeros
        except ValueError:
            print("⚠️ Error: Asegúrese de ingresar solo números válidos.")
            return None

    def mostrar_resultado(self, desviacion, datos):
        print(f"\n📊 Datos utilizados: {datos}")
        print(f"📈 Desviación estándar: {desviacion:.2f}")

    def graficar_resultado(self, datos, desviacion):
        plt.figure(figsize=(8, 5))
        plt.plot(datos, marker='o', label='Datos')
        plt.axhline(y=desviacion, color='red', linestyle='--',
                    label=f'Desviación estándar ≈ {desviacion:.2f}')
        plt.title("Visualización de Desviación Estándar")
        plt.xlabel("Índice")
        plt.ylabel("Valor")
        plt.grid(True)
        plt.legend()
        plt.show()

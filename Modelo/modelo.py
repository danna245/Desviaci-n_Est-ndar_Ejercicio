import mysql.connector
import statistics

class Modelo:
    def __init__(self):
        self.datos = []
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="desviacion_datos"
        )
        self.cursor = self.conexion.cursor()

    def guardar_conjunto_datos(self, nombre, lista_valores):

        sql_conjunto = "INSERT INTO conjunto_datos (nombre) VALUES (%s)"
        self.cursor.execute(sql_conjunto, (nombre,))
        id_conjunto = self.cursor.lastrowid

        
        sql_valores = "INSERT INTO valores_velocidad (id_conjunto, valor) VALUES (%s, %s)"
        datos = [(id_conjunto, v) for v in lista_valores]
        self.cursor.executemany(sql_valores, datos)

        self.conexion.commit()
        self.datos = lista_valores 

    def leer_ultimo_conjunto(self):
        sql = """
        SELECT v.valor
        FROM valores_velocidad v
        INNER JOIN conjunto_datos c ON v.id_conjunto = c.id
        WHERE c.id = (SELECT MAX(id) FROM conjunto_datos)
        """
        self.cursor.execute(sql)
        self.datos = [row[0] for row in self.cursor.fetchall()]
        return self.datos

    def calcular_desviacion_estandar(self):
        if len(self.datos) < 2:
            return None
        return statistics.stdev(self.datos)

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()

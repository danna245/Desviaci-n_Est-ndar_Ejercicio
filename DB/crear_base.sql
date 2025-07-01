//Creación de la base de datos y tablas para almacenar los datos de velocidad
CREATE DATABASE IF NOT EXISTS desviacion_datos;
USE desviacion_datos;

CREATE TABLE IF NOT EXISTS conjunto_datos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS valores_velocidad (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_conjunto INT,
    valor FLOAT NOT NULL,
    FOREIGN KEY (id_conjunto) REFERENCES conjunto_datos(id) ON DELETE CASCADE
);

-- Crear base de datos (si no existe)
CREATE DATABASE IF NOT EXISTS rpm_db;
USE rpm_db;

-- Tabla categorías
CREATE TABLE IF NOT EXISTS categories (
    idCategory INT AUTO_INCREMENT PRIMARY KEY,
    nombreCategoria VARCHAR(255) NOT NULL UNIQUE
);

-- Tabla productos
CREATE TABLE IF NOT EXISTS products (
    idProduct INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    inventario INT DEFAULT 0,
    categoria_id INT NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES categories(idCategory) ON DELETE CASCADE
);

-- Datos iniciales
INSERT INTO categories (nombreCategoria) VALUES
('Electrónica'),
('Ropa'),
('Hogar');

INSERT INTO products (nombre, inventario, categoria_id) VALUES
('Laptop', 15, 1),
('Camisa', 30, 2),
('Silla', 20, 3);

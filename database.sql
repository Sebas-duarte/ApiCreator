-- Crear base de datos (si no existe)
CREATE DATABASE IF NOT EXISTS rpm_db;
USE rpm_db;

-- Crear tabla de categorías
CREATE TABLE IF NOT EXISTS categories (
    idCategory INTEGER PRIMARY KEY AUTOINCREMENT,
    nombreCategoria TEXT NOT NULL UNIQUE
);

-- Crear tabla de productos
CREATE TABLE IF NOT EXISTS products (
    idProduct INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    inventario INTEGER DEFAULT 0,
    categoria_id INTEGER NOT NULL,
    FOREIGN KEY(categoria_id) REFERENCES categories(idCategory)
);

-- Insertar datos iniciales
INSERT INTO categories (nombreCategoria) VALUES ('Electrónica');
INSERT INTO categories (nombreCategoria) VALUES ('Ropa');

INSERT INTO products (nombre, inventario, categoria_id) VALUES ('Laptop', 10, 1);
INSERT INTO products (nombre, inventario, categoria_id) VALUES ('Camiseta', 20, 2);

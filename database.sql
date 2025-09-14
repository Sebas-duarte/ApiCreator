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

-- Insertar datos de ejemplo en categorías
INSERT INTO categories (nombreCategoria) VALUES ('Electrónica');
INSERT INTO categories (nombreCategoria) VALUES ('Hogar');
INSERT INTO categories (nombreCategoria) VALUES ('Deportes');

-- Insertar datos de ejemplo en productos
INSERT INTO products (nombre, inventario, categoria_id) VALUES ('Televisor', 10, 1);
INSERT INTO products (nombre, inventario, categoria_id) VALUES ('Laptop', 5, 1);
INSERT INTO products (nombre, inventario, categoria_id) VALUES ('Aspiradora', 7, 2);
INSERT INTO products (nombre, inventario, categoria_id) VALUES ('Cafetera', 3, 2);
INSERT INTO products (nombre, inventario, categoria_id) VALUES ('Pelota de fútbol', 20, 3);
INSERT INTO products (nombre, inventario, categoria_id) VALUES ('Raqueta', 15, 3);

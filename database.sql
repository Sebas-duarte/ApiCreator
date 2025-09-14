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


-- Insertar categorías (solo si no existen)
INSERT OR IGNORE INTO categories (idCategory, nombreCategoria) VALUES (1, 'Electrónica');
INSERT OR IGNORE INTO categories (idCategory, nombreCategoria) VALUES (2, 'Hogar');
INSERT OR IGNORE INTO categories (idCategory, nombreCategoria) VALUES (3, 'Deportes');

-- Insertar productos (solo si no existen)
INSERT OR IGNORE INTO products (idProduct, nombre, inventario, categoria_id) VALUES (1, 'Televisor', 10, 1);
INSERT OR IGNORE INTO products (idProduct, nombre, inventario, categoria_id) VALUES (2, 'Laptop', 5, 1);
INSERT OR IGNORE INTO products (idProduct, nombre, inventario, categoria_id) VALUES (3, 'Aspiradora', 7, 2);
INSERT OR IGNORE INTO products (idProduct, nombre, inventario, categoria_id) VALUES (4, 'Cafetera', 3, 2);
INSERT OR IGNORE INTO products (idProduct, nombre, inventario, categoria_id) VALUES (5, 'Pelota de fútbol', 20, 3);
INSERT OR IGNORE INTO products (idProduct, nombre, inventario, categoria_id) VALUES (6, 'Raqueta', 15, 3);


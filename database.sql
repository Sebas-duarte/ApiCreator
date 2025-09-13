
CREATE TABLE IF NOT EXISTS categories (
    idCategory INTEGER PRIMARY KEY AUTOINCREMENT,
    nombreCategoria TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS products (
    idProduct INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    inventario INTEGER DEFAULT 0,
    categoria_id INTEGER NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES categories(idCategory) ON DELETE CASCADE
);


INSERT INTO categories (nombreCategoria) VALUES ('celu'), ('Ropa'), ('Alimentos');

-- Insertar productos de ejemplo
INSERT INTO products (nombre, inventario, categoria_id) VALUES 
('Televisor', 10, 1),
('Camisa', 25, 2),
('Pan integral', 50, 3);
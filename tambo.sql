CREATE TABLE IF NOT EXISTS roles(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_rol VARCHAR(200) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dni VARCHAR(8) NOT NULL UNIQUE,
    id_rol INTEGER,
    email TEXT,
    password TEXT,
    FOREIGN KEY (id_rol) REFERENCES roles(id)
);

CREATE TABLE IF NOT EXISTS categorias(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_categoria TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS subcategorias(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_subcategoria TEXT NOT NULL UNIQUE,
    id_categoria INTEGER,
    FOREIGN KEY (id_categoria) REFERENCES categorias (id)
);

CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_producto TEXT NOT NULL UNIQUE,
    id_categoria INTEGER,
    id_subcategoria INTEGER,
    precio REAL,
    stock INTEGER,
    descripcion TEXT,
    ruta_imagen TEXT,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id),
    FOREIGN KEY (id_subcategoria) REFERENCES subcategorias(id)
);

INSERT OR IGNORE INTO roles(nombre_rol) VALUES
('Administrador'),
('Cajero');

INSERT OR IGNORE INTO categorias (nombre_categoria) VALUES
('Cigarros y Vapes'),
('Cervezas'),
('RTDs'),
('Licores'),
('Comidas'),
('Bebidas'),
('Antojos'),
('Helados'),
('Despensa'),
('Promociones');

INSERT OR IGNORE INTO subcategorias (nombre_subcategoria, id_categoria) VALUES
('Cigarros', 1),
('Vapes', 1),
('Packs', 4),
('Whisky', 4),
('Ron', 4),
('Pisco', 4),
('Vodka', 4),
('Más Licores', 4),
('Hielo', 4),
('Empanadas', 5),
('Sandwich/Hamburguesas', 5),
('Rolls SOS', 5),
('Pizza', 5),
('Postre', 5);

INSERT OR IGNORE INTO productos (nombre_producto, id_categoria, id_subcategoria, precio, stock, descripcion, ruta_imagen) VALUES
('Cigarro Lucky Strike Big Chill Xl X 10 Und', 1, 1, 10.30, NULL, NULL, NULL),
('Cigarro Lucky Strike Blue X 10 Und', 1, 1, 8.60, NULL, NULL, NULL),
('Cigarro Lucky Strike Blue X 20 Und', 1, 1, 16.50, NULL, NULL, NULL);
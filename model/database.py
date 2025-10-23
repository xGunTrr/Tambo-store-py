import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("tambo-store-database.db") # Se busca el archivo, en caso no exista se crea uno 
        self.cursor = self.conn.cursor()

    def create_tables(self):
        query = """
            CREATE TABLE IF NOT EXISTS productos (
                id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
                producto TEXT,
                precio REAL,
                cantidad INTEGER NOT NULL,
                fecha_registro DATE DEFAULT CURRENT_DATE
            );

            CREATE TABLE IF NOT EXISTS usuarios (
                id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL UNIQUE,
                password TEXT
            );

            CREATE TABLE IF NOT EXISTS ventas (
                id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
                id_producto INTEGER NOT NULL,
                fecha_registro DATE DEFAULT CURRENT_DATE,
                total REAL,
                FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
            );
        """
        self.cursor.executescript(query)
        self.conn.commit()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetchone(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def fetchall(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()        
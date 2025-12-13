from model.database import Database
from model.arbol import ArbolProductos

class Producto:
    def __init__(self, id=None, nombre_producto=None, id_categoria=None, id_subcategoria=None, precio=None, stock=None, descripcion=None, ruta_imagen=None):
        self.id = id
        self.nombre_producto = nombre_producto
        self.id_categoria = id_categoria
        self.id_subcategoria = id_subcategoria
        self.precio = precio
        self.stock = stock
        self.descripcion = descripcion
        self.ruta_imagen = ruta_imagen
    
    @staticmethod
    def agregar_producto(nombre_producto, id_categoria, id_subcategoria, precio, stock=0, descripcion="", ruta_imagen=""):
        db = Database()
        # Buscar el siguiente ID disponible
        db.cur.execute("SELECT MAX(id) FROM productos")
        max_id = db.cur.fetchone()[0]
        next_id = (max_id + 1) if max_id else 1
        
        query = """
            INSERT INTO productos (id, nombre_producto, id_categoria, id_subcategoria, precio, stock, descripcion, ruta_imagen)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """
        db.cur.execute(query, (next_id, nombre_producto, id_categoria, id_subcategoria, precio, stock, descripcion, ruta_imagen))
        db.conn.commit()

    @staticmethod
    def eliminar_producto(id_producto):
        db = Database()
        query = "DELETE FROM productos WHERE id = ?"
        db.cur.execute(query, (id_producto,))
        db.conn.commit()
        # Recompactar la base de datos y reajustar la secuencia de IDs
        db.cur.execute("VACUUM")
        db.conn.commit()

    @staticmethod
    def actualizar_producto(id_producto, nombre_producto, id_categoria, id_subcategoria, precio, stock):
        db = Database()
        query = """
            UPDATE productos 
            SET nombre_producto = ?, id_categoria = ?, id_subcategoria = ?, precio = ?, stock = ?
            WHERE id = ?;
        """
        db.cur.execute(query, (nombre_producto, id_categoria, id_subcategoria, precio, stock, id_producto))
        db.conn.commit()

    @staticmethod
    def listar_productos():
        db = Database()
        query = """SELECT 
                productos.id, 
                productos.nombre_producto, 
                categorias.nombre_categoria, 
                subcategorias.nombre_subcategoria, 
                productos.precio,
                productos.stock, 
                productos.descripcion, 
                productos.ruta_imagen 
            FROM productos
            INNER JOIN categorias ON productos.id_categoria = categorias.id
            INNER JOIN subcategorias ON productos.id_subcategoria = subcategorias.id;
        """
        filas = db.cur.execute(query).fetchall()
        productos = []
        for f in filas:
            productos.append(
                Producto(
                    id=f[0],
                    nombre_producto=f[1],
                    id_categoria=f[2],
                    id_subcategoria=f[3],
                    precio=f[4],
                    stock=f[5],
                    descripcion=f[6],
                    ruta_imagen=f[7]
                )
            )
        return productos

    @staticmethod
    def cargar_arbol():
        productos = Producto.listar_productos()
        arbol = ArbolProductos()
        for p in productos:
            arbol.insertar(p)
        return arbol

    @staticmethod
    def buscar_productos(nombre):
        arbol = Producto.cargar_arbol()
        return arbol.buscar(nombre) 
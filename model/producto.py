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
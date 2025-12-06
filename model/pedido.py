from model.database import Database

class Pedido:
    def __init__(self, id=None, producto=None, stock=None, comprar_como=None):
        self.id = id
        self.producto = producto
        self.stock = stock
        self.comprar_como = comprar_como

    @staticmethod
    def listar_pedidos():
        db = Database()
        query = """SELECT 
                productos.id, 
                productos.nombre_producto,
                productos.stock 
            FROM productos
        """
        filas = db.cur.execute(query).fetchall()
        pedidos = []
        for f in filas:
            pedidos.append(
                Pedido(
                    id=f[0],
                    producto=f[1],
                    stock=f[2],
                )
            )
        return pedidos


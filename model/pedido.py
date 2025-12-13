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
    
    def aumentar_stock(self, cantidad):
        db = Database()
        stock_actual = self.stock if self.stock is not None else 0
        nuevo_stock = stock_actual + cantidad
        query = "UPDATE productos SET stock = ? WHERE id = ?"
        db.cur.execute(query, (nuevo_stock, self.id))
        db.conn.commit()
        db.conn.close()
        self.stock = nuevo_stock

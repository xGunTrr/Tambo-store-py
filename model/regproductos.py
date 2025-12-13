from model.database import Database
from datetime import datetime, timedelta

class RegistroProducto:
    def __init__(self, id=None, producto=None, stock=None, fecha_registro=None):
        self.id = id
        self.producto = producto
        self.stock = stock
        self.fecha_registro = fecha_registro

    @staticmethod
    def registrar(producto, stock, fecha_registro, fecha_vencimiento=None):
        db = Database()
        if fecha_vencimiento is None:
            fecha_vencimiento = (datetime.now() + timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")

        query = """
            INSERT INTO registro_productos (producto, stock, fecha_registro, fecha_vencimiento)
            VALUES (?, ?, ?, ?)
        """
        db.cur.execute(query, (producto, stock, fecha_registro, fecha_vencimiento))
        db.conn.commit()
        db.conn.close()

        db.conn.close()
    
    @staticmethod
    def listar_registros():
        db = Database()
        query = "SELECT id, producto, stock, fecha_registro FROM registro_productos"
        filas = db.cur.execute(query).fetchall()
        registros = []
        for f in filas:
            registros.append(
                RegistroProducto(
                    id=f[0],
                    producto=f[1],
                    stock=f[2],
                    fecha_registro=f[3]
                )
            )
        return registros
    @staticmethod
    def revisar_vencimientos():
        db = Database()
        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        vencidos = db.cur.execute("""
            SELECT id, producto, stock, fecha_vencimiento
            FROM registro_productos
            WHERE fecha_vencimiento <= ?
        """, (ahora,)).fetchall()

        for v in vencidos:
            # Guardar en registro_vencimientos
            db.cur.execute("""
                INSERT INTO registro_vencimientos (producto, stock, fecha_vencimiento)
                VALUES (?, ?, ?)
            """, (v[1], v[2], v[3]))

            # ✅ Disminuir stock en productos
            db.cur.execute("""
                UPDATE productos
                SET stock = CASE 
                    WHEN stock - ? < 0 THEN 0
                    ELSE stock - ?
                END
                WHERE nombre_producto = ?
            """, (v[2], v[2], v[1]))

            # Eliminar de registro_productos
            db.cur.execute("DELETE FROM registro_productos WHERE id = ?", (v[0],))

        db.conn.commit()
        db.conn.close()


    @staticmethod
    def listar_vencimientos():
        db = Database()
        query = "SELECT id, producto, stock, fecha_vencimiento FROM registro_vencimientos"
        filas = db.cur.execute(query).fetchall()
        return [RegistroProducto(id=f[0], producto=f[1], stock=f[2], fecha_registro=f[3]) for f in filas]




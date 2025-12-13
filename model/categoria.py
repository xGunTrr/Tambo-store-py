from model.database import Database

class Categoria:
    def __init__(self, id=None, nombre_categoria=None):
        self.id = id
        self.nombre_categoria = nombre_categoria

    @staticmethod
    def listar_categorias():
        db = Database()
        query = "SELECT id, nombre_categoria FROM categorias;"
        filas = db.cur.execute(query).fetchall()
        categorias = []
        for f in filas:
            categorias.append(
                Categoria(
                    id=f[0],
                    nombre_categoria=f[1]
                )
            )
        return categorias

    @staticmethod
    def obtener_todas():
        db = Database()
        query = "SELECT id, nombre_categoria FROM categorias;"
        filas = db.cur.execute(query).fetchall()
        return [Categoria(id=f[0], nombre_categoria=f[1]) for f in filas]

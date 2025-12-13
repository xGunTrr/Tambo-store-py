from model.database import Database

class Subcategoria:
    def __init__(self, id=None, nombre_subcategoria=None, id_categoria=None):
        self.id = id
        self.nombre_subcategoria = nombre_subcategoria
        self.id_categoria = id_categoria

    @staticmethod
    def listar_subcategorias():
        db = Database()
        query = """SELECT 
                subcategorias.id,
                subcategorias.nombre_subcategoria,
                categorias.nombre_categoria
                FROM subcategorias
                INNER JOIN categorias ON subcategorias.id_categoria = categorias.id;
            """
        filas = db.cur.execute(query).fetchall()
        subcategorias = []
        for f in filas:
            subcategorias.append(
                Subcategoria(
                    id=f[0],
                    nombre_subcategoria=f[1],
                    id_categoria=f[2]
                )
            )
        return subcategorias
    @staticmethod
    def obtener_todas():
        conn = Database()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre FROM categorias")
        rows = cursor.fetchall()
        return [Subcategoria(id=row[0], nombre=row[1]) for row in rows]


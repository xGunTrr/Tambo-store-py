from model.database import Database

class Rol:
    def __init__(self, id=None, nombre_rol=None):
        self.db = Database()
        self.id = id
        self.nombre_rol = nombre_rol

    @staticmethod
    def listar_roles():
        db = Database()
        query = "SELECT id, nombre_rol FROM roles;"
        filas = db.cur.execute(query).fetchall()
        roles = []
        for f in filas:
            roles.append(
                Rol(
                    id=f[0],
                    nombre_rol=f[1]
                )
            )
        return roles
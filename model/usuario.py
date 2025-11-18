from werkzeug.security import generate_password_hash, check_password_hash
from .database import Database
from flask_login import UserMixin

class Usuario(UserMixin):
    def __init__(self, id=None, dni=None, id_rol=None, email=None, password=None):
        self.id = id
        self.dni = dni
        self.id_rol = id_rol
        self.email = email
        self.password = password

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    @staticmethod
    def listar_usuarios():
        db = Database()
        query = """SELECT 
                usuarios.id, 
                usuarios.dni, 
                roles.nombre_rol, 
                usuarios.email
            FROM usuarios
            INNER JOIN roles ON usuarios.id_rol = roles.id"""
        filas = db.cur.execute(query).fetchall()
        usuarios = []
        for f in filas:
            usuarios.append(
                Usuario(
                    id=f[0],
                    dni=f[1],
                    id_rol=f[2],
                    email=f[3]
                )
            )
        return usuarios

    @staticmethod
    def create_user(p_dni, p_id_rol, p_email, p_password):
        db = Database()
        query = "INSERT INTO usuarios (dni, id_rol, email, password) VALUES (?, ?, ?, ?);"
        db.cur.execute(query, (p_dni, p_id_rol, p_email, generate_password_hash(p_password)))
        db.conn.commit()

    @staticmethod
    def get_user_by_dni(dni):
        db = Database()
        query = "SELECT id, dni, id_rol, email, password FROM usuarios WHERE dni = ?;"
        fila = db.cur.execute(query, (dni,)).fetchone()

        if fila:
            return Usuario(
                id=fila[0],
                dni=fila[1],
                id_rol=fila[2],
                email=fila[3],
                password=fila[4]
            )
        
    @staticmethod
    def get_user_by_id(user_id):
        # user_id puede llegar como string desde Flask-Login, convertir a int si es posible
        try:
            user_id = int(user_id)
        except (TypeError, ValueError):
            return None

        db = Database()
        row = db.cur.execute(
            "SELECT id, dni, id_rol, email, password FROM usuarios WHERE id = ?;",
            (user_id,)
        ).fetchone()

        if row:
            return Usuario(
                id=row[0],
                dni=row[1],
                id_rol=row[2],
                email=row[3],
                password=row[4]
            )
        return None        
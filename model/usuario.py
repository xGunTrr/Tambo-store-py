from werkzeug.security import generate_password_hash, check_password_hash
from .database import Database
from flask_login import UserMixin

# ==========================
# Tablas hash en memoria
# ==========================
sesiones_activas = {}       # 1. token → id_usuario
intentos_fallidos = {}      # 2. dni → contador de intentos
usuarios_por_dni = {}       # 4. cache de usuarios por dni
usuarios_por_email = {}     # 4. cache de usuarios por email

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
    def get_user_by_id(user_id):
        """Obtener usuario por ID (para Flask-Login)"""
        try:
            user_id = int(user_id)
        except (TypeError, ValueError):
            return None

        # Primero buscar en cache
        for usuario in usuarios_por_dni.values():
            if usuario.id == user_id:
                return usuario

        # Si no está en cache, consultar la BD
        db = Database()
        row = db.cur.execute(
            "SELECT id, dni, id_rol, email, password FROM usuarios WHERE id = ?;",
            (user_id,)
        ).fetchone()

        if row:
            usuario = Usuario(
                id=row[0],
                dni=row[1],
                id_rol=row[2],
                email=row[3],
                password=row[4]
            )
            # Actualizar cache
            usuarios_por_dni[usuario.dni] = usuario
            usuarios_por_email[usuario.email] = usuario
            return usuario

        return None

    @staticmethod
    def get_user_by_dni(dni):
        """Obtener usuario por DNI"""
        # Primero buscar en cache
        usuario = usuarios_por_dni.get(dni)
        if usuario:
            return usuario

        # Si no está en cache, consultar la BD
        db = Database()
        row = db.cur.execute(
            "SELECT id, dni, id_rol, email, password FROM usuarios WHERE dni = ?;",
            (dni,)
        ).fetchone()

        if row:
            usuario = Usuario(
                id=row[0],
                dni=row[1],
                id_rol=row[2],
                email=row[3],
                password=row[4]
            )
            # Actualizar cache
            usuarios_por_dni[usuario.dni] = usuario
            usuarios_por_email[usuario.email] = usuario
            return usuario

        return None

    @staticmethod
    def listar_usuarios():
        """Listar todos los usuarios desde la BD y actualizar cache"""
        db = Database()
        query = """SELECT 
                usuarios.id, 
                usuarios.dni, 
                roles.nombre_rol, 
                usuarios.email,
                usuarios.password
            FROM usuarios
            INNER JOIN roles ON usuarios.id_rol = roles.id"""
        filas = db.cur.execute(query).fetchall()
        usuarios = []
        for f in filas:
            usuario = Usuario(
                id=f[0],
                dni=f[1],
                id_rol=f[2],   # aquí puedes usar nombre_rol si prefieres
                email=f[3],
                password=f[4]
            )
            usuarios.append(usuario)
            # actualizar cache
            usuarios_por_dni[usuario.dni] = usuario
            usuarios_por_email[usuario.email] = usuario
        return usuarios


    # ==========================
    # Métodos de seguridad
    # ==========================

    @staticmethod
    def registrar_sesion(token, usuario_id):
        """Guardar sesión activa en tabla hash"""
        sesiones_activas[token] = usuario_id

    @staticmethod
    def verificar_sesion(token):
        """Verificar si un token está activo"""
        return sesiones_activas.get(token)

    @staticmethod
    def registrar_intento(dni):
        """Registrar intento fallido de login"""
        intentos_fallidos[dni] = intentos_fallidos.get(dni, 0) + 1
        return intentos_fallidos[dni]

    @staticmethod
    def resetear_intentos(dni):
        """Resetear intentos al iniciar sesión correctamente"""
        if dni in intentos_fallidos:
            intentos_fallidos[dni] = 0

    @staticmethod
    def cargar_cache_usuarios():
        """Cargar usuarios en tablas hash para búsquedas rápidas"""
        db = Database()
        filas = db.cur.execute("SELECT id, dni, id_rol, email, password FROM usuarios").fetchall()
        for f in filas:
            usuario = Usuario(id=f[0], dni=f[1], id_rol=f[2], email=f[3], password=f[4])
            usuarios_por_dni[usuario.dni] = usuario
            usuarios_por_email[usuario.email] = usuario

    @staticmethod
    def buscar_por_dni(dni):
        """Buscar usuario en cache por DNI"""
        return usuarios_por_dni.get(dni)

    @staticmethod
    def buscar_por_email(email):
        """Buscar usuario en cache por email"""
        return usuarios_por_email.get(email)

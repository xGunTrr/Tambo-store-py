from model.classes import ProductModel
from model.classes import SellModel
from model.classes import UserModel
from model.database import Database

class UserDAO:
    def __init__(self, database):
        self.db = database

    def create_user(self, user):
        query = "INSERT INTO usuarios (usuario, password) VALUES (?, ?);"
        params = (user.get_user(), user.get_password())
        self.db.execute(query, params)

    def get_user_by_username(self, username):
        query = "SELECT id_usuario, usuario, password FROM usuarios WHERE usuario = ?;"
        row = self.db.fetchone(query, (username,))
        if row:
            return UserModel(row[0], row[1], row[2])
        return None

    def verify_user(self, username, password):
        query = "SELECT id_usuario, usuario, password FROM usuarios WHERE usuario=? AND password=?;"
        row = self.db.fetchone(query, (username, password))
        if row:
            return UserModel(row[0], row[1], row[2])
        return None

    def get_all_users(self):
        query = "SELECT id_usuario, usuario, password FROM usuarios;"
        rows = self.db.fetchall(query)
        return [UserModel(r[0], r[1], r[2]) for r in rows]
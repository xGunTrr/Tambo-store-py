import tkinter as tk

from model.database import Database
from controller.form_controller import LoginController
from model.classes_dao import UserDAO
from controller.main_controller import MainController

if __name__ == "__main__":
    database = Database()
    user_dao = UserDAO(database)

    root = MainController(user_dao)
    root.main_view.withdraw()

    LoginController(root.main_view, user_dao, root)
    root.main_view.mainloop()
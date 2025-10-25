import tkinter as tk

from model.database import Database
from controller.form_controller import LoginController
from model.classes_dao import UserDAO

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    database = Database()
    user_dao = UserDAO(database)
    LoginController(root, user_dao)

    root.mainloop()
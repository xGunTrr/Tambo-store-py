from view.form_view import LoginForm
from view.form_view import SigninForm
from controller.main_controller import MainController
from model.classes import UserModel
from tkinter import messagebox

class SigninController:
    def __init__(self, root, user_dao):
        self.root = root
        self.user_dao = user_dao
        self.signin_form = SigninForm(root)

        self.signin_form.button_wid01.config(command=self.open_login)
        self.signin_form.button_wid02.config(command=self.create_user)

    def open_login(self):
        self.signin_form.destroy()
        LoginController(self.root, self.user_dao)
        
    def create_user(self):
        p_username, p_password = self.signin_form.get_user_data()

        if p_username == self.signin_form.user_entry.placeholder:
            messagebox.showwarning(title="Advertencia", message="La casilla de usuario no debe estar vacía")
            return

        if p_password == self.signin_form.password_entry.placeholder:
            messagebox.showwarning(title="Advertencia", message="La casilla de contraseña no debe estar vacía")
            return

        if len(p_username) < 4:
            messagebox.showwarning(title="Advertencia", message="El usuario debe tener al menos 5 caracteres")
            return

        if len(p_password) < 4:
            messagebox.showwarning(title="Advertencia", message="La contraseña debe tener al menos 6 caracteres")
            return

        self.user_dao.create_user(UserModel(id_user=0, user=p_username, password=p_password))
        messagebox.showinfo(title="Éxito", message="Usuario creado correctamente")

class LoginController:
    def __init__(self, root, user_dao, main_controller):
        self.root = root
        self.user_dao = user_dao
        self.main_controller = main_controller
        self.login_form = LoginForm(root)

        self.login_form.button_wid01.config(command=self.open_signin)
        self.login_form.button_wid02.config(command=self.login_user)
    
    def open_signin(self):
        self.login_form.destroy()
        SigninController(self.root, self.user_dao)
    
    def login_user(self):
        p_username, p_password = self.login_form.get_user_data()

        user = self.user_dao.verify_user(p_username, p_password)

        if not user:
            messagebox.showwarning(title="Advertencia", message="Usuario o contraseña incorrectas")
            return

        user_info = {
            "id": user.get_id(),
            "usuario": user.get_user()
        }

        self.open_main_view()
        self.main_controller.show_user_info(user_info)

    def open_main_view(self):
        self.login_form.destroy()
        self.root.wm_deiconify()


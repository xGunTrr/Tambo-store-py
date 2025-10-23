from model.classes import UserModel

class SigninController:
    def __init__(self, signin_form, user_dao):
        self.signin_form = signin_form
        self.user_dao = user_dao
        self.signin_form.button_wid.config(command=self.create_user)

    def create_user(self):
        p_username = self.signin_form.user_entry.get()
        p_password = self.signin_form.password_entry.get()

        self.user_dao.create_user(UserModel(id_user=0, user=p_username, password=p_password))
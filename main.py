from view.form_view import FormView
from view.form_view import LoginForm
from view.form_view import SigninForm
from model.classes import UserModel
from model.classes_dao import UserDAO
from model.database import Database
from controller.form_controller import SigninController

db = Database()
db.create_tables()
user_dao = UserDAO(db)

sign_form = SigninForm()
sign_controller = SigninController(sign_form, user_dao)

sign_form.mainloop()
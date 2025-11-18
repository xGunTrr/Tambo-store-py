from flask import render_template, Blueprint, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_login import current_user
from flask_login import login_user, logout_user
from wtforms import StringField, SubmitField, PasswordField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, Length
from urllib.parse import urlparse
from model.usuario import Usuario
from model.rol import Rol

class SignupForm(FlaskForm):
    dni = StringField('Dni', validators=[DataRequired(), Length(max=10)])
    rol = SelectField('Rol', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=20)])
    submit = SubmitField('Registrar')

class SigninForm(FlaskForm):
    dni = StringField('Dni', validators=[DataRequired(message="Este campo es obligatorio.")])
    password = PasswordField('Password', validators=[DataRequired(message="Este campo es obligatorio.")])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Login')

form_bp = Blueprint('form_bp', __name__)

@form_bp.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignupForm()

    # Se listan los roles y se agregan como opciones dentro del rol -> SelectField de la clase SignupForm
    roles = Rol.listar_roles()
    form.rol.choices = [(r.id, r.nombre_rol) for r in roles]

    # Se validan los datos del formularios
    if form.validate_on_submit():
        d_dni = form.dni.data
        d_idrol = form.rol.data
        d_email = form.email.data
        d_password = form.password.data

        Usuario.create_user(d_dni, d_idrol, d_email, d_password)

        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('form_bp.signin'))
    return render_template('signup_form.html', form=form)

@form_bp.route('/signin', methods=["GET", "POST"])
def signin():
    form = SigninForm()

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if form.validate_on_submit():
        d_dni = form.dni.data
        d_password = form.password.data

        user_model = Usuario.get_user_by_dni(d_dni)

        if user_model is not None:
            if user_model.check_password(d_password):
                login_user(user_model, remember=form.remember_me.data)
                next = request.args.get('next')

                if not next or urlparse(next).netloc != '':
                    next = url_for('index')
                return redirect(url_for('index'))
    return render_template('signin_form.html', form=form)

@form_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('form_bp.signin'))
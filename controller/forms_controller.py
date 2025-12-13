from flask import render_template, Blueprint, request, redirect, url_for , flash
from flask_login import current_user, login_user, logout_user
from urllib.parse import urlparse
from model.usuario import Usuario , intentos_fallidos
from model.rol import Rol

form_bp = Blueprint('form_bp', __name__)

@form_bp.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Extraer datos directamente de los inputs HTML
        d_dni = request.form.get("dni")
        d_idrol = request.form.get("rol")
        d_email = request.form.get("email")
        d_password = request.form.get("password")

        # Guardar en la BD
        Usuario.create_user(d_dni, d_idrol, d_email, d_password)

        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('form_bp.signin'))

    # Pasar roles a la plantilla para renderizar el <select>
    roles = Rol.listar_roles()
    return render_template("signup_form.html", roles=roles)


@form_bp.route('/signin', methods=["GET", "POST"])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == "POST":
        d_dni = request.form.get("dni")
        d_password = request.form.get("password")
        remember_me = request.form.get("remember_me")

        user_model = Usuario.get_user_by_dni(d_dni)

        if user_model is None:
            flash("Usuario no encontrado")
            print("Intentos actuales:", intentos_fallidos)   # 👈 aquí ves el estado
            return redirect(url_for("form_bp.signin"))

        # Verificar si está bloqueado
        if intentos_fallidos.get(d_dni, 0) >= 5:
            flash("Usuario bloqueado por exceso de intentos")
            print("Intentos actuales (bloqueado):", intentos_fallidos)  # 👈 aquí ves el estado
            return redirect(url_for("form_bp.signin"))

        # Verificar contraseña
        if user_model.check_password(d_password):
            Usuario.resetear_intentos(d_dni)
            print("Intentos actuales (reset):", intentos_fallidos)  # 👈 aquí ves el reset
            login_user(user_model, remember=bool(remember_me))
            next = request.args.get('next')
            if not next or urlparse(next).netloc != '':
                next = url_for('index')
            return redirect(next)
        else:
            Usuario.registrar_intento(d_dni)
            print("Intentos actuales (fallo):", intentos_fallidos)  # 👈 aquí ves el contador subir
            flash("Contraseña incorrecta")
            return redirect(url_for("form_bp.signin"))

    return render_template("signin_form.html")


@form_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('form_bp.signin'))

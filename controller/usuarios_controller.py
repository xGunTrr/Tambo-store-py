from flask import render_template, Blueprint, request, redirect, url_for
from flask_login import login_required
from model.usuario import Usuario
from model.rol import Rol

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/usuarios')
@login_required
def listar_usuarios():
    usuarios = Usuario.listar_usuarios()
    roles = Rol.listar_roles()
    return render_template('index-usuarios.html', usuarios=usuarios, roles=roles)
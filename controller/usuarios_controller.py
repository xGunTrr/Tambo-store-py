from flask import render_template, Blueprint, request, redirect, url_for
from flask_login import login_required
from model.usuario import Usuario

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/usuarios')
@login_required
def listar_usuarios():
    usuarios = Usuario.listar_usuarios()
    return render_template('index-usuarios.html', usuarios=usuarios)
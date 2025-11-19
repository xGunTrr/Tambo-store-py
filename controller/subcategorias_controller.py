from flask import render_template, Blueprint
from flask_login import login_required
from model.subcategoria import Subcategoria

subcategoria_bp = Blueprint('subcategoria_bp', __name__)

@subcategoria_bp.route('/subcategorias')
@login_required
def listar_productos():
    subcategorias = Subcategoria.listar_subcategorias()
    return render_template('index-subcategorias.html', subcategorias=subcategorias)
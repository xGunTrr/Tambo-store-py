from flask import render_template, Blueprint
from flask_login import login_required
from model.categoria import Categoria

categoria_bp = Blueprint('categoria_bp', __name__)

@categoria_bp.route('/categorias')
@login_required
def listar_productos():
    categorias = Categoria.listar_categorias()
    return render_template('index-categorias.html', categorias=categorias)
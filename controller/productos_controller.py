from flask import render_template, Blueprint
from flask_login import login_required
from model.producto import Producto
from model.categoria import Categoria
from model.subcategoria import Subcategoria

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/productos')
@login_required
def listar_productos():
    productos = Producto.listar_productos()
    categorias = Categoria.listar_categorias()
    subcategorias = Subcategoria.listar_subcategorias()
    return render_template('index-productos.html', productos=productos, categorias=categorias, subcategorias=subcategorias)
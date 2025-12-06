from flask import render_template, Blueprint
from flask_login import login_required
from model.pedido import Pedido

pedidos_bp = Blueprint('pedidos_bp', __name__)

@pedidos_bp.route('/pedidos')
@login_required
def listar_pedidos():
    pedidos = Pedido.listar_pedidos()
    return render_template('index-pedidos.html', pedidos=pedidos)

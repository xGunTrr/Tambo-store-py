from flask import render_template, Blueprint, request, redirect, url_for
from flask_login import login_required
from model.pedido import Pedido

pedidos_bp = Blueprint('pedidos_bp', __name__)

@pedidos_bp.route('/pedidos')
@login_required
def listar_pedidos():
    pedidos = Pedido.listar_pedidos()
    return render_template('index-pedidos.html', pedidos=pedidos)

# 👉 Nueva ruta para procesar el pedido
@pedidos_bp.route('/pedir_producto', methods=["POST"])
@login_required
def pedir_producto():
    id_producto = int(request.form.get("id_producto"))
    cantidad = int(request.form.get("cantidad"))

    # Buscar el pedido (producto) por ID
    pedidos = Pedido.listar_pedidos()
    pedido = next((p for p in pedidos if p.id == id_producto), None)

    if pedido:
        pedido.aumentar_stock(cantidad)

    return redirect(url_for('pedidos_bp.listar_pedidos'))

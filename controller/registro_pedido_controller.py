from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from datetime import datetime
from model.regproductos import RegistroProducto

# Definir el blueprint
registro_pedidos_bp = Blueprint('registro_pedidos_bp', __name__, url_prefix="/registro-pedidos")

# Ruta para listar los registros
@registro_pedidos_bp.route('/')
@login_required
def listar_registros():
    RegistroProducto.revisar_vencimientos()
    registros = RegistroProducto.listar_registros()
    vencidos = RegistroProducto.listar_vencimientos()
    return render_template("index-registro-productos.html", 
        registro_productos=registros,
        vencimientos=vencidos
    )
# Ruta para registrar un producto
@registro_pedidos_bp.route('/registrar', methods=["POST"])
@login_required
def registrar_producto():
    producto = request.form.get("producto")
    stock = request.form.get("stock")
    id_producto = request.form.get("id")
    fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fecha_vencimiento = request.form.get("fecha_vencimiento")

    # Validar stock
    if not stock:
        stock = 0
    else:
        stock = int(stock)

    # Registrar pedido en registro_productos
    RegistroProducto.registrar(producto, stock, fecha_registro,fecha_vencimiento)

    # ✅ Actualizar stock en productos
    from model.pedido import Pedido
    pedidos = Pedido.listar_pedidos()
    pedido = next((p for p in pedidos if str(p.id) == str(id_producto)), None)

    if pedido:
        pedido.aumentar_stock(stock)

    flash("Producto registrado y stock actualizado", "success")
    return redirect(url_for('registro_pedidos_bp.listar_registros'))



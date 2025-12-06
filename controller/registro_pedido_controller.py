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
    fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    RegistroProducto.registrar(producto, stock, fecha_registro)
    flash("Producto registrado correctamente", "success")
    return redirect(url_for('registro_pedidos_bp.listar_registros'))
@registro_pedidos_bp.route('/revisar-vencimientos')
@login_required
def revisar_vencimientos():
    RegistroProducto.revisar_vencimientos()
    flash("Vencimientos actualizados", "info")
    return redirect(url_for('registro_pedidos_bp.listar_registros'))

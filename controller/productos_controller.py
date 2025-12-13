from flask import render_template, Blueprint, request, redirect, url_for ,flash
from flask_login import login_required
from model.producto import Producto
from model.categoria import Categoria
from model.subcategoria import Subcategoria

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/productos', methods=["GET", "POST"])
@login_required
def listar_productos():
    if request.method == "POST":
        query = request.form.get("query")
        productos = Producto.buscar_productos(query)
    else:
        productos = Producto.listar_productos()

    categorias = Categoria.listar_categorias()
    subcategorias = Subcategoria.listar_subcategorias()

    return render_template(
        'index-productos.html',
        productos=productos,
        categorias=categorias,
        subcategorias=subcategorias
    )

# Nueva ruta para agregar producto desde el modal
@product_bp.route('/agregar_producto', methods=["POST"])
@login_required
def agregar_producto():
    print("👉 INTENTO DE INSERT PRODUCTO")   # log antes de insertar
    nombre = request.form.get("nombre_producto")
    id_categoria = request.form.get("id_categoria")
    id_subcategoria = request.form.get("id_subcategoria")
    precio = request.form.get("precio")
    stock = request.form.get("stock", 0)

    Producto.agregar_producto(
        nombre_producto=nombre,
        id_categoria=id_categoria,
        id_subcategoria=id_subcategoria,
        precio=precio,
        stock=stock,
    )
    print("✅ PRODUCTO INSERTADO")   # log después de insertar
    return redirect(url_for('product_bp.listar_productos'))

@product_bp.route('/eliminar_producto/<int:id_producto>', methods=["POST"])
@login_required
def eliminar_producto(id_producto):
    Producto.eliminar_producto(id_producto)
    flash("Producto eliminado correctamente")
    return redirect(url_for('product_bp.listar_productos'))

@product_bp.route('/editar_producto', methods=["POST"])
@login_required
def editar_producto():
    print("👉 INTENTO DE UPDATE PRODUCTO")
    id_producto = request.form.get("id_producto")
    nombre = request.form.get("nombre_producto")
    id_categoria = request.form.get("id_categoria")
    id_subcategoria = request.form.get("id_subcategoria")
    precio = request.form.get("precio")
    stock = request.form.get("stock")

    Producto.actualizar_producto(
        id_producto=id_producto,
        nombre_producto=nombre,
        id_categoria=id_categoria,
        id_subcategoria=id_subcategoria,
        precio=precio,
        stock=stock,
    )
    print("✅ PRODUCTO ACTUALIZADO")
    flash("Producto actualizado correctamente")
    return redirect(url_for('product_bp.listar_productos'))

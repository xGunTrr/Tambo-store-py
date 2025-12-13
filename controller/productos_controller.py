from flask import render_template, Blueprint, request, redirect, url_for
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
    nombre = request.form.get("nombre_producto")
    id_categoria = request.form.get("categoria")
    id_subcategoria = request.form.get("subcategoria")
    precio = request.form.get("precio")
    stock = request.form.get("stock", 0)
    descripcion = request.form.get("descripcion", "")
    ruta_imagen = request.form.get("ruta_imagen", "")

    Producto.agregar_producto(
        nombre_producto=nombre,
        id_categoria=id_categoria,
        id_subcategoria=id_subcategoria,
        precio=precio,
        stock=stock,
        descripcion=descripcion,
        ruta_imagen=ruta_imagen
    )

    return redirect(url_for('product_bp.listar_productos'))


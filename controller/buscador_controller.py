from flask import Blueprint, render_template, request
from model.buscador import cargar_arbol

buscador_bp = Blueprint('buscador', __name__)  # ← aquí va __name__
arbol = cargar_arbol()  # Cargamos el árbol al iniciar

@buscador_bp.route("/", methods=["GET", "POST"])
def index():
    productos = []
    if request.method == "POST":
        query = request.form.get("query")
        productos = arbol.buscar(query)
    else:
        productos = arbol.buscar("")  # Buscar vacío devuelve todos
    return render_template("index.html", productos=productos)

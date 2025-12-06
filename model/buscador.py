from model.database import Database

class Nodo:
    def __init__(self, producto):
        # producto es una tupla: (id, nombre_producto, precio, stock)
        self.producto = producto
        self.izq = None
        self.der = None

class ArbolProductos:
    def __init__(self):
        self.raiz = None

    def insertar(self, producto):
        if self.raiz is None:
            self.raiz = Nodo(producto)
        else:
            self._insertar(self.raiz, producto)

    def _insertar(self, nodo, producto):
        # Compara por nombre del producto (posición 1 de la tupla)
        if producto[1].lower() < nodo.producto[1].lower():
            if nodo.izq is None:
                nodo.izq = Nodo(producto)
            else:
                self._insertar(nodo.izq, producto)
        else:
            if nodo.der is None:
                nodo.der = Nodo(producto)
            else:
                self._insertar(nodo.der, producto)

    def buscar(self, nombre):
        return self._buscar(self.raiz, nombre.lower())

    def _buscar(self, nodo, nombre):
        if nodo is None:
            return []
        resultados = []
        # Si el texto buscado está dentro del nombre del producto
        if nombre in nodo.producto[1].lower():
            resultados.append({
                "id": nodo.producto[0],
                "nombre": nodo.producto[1],
                "precio": nodo.producto[2],
                "stock": nodo.producto[3]
            })
        resultados += self._buscar(nodo.izq, nombre)
        resultados += self._buscar(nodo.der, nombre)
        return resultados

    def listar_todos(self):
        """Devuelve todos los productos en orden alfabético por nombre"""
        return self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo is None:
            return []
        return self._inorden(nodo.izq) + [{
            "id": nodo.producto[0],
            "nombre": nodo.producto[1],
            "precio": nodo.producto[2],
            "stock": nodo.producto[3]
        }] + self._inorden(nodo.der)

def cargar_arbol():
    db = Database()  # Usamos tu clase Database
    query = "SELECT id, nombre_producto, precio, stock FROM productos"
    productos = db.cur.execute(query).fetchall()

    arbol = ArbolProductos()
    for p in productos:
        arbol.insertar(p)
    return arbol

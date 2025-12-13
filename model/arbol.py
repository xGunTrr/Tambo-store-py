from model.database import Database

class Nodo:
    def __init__(self, producto):
        # producto es un objeto de la clase Producto
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
        # Comparación usando atributo nombre_producto
        if producto.nombre_producto.lower() < nodo.producto.nombre_producto.lower():
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
        # Comparación usando atributo nombre_producto
        if nombre in nodo.producto.nombre_producto.lower():
            resultados.append(nodo.producto)
        resultados += self._buscar(nodo.izq, nombre)
        resultados += self._buscar(nodo.der, nombre)
        return resultados

    def listar_todos(self):
        """Devuelve todos los productos en orden alfabético por nombre"""
        return self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo is None:
            return []
        return (
            self._inorden(nodo.izq)
            + [{
                "id": nodo.producto.id,
                "nombre": nodo.producto.nombre_producto,
                "precio": nodo.producto.precio,
                "stock": nodo.producto.stock
            }]
            + self._inorden(nodo.der)
        )

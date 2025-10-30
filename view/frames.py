import tkinter as tk

class ActualizarUsuarioFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg="green")
        tk.Label(self, text="Administrar Usuario", bg="green", fg="white").pack(padx=20, pady=20)

class NuevaBoletaFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg="red")
        tk.Label(self, text="Nueva Boleta", bg="red", fg="white").pack(padx=20, pady=20)

class NuevoProductoFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg="blue")
        tk.Label(self, text="Nuevo Producto", bg="blue", fg="white").pack(padx=20, pady=20)
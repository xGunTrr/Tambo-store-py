from view.widgets import NewTopLevel

import tkinter as tk 
from PIL import Image, ImageTk, ImageOps

from config import W_FORM, H_FORM

class FormView(NewTopLevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # --- Propiedades de la pantalla ---
        self.resizable(0, 0) # No se puede reescalar
        self.center_top_level(W_FORM, H_FORM)
        self.protocol("WM_DELETE_WINDOW", self.quit_app)

        # --- Creación de frames para guardar los widgets ---
        frame_left = tk.Frame(self, bg="#9c1b83")
        frame_left.grid(row=0, column=0, sticky="nsew")

        frame_right = tk.Frame(self, bg="white")
        frame_right.grid(row=0, column=1, sticky="nsew")

        # --- configuración de los frames dentro de la pantalla ---
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # --- Imagen de Tambo ---
        self.image = Image.open("images/tambo_flyer.png")
        self.image = self.image.resize((405, 540), Image.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.label_image = tk.Label(frame_left, image=self.image_tk, bg="#9c1b83")
        self.label_image.grid(row=0, column=0)

        # --- configuración de los elementos dentro de frame_left ---
        frame_left.rowconfigure(0, weight=1)
        frame_left.columnconfigure(0, weight=1)

        # --- Heading text para la app ---
        self.heading_text = tk.Label(frame_right, bg="white", font=("Arial", 23, "bold"))
        self.heading_text.grid(row=0, column=0, columnspan=2, pady=20)

        # --- Campo de usuario ---
        self.user_entry = tk.Entry(frame_right, fg="gray", border=0, bg="white", width=50, font=("Arial", 11, "bold"))
        self.user_entry.grid(row=1, column=0, columnspan=2, pady=10, ipadx=10, ipady=5)

        # --- Campo de contraseña ---
        self.password_entry = tk.Entry(frame_right, fg="gray", border=0, bg="white", width=50, font=("Arial", 11, "bold"))
        self.password_entry.grid(row=2, column=0, columnspan=2, pady=10, ipadx=10, ipady=5)

        # --- Mensaje para el usuario + botón de registro ---
        frame_message = tk.Frame(frame_right, bg="white")
        frame_message.grid(row=3, column=0, columnspan=2, padx=30, pady=5, sticky="w")  # alineado a la izquierda

        self.message = tk.Label(frame_message, bg="white", font=("Arial", 11))
        self.message.pack(side="left")

        self.button_wid01 = tk.Button(frame_message, bg="white", fg="#57a1f8", font=("Arial", 11), border=0, cursor="hand2")
        self.button_wid01.pack(side="left", padx=(5, 0))

        # --- Botón ---
        self.button_wid02 = tk.Button(frame_right, bg="#57a1f8", border=0, fg="white", width=20, cursor="hand2")
        self.button_wid02.grid(row=4, column=0, columnspan=2, pady=20)

        # --- configuración de los elementos dentro de frame_right ---
        frame_right.rowconfigure(0, weight=5)
        frame_right.rowconfigure(1, weight=1)
        frame_right.rowconfigure(2, weight=1)
        frame_right.rowconfigure(3, weight=5)
        frame_right.columnconfigure(0, weight=1)

    # --- Métodos genéricos para cualquier Entry ---
    def on_enter(self, e):
        entry = e.widget
        if entry.get() == entry.placeholder:
            entry.delete(0, 'end')
            entry.config(fg="black")
            if entry.placeholder == "Ingresa tu contraseña":
                entry.config(show="*")

    def on_leave(self, e):
        entry = e.widget
        if entry.get() == '':
            entry.insert(0, entry.placeholder)
            entry.config(fg="gray")
            if entry.placeholder == "Ingresa tu contraseña" or entry.placeholder == "Crea una contraseña":
                entry.config(show="")

    def get_user_data(self):
        return self.user_entry.get(), self.password_entry.get()
    
    def quit_app(self):
        self.destroy()
        self.master.quit()

class LoginForm(FormView):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Iniciar Sesión")

        self.heading_text.config(text="Iniciar sesión")

        self.user_entry.insert(0, "Ingresa tu usuario")
        self.user_entry.placeholder = "Ingresa tu usuario"
        self.user_entry.bind("<FocusIn>", self.on_enter)
        self.user_entry.bind("<FocusOut>", self.on_leave)

        self.password_entry.insert(0, "Ingresa tu contraseña")
        self.password_entry.placeholder = "Ingresa tu contraseña"
        self.password_entry.bind("<FocusIn>", self.on_enter)
        self.password_entry.bind("<FocusOut>", self.on_leave)

        self.message.config(text="¿Aún no tienes una cuenta?")
        self.button_wid01.config(text="Registrarse")

        self.button_wid02.config(text="Ingresar")

class SigninForm(FormView):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Crear una cuenta")

        self.heading_text.config(text="Registrarse")

        self.user_entry.insert(0, "Crea un usuario (mínimo 4 dígitos)")
        self.user_entry.placeholder = "Crea un usuario (mínimo 4 dígitos)"
        self.user_entry.bind("<FocusIn>", self.on_enter)
        self.user_entry.bind("<FocusOut>", self.on_leave)

        self.password_entry.insert(0, "Crea una contraseña (mínimo 4 dígitos)")
        self.password_entry.placeholder = "Crea una contraseña (mínimo 4 dígitos)"
        self.password_entry.bind("<FocusIn>", self.on_enter)
        self.password_entry.bind("<FocusOut>", self.on_leave)

        self.message.config(text="¿Tienes una cuenta?")
        self.button_wid01.config(text="Iniciar Sesión")

        self.button_wid02.config(text="Crear usuario")
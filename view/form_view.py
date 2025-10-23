import tkinter as tk 

from config import FORM_SIZE

class FormView(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry(FORM_SIZE)

        frame_left = tk.Frame(self, bg="red")
        frame_left.grid(row=0, column=0, sticky="nsew")

        frame_right = tk.Frame(self, bg="white")
        frame_right.grid(row=0, column=1, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.heading_text = tk.Label(frame_right, bg="white", font=("Arial", 23, "bold"))
        self.heading_text.grid(row=0, column=0, pady=20)

        # --- Campo de usuario ---
        self.user_entry = tk.Entry(frame_right, fg="gray", border=0, bg="white", width=25, font=("Arial", 11, "bold"))
        self.user_entry.grid(row=1, column=0, pady=10, ipadx=10, ipady=5)

        # --- Campo de contraseña ---
        self.password_entry = tk.Entry(frame_right, fg="gray", border=0, bg="white", width=25, font=("Arial", 11, "bold"))
        self.password_entry.grid(row=2, column=0, pady=10, ipadx=10, ipady=5)

        # --- Botón ---
        self.button_wid = tk.Button(frame_right, bg="#57a1f8", border=0, fg="white", width=20)
        self.button_wid.grid(row=3, column=0, pady=20)

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
            if entry.placeholder == "enter your password":
                entry.config(show="*")

    def on_leave(self, e):
        entry = e.widget
        if entry.get() == '':
            entry.insert(0, entry.placeholder)
            entry.config(fg="gray")
            if entry.placeholder == "enter your password" or entry.placeholder == "enter a password":
                entry.config(show="")

class LoginForm(FormView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.heading_text.config(text="Log In")

        self.user_entry.insert(0, "enter your username")
        self.user_entry.placeholder = "enter your username"
        self.user_entry.bind("<FocusIn>", self.on_enter)
        self.user_entry.bind("<FocusOut>", self.on_leave)

        self.password_entry.insert(0, "enter your password")
        self.password_entry.placeholder = "enter your password"
        self.password_entry.bind("<FocusIn>", self.on_enter)
        self.password_entry.bind("<FocusOut>", self.on_leave)

        self.button_wid.config(text="Log in")

class SigninForm(FormView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.heading_text.config(text="Sign In")

        self.user_entry.insert(0, "enter a username")
        self.user_entry.placeholder = "enter a username"
        self.user_entry.bind("<FocusIn>", self.on_enter)
        self.user_entry.bind("<FocusOut>", self.on_leave)

        self.password_entry.insert(0, "enter a password")
        self.password_entry.placeholder = "enter a password"
        self.password_entry.bind("<FocusIn>", self.on_enter)
        self.password_entry.bind("<FocusOut>", self.on_leave)

        self.button_wid.config(text="Sign in")

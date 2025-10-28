from view.widgets import NewTk
import tkinter as tk
from PIL import Image, ImageTk, ImageOps
from config import W_APP, H_APP
from config import APP_TITLE

class MainView(NewTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # --- Configuración de la ventana ---
        self.center_Tk(W_APP, H_APP)
        self.title(APP_TITLE)

        # --- Frames ---
        top_frame = tk.Frame(self, bg="#9c1b83")
        top_frame.grid(row=0, column=0, sticky="nsew")

        mid_frame = tk.Frame(self, bg="white")
        mid_frame.grid(row=1, column=0, sticky="nsew")

        bottom_frame = tk.Frame(self, bg="#9c1b83")
        bottom_frame.grid(row=2, column=0, sticky="nsew")

        # --- Configuración del grid ---
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=100)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # ---Frame superior---
        # --- logo tambo
        self.image_logo = Image.open("images/tambo_flyer02.png")
        self.image_logo = self.image_logo.resize((200, 100), Image.LANCZOS)
        self.image_tk_logo = ImageTk.PhotoImage(self.image_logo)
        self.label_image_logo = tk.Label(top_frame, image=self.image_tk_logo, bg="#9c1b83")
        self.label_image_logo.pack(side="left", padx=(10, 0))

        # --- perfil de ususario ---
        self.image_profile = Image.open("images/user.ico")
        self.image_profile = self.image_profile.resize((50, 50), Image.LANCZOS)
        self.image_tk_profile = ImageTk.PhotoImage(self.image_profile)
        self.label_image_profile = tk.Label(top_frame, image=self.image_tk_profile, bg="#9c1b83")
        self.label_image_profile.pack(side="right", padx=(0, 60))
        
        self.frame_user_data = tk.Frame(top_frame)

        # --- Frame inferior ---
        self.local_time = tk.Label(bottom_frame)
        self.local_time.pack(side="left")

        self.local_date = tk.Label(bottom_frame)
        self.local_date.pack(side="right")


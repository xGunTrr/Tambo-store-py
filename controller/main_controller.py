from view.main_view import MainView
import pytz
import locale
from datetime import datetime

class MainController:
    def __init__(self, user_dao):
        self.user_dao = user_dao
        self.main_view = MainView()
        self.actualizar_hora()

    def actualizar_hora(self):
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        zona = pytz.timezone('America/Lima')
        ahora = datetime.now(zona)

        # --- Formatear hora y fecha ---
        hora = ahora.strftime('%H:%M:%S') # e.g. 14:41:03 pm
        fecha = ahora.strftime('%A, %d de %B de %Y')  # e.g. Lunes, 27 de octubre de 2025

        # --- Actualizar etiquetas ---
        self.main_view.local_time.config(text=f"Hora Local: {hora}", bg="#9B1C6E", fg="#FFFFFF")
        self.main_view.local_date.config(text=f"Fecha Local: {fecha}", bg="#9B1C6E", fg="#FFFFFF")

        # --- Volver a ejecutar cada segundo ---
        self.main_view.local_time.after(1000, self.actualizar_hora)
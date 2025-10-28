import tkinter as tk

class NewTopLevel(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

    # --- Método que permite centrar una ventana ---
    def center_top_level(self, wventana, hventana):
        wtotal, htotal = self.winfo_screenwidth(), self.winfo_screenheight()
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
    
        self.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

class NewTk(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    # --- Método que permite centrar una ventana ---
    def center_Tk(self, wventana, hventana):
        wtotal, htotal = self.winfo_screenwidth(), self.winfo_screenheight()
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
    
        self.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))        
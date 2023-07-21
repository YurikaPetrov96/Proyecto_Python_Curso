import customtkinter
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk
import imageio

class Home(customtkinter.CTkFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        customtkinter.CTkFrame.__init__(self, parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        
        # for i in range(5):
        # self.grid_rowconfigure(i, weight=0)
        # self.grid_columnconfigure(i, weight=0)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=2)
        self.grid_columnconfigure(4, weight=1)
        
        #labels
        
        #botones
        button1 = customtkinter.CTkButton(self, text="Indice", font=("ROBOTO", 14))
        button1.grid(row=3, column= 1, sticky ="ne", ipadx=20)
        button2 = customtkinter.CTkButton(self, text="Historial", font=("ROBOTO", 14))
        button2.grid(row=3, column= 2, sticky="n", ipadx=20)
        button3 = customtkinter.CTkButton(self, text="Busqueda", font=("ROBOTO", 14))
        button3.grid(row=3, column= 3, sticky="nw", ipadx=20)
        log_out_button = customtkinter.CTkButton(self, text="Cerrar Sesion", command= self.cerrar_sesion)
        log_out_button.grid(row=0, column= 4, sticky = "ne")
        
        
        
    def cerrar_sesion(self):
        self.switch_frame_callback("Start_page")
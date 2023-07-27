import customtkinter
from CTkMessagebox import CTkMessagebox

class Indice(customtkinter.CTkFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        
        label = customtkinter.CTkLabel(self, text="Hola soy el indice", font=("ROBOTO", 16))
        label.pack(padx=20, pady=20)

class Historial(customtkinter.CTkFrame):
    def __init__(self, Frame, switch_frame_callback, *args, **kwargs):
        super().__init__(Frame, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        
        label = customtkinter.CTkLabel(self, text="Historial", font=("ROBOTO", 16))
        label.pack(padx=20, pady=20)

class Search_gui(customtkinter.CTkFrame):
    def __init__(self, Frame, switch_frame_callback, *args, **kwargs):
        super().__init__(Frame, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        from utils import buscador

        label = customtkinter.CTkLabel(self, font=("ROBOTO", 16), comand=ventana_buscador)
        label.pack(padx=20, pady=20)

# pages = {
#     "Indice":Indice,
#     "Historial":Historial,
#     "Buscador":Search_gui
# }


class Home(customtkinter.CTkScrollableFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        customtkinter.CTkScrollableFrame.__init__(self, parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        self.current_frame = None
        
        # for i in range(5): #ejemplo para automaticamente asignar el mimsmo valor a todas las celdas.
        # self.grid_rowconfigure(i, weight=0)
        # self.grid_columnconfigure(i, weight=0)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)
        self.grid_columnconfigure(3, weight=1)
            
        #labels
        
        #botones
        
        button1 = customtkinter.CTkButton(self, text="Indice", font=("ROBOTO", 14), command= self.Go_indice)
        button1.grid(row=0, column= 1, sticky ="ne", padx=5, ipadx=20)
        button2 = customtkinter.CTkButton(self, text="Historial", font=("ROBOTO", 14), command= self.Go_historial)
        button2.grid(row=0, column= 2, sticky="n", padx=5, ipadx=20)
        button3 = customtkinter.CTkButton(self, text="Busqueda", font=("ROBOTO", 14), command= self.Go_search_gui)
        button3.grid(row=0, column= 3, sticky="nw", padx=5, ipadx=20)
        log_out_button = customtkinter.CTkButton(self, text="Cerrar Sesion", command= self.cerrar_sesion)
        log_out_button.grid(row=0, column= 4, sticky = "ne")
        
        
        
    def show_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.grid_forget()  # Hide the current frame if any
        self.current_frame = frame_class(self, self.switch_frame_callback)
        self.current_frame.grid(row=1, column=0, columnspan=4, sticky="nsew")    
    
    def Go_search_gui(self):
        self.show_frame(Search_gui)
    
    def Go_indice(self):
        self.show_frame(Indice)
            
    def Go_historial(self):
        self.show_frame(Historial)
            
    def cerrar_sesion(self):
        self.switch_frame_callback("Start_page")
        

        
        
             
    
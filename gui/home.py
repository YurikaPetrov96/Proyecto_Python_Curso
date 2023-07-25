import customtkinter
from CTkMessagebox import CTkMessagebox

class Indice(customtkinter.CTkFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        
    #configuración de las lineas
        self.grid_rowconfigure(0, weight=1)
        for i in range(1,4):
            self.grid_rowconfigure(i, weight=0)
        
        #configuracion de las columnas
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        self.grid_columnconfigure(4, weight= 2)
        self.grid_columnconfigure(5, weight= 1)
        self.grid_columnconfigure(6, weight= 0)
        
        #labels
        placeholder_label = customtkinter.CTkLabel(self, text = "")
        placeholder_label.grid(row=0, column= 1, columnspan=5)
        label0 = customtkinter.CTkLabel(self, text="Buscar:", font=("", 15, "bold"))
        label0.grid(row=1, column= 4, sticky= "ne")
        
        
        #entries
        self.entry0 = customtkinter.CTkEntry(self)
        self.entry0.grid(row=1, column=5, sticky="nwe", padx=5)
        
        
        
        
        #botones
        button1= customtkinter.CTkButton(self, text="Buscar", command="")
        button1.grid(row=1, column= 6, sticky="ne")
        
        
    def show_search(self):
        """Para mostrar lo que se requiera en el busacdor"""
        busqueda = self.entry0.get()
        busqueda

class Historial(customtkinter.CTkFrame):
    def __init__(self, Frame, switch_frame_callback, *args, **kwargs):
        super().__init__(Frame, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        
        label = customtkinter.CTkLabel(self, text="Historial", font=("ROBOTO", 16))
        label.pack(padx=20, pady=20)
        

class Home(customtkinter.CTkScrollableFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        customtkinter.CTkScrollableFrame.__init__(self, parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        self.current_frame = None
        
        #configuracion de columnas
        
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
        log_out_button = customtkinter.CTkButton(self, text="Cerrar Sesion", command= self.cerrar_sesion)
        log_out_button.grid(row=0, column= 4, sticky = "ne")
        
        
        
    def show_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.grid_forget()  # Hide the current frame if any
        self.current_frame = frame_class(self, self.switch_frame_callback)
        self.current_frame.grid(row=1, column=0, columnspan=5, sticky="nsew")    
    
    
    def Go_indice(self):
        self.show_frame(Indice)
            
    def Go_historial(self):
        self.show_frame(Historial)
            
    def cerrar_sesion(self):
        self.switch_frame_callback("Start_page")
        

        
        
             
    
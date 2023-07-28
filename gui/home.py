import customtkinter
from CTkMessagebox import CTkMessagebox
import datetime

class Main_page(customtkinter.CTkFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        
    #configuración de las lineas
        self.grid_rowconfigure(0, weight=0)
        for i in range(1,4):
            self.grid_rowconfigure(i, weight=1)
        
        #configuracion de las columnas
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        self.grid_columnconfigure(4, weight= 2)
        self.grid_columnconfigure(5, weight= 1)
        self.grid_columnconfigure(6, weight= 0)
        
        #labels
        label0 = customtkinter.CTkLabel(self, text="Buscar:", font=("", 15, "bold"))
        label0.grid(row=0, column= 4, sticky= "ne")
        label2 = customtkinter.CTkLabel(self, text="Historial")
        label2.grid(row=2, column=5, columnspan=2, sticky= "news")
        self.label3 = customtkinter.CTkLabel(self, text="", font=("", 12))
        self.label3.grid(row=3, column=5, columnspan= 2, sticky= "news")
        
        
        #entries
        self.entry0 = customtkinter.CTkEntry(self)
        self.entry0.grid(row=0, column=5, sticky="nwe", padx=5)
        
        
        
        
        #botones
        button1= customtkinter.CTkButton(self, text="Buscar", command="")
        button1.grid(row=0, column= 6, sticky="ne")
        
        
        self.show_time()
    

    def show_history():
        pass
       
    def show_search(self):
        """Para mostrar lo que se requiera en el busacdor"""
        busqueda = self.entry0.get()
        busqueda
        
    def show_time(self):
        """Para definir un refrezco de pantalla"""
        time = datetime.datetime.now().strftime("Time:%H:%M:%S")
        self.label3.configure(text=time)
        self.label3['text'] = time
        self.after(5000, self.show_time)
        
class Mapa(customtkinter.CTkFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        
        

class Home(customtkinter.CTkScrollableFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        customtkinter.CTkScrollableFrame.__init__(self, parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        self.current_frame = None
        
        #configuracion de columnas
        
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=2)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)
        self.grid_columnconfigure(3, weight=1)
            
        #labels
        
        #botones
        button1 = customtkinter.CTkButton(self, text="Pagina Principal", font=("ROBOTO", 14), command= self.go_main_frame)
        button1.grid(row=0, column= 1, sticky ="ne", padx=5, ipadx=20)
        button2 = customtkinter.CTkButton(self, text="Mapa y Reviews", font=("ROBOTO", 14), command= self.go_map)
        button2.grid(row=0, column= 2, sticky="n", padx=5, ipadx=20)
        log_out_button = customtkinter.CTkButton(self, text="Cerrar Sesion", command= self.cerrar_sesion)
        log_out_button.grid(row=0, column= 4, sticky = "ne")
        
        placeholder_label = customtkinter.CTkLabel(self, text = "")
        placeholder_label.grid(row=1, column= 0, columnspan=4)
        
        
        
    def show_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.grid_forget()  # Oculta el frame actual si hay alguno.
        self.current_frame = frame_class(self, self.switch_frame_callback)
        self.current_frame.grid(row=2, column=0, columnspan=5, sticky="nsew")    
    
    
    def go_main_frame(self):
        self.show_frame(Main_page)
            
    def go_map(self):
        self.show_frame(Mapa)
            
    def cerrar_sesion(self):
        self.switch_frame_callback("Start_page")
        

        
        
             
    
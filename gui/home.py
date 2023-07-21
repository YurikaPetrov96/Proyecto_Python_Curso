import customtkinter

class Home(customtkinter.CTkFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        customtkinter.CTkFrame.__init__(self, parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        
        for i in range(5):
            self.grid_rowconfigure(i, weight=0)
            self.grid_columnconfigure(i, weight=0)
        
        
        
        
        
        
        
        
        log_out_button = customtkinter.CTkButton(self, text="Cerrar Sesion", command= self.cerrar_sesion)
        log_out_button.grid(row=2, column= 1)
        
        
        
    def cerrar_sesion(self):
        self.switch_frame_callback("Start_page")
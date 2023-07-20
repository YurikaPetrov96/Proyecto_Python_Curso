import customtkinter

class Home(customtkinter.CTkFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        customtkinter.CTkFrame.__init__(self, parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        
        
        
        
        
        
        
        
        
        
        log_out_button = customtkinter.CTkButton(self, text="Cerrar Sesion", command= self.cerrar_sesion)
        log_out_button.grid(row=4, column= 3)
        
        
        
    def cerrar_sesion(self):
        self.switch_frame_callback("Start_page")
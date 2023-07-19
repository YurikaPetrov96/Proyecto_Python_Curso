import customtkinter
   
## 1
class Login_register(customtkinter.CTkFrame):
    """Un frame de inicio: """
    def __init__(self, parent,  *args, **kwargs):
        customtkinter.CTkFrame.__init__(self, parent, *args, **kwargs)
        
        
        #rely and relx, even the relative ones need to ve between 0 and 1, AND, relative should be a fraction of the rely or relx
        bienvenida_label = customtkinter.CTkLabel(self, text= "Iniciar Sesion o Registrarse.")
        bienvenida_label.grid(row=0, column=4, padx=0, pady=0)
        
        #labels
        username_label = customtkinter.CTkLabel(self, text= "Usuario:")
        username_label.grid(row=1, column=2, padx=5, pady=5)
        contrasena_label = customtkinter.CTkLabel(self, text= "Contraseña:")
        contrasena_label.grid(row=2, column=2, padx=5, pady=5)
        
        #entries
        username_entry = customtkinter.CTkEntry(self)
        username_entry.grid(row=1, column=4, padx=5, pady=5)
        contrasena_entry = customtkinter.CTkEntry(self, show= "*")
        contrasena_entry.grid(row=2, column= 4, padx=5, pady=5)
        
        #botones
        
        registro_button = customtkinter.CTkButton(self, text="Registese", command=lambda: parent.switch_frame("Registry_page"))
        registro_button.grid(row=3, column=2, padx=5, pady=5)
        authenticate_button = customtkinter.CTkButton(self, text="Iniciar Sesion", command="")
        authenticate_button.grid(row=3, column=4, padx=5, pady=5)





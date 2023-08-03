import customtkinter
from CTkMessagebox import CTkMessagebox
from models.users import Usuario
from models.users import Verificacion
   
## 1
class Login_register(customtkinter.CTkFrame):
    """Un frame de inicio: """
    def __init__(self, parent, switch_frame_callback,  *args, **kwargs):
        customtkinter.CTkFrame.__init__(self, parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback ## si o si tiene que estar en los Frame, porque esta en la app principal
        
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=1)
        
        
        #labels
        bienvenida_label = customtkinter.CTkLabel(self, text= "Inicie Sesion o Registrese: ", font=("Roboto",16))
        bienvenida_label.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="s")
        username_label = customtkinter.CTkLabel(self, text= "Usuario:")
        username_label.grid(row=1, column=1, padx=5, pady=5, sticky="e")
        contrasena_label = customtkinter.CTkLabel(self, text= "Contraseña:")
        contrasena_label.grid(row=2, column=1, padx=5, pady=5, sticky="e")
        
        #entries
        self.username_entry = customtkinter.CTkEntry(self)
        self.username_entry.grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.contrasena_entry = customtkinter.CTkEntry(self, show= "*")
        self.contrasena_entry.grid(row=2, column= 2, padx=5, pady=5, sticky="nw")
        
        #botones
        
        registro_button = customtkinter.CTkButton(self, text="Registrarse", command=lambda: parent.switch_frame("Registry_page"))
        registro_button.grid(row=3, column=1, padx=5, pady=5, sticky="ne")
        authenticate_button = customtkinter.CTkButton(self, text="Iniciar Sesion", command=self.validacion_log)
        authenticate_button.grid(row=3, column=2, padx=5, pady=5, sticky="nw")
        
    
    def validacion_log(self):
        username = self.username_entry.get().strip()
        password = self.contrasena_entry.get()
        
        
        try:
            # Si la información es valida, se procedera a registrar al usuario
            
            if Verificacion.username_check1(self, username) is True:
                
                authentification_result = Usuario(username, password).autentificar_usuario()
                id_token= Usuario(username, password).token_user()
                self.master.user_id = id_token
                print(self.master.user_id)
                # si todo funcionó correctamente, veremos un mensaje de Login efectivo y abrira home
                if authentification_result is True:
                    self.show_good_messages()
                    self.username_entry.delete(0, customtkinter.END)
                    self.contrasena_entry.delete(0, customtkinter.END)
                    
                else:
                    self.show_failed()
                    self.master.user_id = None
            else:
                self.show_user_not_found_msg()
        except InputError as e:
            print(e)
            
    def show_good_messages(self):
            self.go_home_page()
    
    def show_failed(self):
        msg = CTkMessagebox(title="No permitido", message="No pudiste iniciar sesion. Intenta de Nuevo", icon ="cancel", option_1="Ok")
        response = msg.get()
        if response =="OK":
            self.go_back()
    
    def show_user_not_found_msg(self):
        msg = CTkMessagebox(title="Usuario no encontrado", message="El usuario ingresado no existe.", icon="warning", option_1="OK")
        response = msg.get()
        if response =="OK":
            self.go_back()
    
    def go_home_page(self):
        """Metodo para volver a la pagina Home, osea Indice"""
        self.switch_frame_callback("Home_page")
        
        
    def go_back(self):
        """Metodo para ir al frame Start_page donde nos logeamos."""
        self.switch_frame_callback("Start_page")
            
            
class InputError(Exception):
    """Elevamos este error cuando lo ingresado por el usuario es incorrecto.
    Attributes:
        expr -- Mencionamos parte del codigo donde sucedió el error.
        msg  -- Explicacion del error
    """
    def __init__(self, msg):
        super().__init__(msg)



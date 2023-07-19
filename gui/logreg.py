import customtkinter
from CTkMessagebox import CTkMessagebox
from models.users import Usuario
   
## 1
class Login_register(customtkinter.CTkFrame):
    """Un frame de inicio: """
    def __init__(self, parent, switch_frame_callback,  *args, **kwargs):
        customtkinter.CTkFrame.__init__(self, parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback ## si o si tiene que estar en los Frame, porque esta en la app principal
        
        
        bienvenida_label = customtkinter.CTkLabel(self, text= "Iniciar Sesion o Registrarse.")
        bienvenida_label.grid(row=0, column=4, padx=0, pady=0)
        
        #labels
        username_label = customtkinter.CTkLabel(self, text= "Usuario:")
        username_label.grid(row=1, column=2, padx=5, pady=5)
        contrasena_label = customtkinter.CTkLabel(self, text= "Contraseña:")
        contrasena_label.grid(row=2, column=2, padx=5, pady=5)
        
        #entries
        self.username_entry = customtkinter.CTkEntry(self)
        self.username_entry.grid(row=1, column=4, padx=5, pady=5)
        self.contrasena_entry = customtkinter.CTkEntry(self, show= "*")
        self.contrasena_entry.grid(row=2, column= 4, padx=5, pady=5)
        
        #botones
        
        registro_button = customtkinter.CTkButton(self, text="Registrarse", command=lambda: parent.switch_frame("Registry_page"))
        registro_button.grid(row=3, column=2, padx=5, pady=5)
        authenticate_button = customtkinter.CTkButton(self, text="Iniciar Sesion", command=self.validacion_log)
        authenticate_button.grid(row=3, column=4, padx=5, pady=5)
    
    def validacion_log(self):
        username = self.username_entry.get().strip()
        password = self.contrasena_entry.get()
        
        try:
            # Si la información es valida, se procedera a registrar al usuario
            authentification_result = Usuario(username, password).autentificar_usuario()
            # si todo funcionó correctamente, veremos un mensaje de Login efectivo y abrira home
            if authentification_result is True:
                self.show_good_messages()
            elif authentification_result is False:
                self.show_failed()
            else:
                self.show_user_not_found_msg()
        except InputError as e:
            print(e)
            
    def show_good_messages(self):
        msg = CTkMessagebox(title="Exito.", message="Iniciaste sesion exitosamente.", icon = "check", option_1="OK")
        response = msg.get()
        if response =="OK":
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
        """Function to go back to start_page"""
        self.switch_frame_callback("Home_page")
        
    def go_back(self):
        self.switch_frame_callback("Start_page")
            
            
class InputError(Exception):
    """Raised when user input is incorrect
    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """
    def __init__(self, msg):
        super().__init__(msg)



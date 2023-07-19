import customtkinter
from CTkMessagebox import CTkMessagebox
from models.users import Usuario
from models.users import Verificacion

class Registro(customtkinter.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        customtkinter.CTkFrame.__init__(self, parent, *args, **kwargs)
        
        #labels
        label0 = customtkinter.CTkLabel(self, text="Por favor ingrese los datos del formulario: ")
        label0.grid(row=0, column=0, columnspan = 3, padx=10, pady= 10)
        label1 = customtkinter.CTkLabel(self, text="Usuario: ")
        label1.grid(row=1, column=0, padx=5, pady=5)
        label2 = customtkinter.CTkLabel(self, text="Contraseña: ")
        label2.grid(row=2, column=0, padx=5, pady=5)
        label3 = customtkinter.CTkLabel(self, text="Email: ")
        label3.grid(row=3, column=0, padx=5, pady=5)
        
        #entries
        self.entry1=customtkinter.CTkEntry(self)
        self.entry1.grid(row=1, column=1, padx=5, pady=5)
        self.entry2=customtkinter.CTkEntry(self, show="*")
        self.entry2.grid(row=2, column=1, padx=5, pady=5)
        self.entry3=customtkinter.CTkEntry(self)
        self.entry3.grid(row=3, column=1, padx=5, pady=5)
        
        #botones
        final_button = customtkinter.CTkButton(self, text="Registrarse", command=lambda: self.verificar_registro())
        final_button.grid(row=4, column=10, columnspan=2, padx=1, pady=1)
        cancel_button = customtkinter.CTkButton(self, text="Cancerlar", command=lambda: parent.switch_frame("Start_page"))
        cancel_button.grid(row=4, column=12, columnspan=2, padx=1, pady=1)
        
    def verificar_registro(self):
        username = self.entry1.get()
        password = self.entry2.get()
        email = self.entry3.get()
        
        # Validamos la información de usuario.
        try:
            verifier = Verificacion()
            verifier.username_check(username)
            verifier.password_check(password)
            verifier.email_check(email)
            
            # Si la información es valida, se procedera a registrar al usuario
            Usuario(username, password, email).registrar_usuario()
            # si todo funcionó correctametne, veremos un mensaje de registro efectivo y volveremos a login.
            self.show_success_message() # muestra un mensaje de registro exitoso.
        except InputError as e:
            print(e)
            
    def show_success_message(self):
        msg = CTkMessagebox(title="Registro Exitoso.", message="Registro completado satisfactoriamente.", icon = "check", option_1="OK")
        response = msg.get()
        if response =="OK":
            self.go_back_start()
    
    def go_back_start(self):
        """Function to go back to start_page"""
        lambda: self.switch_frame("Start_page")
            
            
class InputError(Exception):
    """Raised when user input is incorrect
    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """
    def __init__(self, msg):
        pass
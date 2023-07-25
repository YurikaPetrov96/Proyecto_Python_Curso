import customtkinter
from CTkMessagebox import CTkMessagebox
from models.users import Usuario
from models.users import Verificacion

class Registro(customtkinter.CTkFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        customtkinter.CTkFrame.__init__(self, parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        
        #configuracion de lineas
        self.grid_rowconfigure(0, weight=1)
        for i in range(1,5):
            self.grid_rowconfigure(i, weight=0)
        self.grid_rowconfigure(6, weight=1)
        #configuracion de columnas
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=1)
        
        
        #labels
        label0 = customtkinter.CTkLabel(self, text="Por favor ingrese los datos del formulario: ", font=("Roboto",16))
        label0.grid(row=0, column=1, columnspan=2, padx=5, pady= 5, sticky="s")
        label1 = customtkinter.CTkLabel(self, text="Nombre de Usuario:", font=("Roboto",14))
        label1.grid(row=1, column=1, padx=5, pady=5, sticky= "e", ipadx=17)
        label2 = customtkinter.CTkLabel(self, text="Contraseña:", font=("Roboto",14))
        label2.grid(row=2, column=1, padx=5, pady=5, sticky="ne", ipadx=17)
        label3 = customtkinter.CTkLabel(self, text="Apellido:", font=("Roboto",14))
        label3.grid(row=3, column=1, padx=5, pady=5, sticky="ne", ipadx=17)
        label4 = customtkinter.CTkLabel(self, text="Primer Nombre:", font=("Roboto",14))
        label4.grid(row=4, column=1, padx=5, pady=5, sticky="ne", ipadx=17)
        label5 = customtkinter.CTkLabel(self, text="Correo Electronico:", font=("Roboto",14))
        label5.grid(row=5, column=1, padx=5, pady=5, sticky="ne", ipadx=17)
        
        #entries
        self.entry1=customtkinter.CTkEntry(self)
        self.entry1.grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.entry2=customtkinter.CTkEntry(self, show="*")
        self.entry2.grid(row=2, column=2, padx=5, pady=5, sticky="nw")
        self.entry3=customtkinter.CTkEntry(self)
        self.entry3.grid(row=3, column= 2, padx= 5, pady=5, sticky="nw")
        self.entry4=customtkinter.CTkEntry(self)
        self.entry4.grid(row=4, column= 2, padx=5, pady=5, sticky="nw")
        self.entry5=customtkinter.CTkEntry(self)
        self.entry5.grid(row=5, column=2, padx=5, pady=5, sticky="nw")
        
        #botones
        final_button = customtkinter.CTkButton(self, text="Registrarse", command=lambda: self.verificar_registro(), font=("Roboto",14))
        final_button.grid(row=6, column=1, padx=1, pady=1, sticky="ne", ipadx=4)
        cancel_button = customtkinter.CTkButton(self, text="Cancerlar", command=lambda: self.switch_frame_callback("Start_page"), font=("Roboto",14))
        cancel_button.grid(row=6, column=2, padx=1, pady=1, sticky="nw", ipadx=3)
        
    def verificar_registro(self):
        username = self.entry1.get()
        password = self.entry2.get()
        apellido = self.entry3.get().capitalize()
        nombre = self.entry4.get().capitalize()
        email = self.entry5.get()
        
        # Validamos la información de usuario.
        try:
            verifier = Verificacion()
            user_check1 = verifier.username_check1(username)
            user_check2 = verifier.username_check2(username)
            pass_check = verifier.password_check(password)
            app_check = verifier.apellido_check(apellido)
            nombre_check= verifier.nombre_check(nombre)
            email_check = verifier.email_check(email)
            
            while True:
                if user_check1 is True:
                    self.Boxes.username_used(self)
                    return False
                if user_check2 is False:
                    self.Boxes.user_check_box(self)
                    return False
                if pass_check is False:
                    self.Boxes.user_pass_box(self)
                    return False
                if app_check is False:
                    self.Boxes.app_box(self)
                    return False
                if nombre_check is False:
                    self.Boxes.nom_box(self)
                    return False
                if email_check is False:
                    self.Boxes.user_email_box(self)
                    return False
                else: 
                    # Si la información es valida, se procedera a registrar al usuario
                    Usuario(username, password, apellido, nombre, email).registrar_usuario()
                    # si todo funcionó correctametne, veremos un mensaje de registro efectivo y volveremos a login.
                    self.Boxes.show_success_message(self) # muestra un mensaje de registro exitoso.
                    return False
        except InputError as e:
            print(e)
    
    
    class Boxes(CTkMessagebox):
        def init__(self, switch_frame_callback, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.switch_frame_callback = switch_frame_callback
            
        def show_success_message(self):
            msg = CTkMessagebox(title="Registro Exitoso.", message="Registro completado satisfactoriamente.", icon = "check", option_1="OK")
            response = msg.get()
            if response =="OK":
                self.switch_frame_callback("Start_page")
        
        def user_check_box(self):
            msg = CTkMessagebox(title="Username Invalido", message="Ingrese un nombre de usuario mayor o igual a 4 caracteres.", option_1="OK")
            response = msg.get()
            if response =="OK":
                msg.destroy()
            
        def user_pass_box(self):
            msg = CTkMessagebox(title="Contraseña Invalida.", message="Ingrese una contraseña con 6 o mas caracteres, y que tenga al menos un numero", option_1="OK")
            response = msg.get()
            if response =="OK":
                msg.destroy()
                
        def app_box(self):
            msg = CTkMessagebox(title="Error Apellido", message="Ingrese un apellido por favor.", option_1="OK")
            response = msg.get()
            if response =="OK":
                msg.destroy()
        
        def nom_box(self):
            msg = CTkMessagebox(title="Error Nombre", message="Ingrese un nombre por favor.", option_1="OK")
            response = msg.get()
            if response =="OK":
                msg.destroy()
                
        def user_email_box(self):
            msg = CTkMessagebox(title="Email invalido", message="Ingrese un email valido.", option_1="OK")
            response = msg.get()
            if response =="OK":
                msg.destroy()          
        
        def username_used(self):
            msg = CTkMessagebox(title="Usuario ya registrado.", message="El nombre de usuario ya fue registrado, por favor intente con otro nombre de usuario.", option_1="OK")
            response = msg.get()
            if response =="OK":
                msg.destroy()   
            
class InputError(Exception):
    """Raised when user input is incorrect
    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """
    def __init__(self, msg):
        super().__init__(msg)
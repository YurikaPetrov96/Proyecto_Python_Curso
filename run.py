import tkinter as tk
from tkinter import ttk
import json
import hashlib

class use_json: #clase Json para poder tener mejor las variables a usar.
    @staticmethod
    def save_data(data):
        with open("data/users.json", "w") as file:
            json.dump(data, file)
    
    @staticmethod
    def load_data():
        try:
            with open("data/users.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

class Usuario: # clase usuario inicializada, y con metodos estaticos.
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    @staticmethod
    def hash_password(password, salt):
        hash_object = hashlib.sha256()
        hash_object.update(password.encode('utf-8') + salt.encode('utf-8'))
        return hash_object.hexdigest()
    
    @staticmethod
    def registrar_usuario():
        username = app.frame.username_entry.get()
        password = app.frame.password_entry.get()
        salt = "random_salt"
        hashed_password = Usuario.hash_password(password, salt)
        data = use_json.load_data()
        data[username] = {
            "salt": salt,
            "hashed_password": hashed_password
        }
        use_json.save_data(data)
        print("Datos Guardados")
      
    @staticmethod
    def autentificar_usuario():
        data = use_json.load_data()  #ingresa datos antes de realizar la autentificacion
        username = app.frame.username_entry.get()
        password = app.frame.password_entry.get()
        if username in data:
            user_data = data[username]
            hashed_password = Usuario.hash_password(password, user_data["salt"])
            if hashed_password == user_data["hashed_password"]:
                print("Iniciaste Sesion.")
                return True
        print("No pudiste iniciar sesion.")
        return False

class Main_frame(tk.Frame):
    """
    Main Frame of this program.
    """
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        registro_label = ttk.Label(self, text="Inicie Sesion o Registrese: ")
        registro_label.grid(row=0, column=0, padx=10, pady=1)

        self.username_label = ttk.Label(self, text="Ingrese su nombre de Usuario: ")
        self.username_label.grid(row=1, column=0, padx=0, pady=10)
        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(row=1, column=1, padx=1, pady=10)

        self.password_label = ttk.Label(self, text="Ingrese su contraseña: ")
        self.password_label.grid(row=2, column=0, padx=0, pady=10)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.grid(row=2, column=1, padx=0, pady=10)

        add_button = ttk.Button(self, text="Registrarse", command=Application.Change_frame)
        add_button.grid(row=3, column=0, columnspan=2, padx=1, pady=2)

        authenticate_button = ttk.Button(self, text="Autenticar", command=Usuario.autentificar_usuario)
        authenticate_button.grid(row=3, column=1, columnspan=2, padx=1, pady=2)


class Registro_frame(tk.Frame):
    def __init__(self, registro, *args, **kwargs):
        super().__init__(registro, *args, **kwargs)
        
        registro_label = ttk.Label(self, text="Registrese por favor: ")
        registro_label.grid(row=0, column=0, padx=10, pady=1)

        self.username_label = ttk.Label(self, text="Ingrese su nombre de Usuario: ")
        self.username_label.grid(row=1, column=0, padx=0, pady=10)
        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(row=1, column=1, padx=1, pady=10)

        self.password_label = ttk.Label(self, text="Ingrese su contraseña: ")
        self.password_label.grid(row=2, column=0, padx=0, pady=10)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.grid(row=2, column=1, padx=0, pady=10)
        
        
        add_button = ttk.Button(self, text="Registrarse", command=Usuario.registrar_usuario)
        add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)



class Application(tk.Tk):
    """Main window for the application"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("App Proyecto Cimne")
        self.geometry("800x600")
        self.iconbitmap("music.ico")
        self.frame = Main_frame(self)
        self.frame.pack()
    
    def Change_frame():
        pass


if __name__ == "__main__":
    app = Application()
    app.mainloop()

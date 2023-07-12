from tkinter import *
from tkinter import ttk
import sv_ttk
import json
import hashlib

class use_json: #clase Json para poder tener mejor las variables a usar.
    @staticmethod
    def save_data(data):
        with open("src/users.json", "w") as file:
            json.dump(data, file)
    
    @staticmethod
    def load_data():
        try:
            with open("src/users.json", "r") as file:
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
        username = username_entry.get()
        password = password_entry.get()
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
        username = username_entry.get()
        password = password_entry.get()
        if username in data:
            user_data = data[username]
            hashed_password = Usuario.hash_password(password, user_data["salt"])
            if hashed_password == user_data["hashed_password"]:
                print("Autentificacion Permitida")
                return True
        print("Autentificacion Fracasada.")
        return False

class Local:
    def __init__(self):
        pass

root = Tk()
root.title("Tour Musical")
root.geometry("1280x720+10+10")
root.iconbitmap("src/music.ico")
sv_ttk.use_dark_theme()

registro_label = ttk.Label(root, text="Registrese por favor: ")
registro_label.grid(row=0, column=0, padx=10, pady=10)

username_label = ttk.Label(root, text="Ingrese su nombre de Usuario: ")
username_label.grid(row=1, column=0, padx=10, pady=10)
username_entry = ttk.Entry(root)
username_entry.grid(row=1, column=1, padx=10, pady=10)

password_label = ttk.Label(root, text="Ingrese su contraseña: ")
password_label.grid(row=2, column=0, padx=10, pady=10)
password_entry = ttk.Entry(root, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10)

add_button = ttk.Button(root, text="Registrarse", command=Usuario.registrar_usuario)
add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

authenticate_button = ttk.Button(root, text="Autenticar", command=Usuario.autentificar_usuario)
authenticate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

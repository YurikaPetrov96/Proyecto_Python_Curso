import json
import hashlib
import os
import re


class db():
    """Accedemos al a base de datos (json.)"""
    @staticmethod
    def save_data(data, file_name, folder_path="data/"):
        file_path = os.path.join(folder_path, file_name)
        current_data = db.load_data(file_path)
        current_data.update(data)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file)
    
    @staticmethod
    def load_data(file_name, folder_path="data/"):
        file_path = os.path.join(folder_path, file_name)
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
        
    @staticmethod
    def load_data_from_eventos(file_name, folder_path="data/"):
        file_path = os.path.join(folder_path, file_name)
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                event_data = json.load(file)
                for event in event_data:
                    event["indice"] = int(event["indice"])
                return event_data
        except (FileNotFoundError, json.JSONDecodeError):
            return []

class Usuario():
    def __init__(self, username, password, apellido= None, nombre=None, email=None):
        self.username = username
        self.password = password
        self.apellido = apellido
        self.nombre = nombre
        self.email = email
        self.user_id = Usuario.generate_user_id()
    
    @staticmethod
    def hash_password(password, salt):
        hash_object = hashlib.sha256()
        hash_object.update(password.encode('utf-8') + salt.encode('utf-8'))
        return hash_object.hexdigest()
    
    @classmethod
    def generate_user_id(cls): #generamos el user id.
        data = db.load_data("users.json") #caragamos la base de datos
        if data:
            max_user_id = max(map(int, data.keys())) #si en la db hay una key numeral la pasamos a int para realizarle una suma.
            return str(max_user_id + 1)
        else:
            return "1" #si no existe data usamos esto.
            
    def registrar_usuario(self):
        if self.email is None:
            raise InputError("El email es necesario para registrarse.")
        salt = "random_salt"
        hashed_password = Usuario.hash_password(self.password, salt)
        email = self.email
        data = db.load_data("users.json")
        data[str(self.user_id)] = {
            "username": self.username,
            "salt": salt,
            "hashed_password": hashed_password,
            "apellido": self.apellido,
            "nombre":self.nombre,
            "email": email
        }
        db.save_data(data, "users.json")
        print("Datos Guardados")
        
        
    def autentificar_usuario(self):
        data = db.load_data("users.json")  # Cargamos antes de realizar una verificación.
        for user_id, user_data in data.items():
            if user_data["username"] == self.username:
                hashed_password = Usuario.hash_password(self.password, user_data["salt"])
                if hashed_password == user_data["hashed_password"]:
                    return True
                else:
                    return False  # la contraseña es incorrecta
        return False  # El usuario no fue encontrado en los datos.
    
    def token_user(self):
        data = db.load_data("users.json")
        for user_id, user_data in data.items():
            if user_data["username"] == self.username:
                return user_id


## Validamos los datos de los usuarios

def has_numbers(foo):
    return any(char.isdigit() for char in foo)

def has_simbols(foo):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, foo))

class Verificacion():
    """validacion del usuario"""
    
    def username_check1(self, username):
        try:
            data = db.load_data("users.json")
            for user_id, user_data in data.items():
                if username == user_data["username"]:
                    return True
            
            return False    
        except ValueError:
            print("Error.")
    
    def username_check2(self, username):
        try:
            if len(username) >= 4:
                print("Usuario valido")
                return True
            else:
                return False
        except:
            ValueError
                
    def password_check(self, password):
        try:
            if len(password) >= 6 and has_numbers(password):
                return True
            else:
                return False
        except ValueError:
            print("Se ingresaron caracteres incorrectos.")
            
    def apellido_check(self, apellido):
        """chequeo del apellido"""
        try:
            if apellido == None:
                return False
            else:
                return True
        except ValueError:
            print("Se ingresaron caracteres incorrectos.")
    
    def nombre_check(self, nombre):
        """chequeo de nombre"""
        try:
            if nombre == None:
                return False
            else:
                return True
        except ValueError:
            print("Se ingresaron caracteres incorrectos.")
                
    def email_check(self, email):
        try:
            if has_simbols(email):
                return True
            else:
                return False
        except ValueError:
            print("Se ingresaron caracteres incorrectos.")

class InputError(Exception):
    """Elevamos este error cuando lo ingresado por el usuario es incorrecto.
    Attributes:
        expr -- Mencionamos parte del codigo donde sucedió el error.
        msg  -- Explicacion del error
    """
    def __init__(self, msg):
        pass



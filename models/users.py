import json
import hashlib


class db():
    """access to database"""
    @staticmethod
    def save_data(data):
        with open("data/users.json", "w", encoding="utf-8") as file:
            json.dump(data, file)
    
    @staticmethod
    def load_data():
        try:
            with open("data/users.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

class Usuario():
    user_count = 0
    def __init__(self, username, password, email=None):
        self.username = username
        self.password = password
        self.email = email
        self.user_id = Usuario.generate_user_id()
    
    @staticmethod
    def hash_password(password, salt):
        hash_object = hashlib.sha256()
        hash_object.update(password.encode('utf-8') + salt.encode('utf-8'))
        return hash_object.hexdigest()
    
    @classmethod
    def generate_user_id(cls):
        cls.user_count+=1
        return cls.user_count
            
    def registrar_usuario(self, *args):
        if self.email is None:
            raise InputError("El email es necesario para registrarse.")
        salt = "random_salt"
        hashed_password = Usuario.hash_password(self.password, salt)
        email = self.email
        data = db.load_data()
        data[str(self.user_id)] = {
            "username": self.username,
            "salt": salt,
            "hashed_password": hashed_password,
            "email": email
        }
        db.save_data(data)
        print("Datos Guardados")
        
        
    def autentificar_usuario(self):
        data = db.load_data()  # Load data before performing authentication
        for user_id, user_data in data.items():
            if user_data["username"] == self.username:
                hashed_password = Usuario.hash_password(self.password, user_data["salt"])
                if hashed_password == user_data["hashed_password"]:
                    return True
                else:
                    return False  # The password is incorrect.
        return False  # The user was not found in the data.


## validate user inforamtion before summiting to login or register

def has_numbers(foo):
    return any(char.isdigit() for char in foo)

def has_simbols(foo):
    return any(char == "@" for char in foo)

class Verificacion():
    """validacion del usuario"""
    
    def username_check(self, username):
        try:
            if len(username) < 4: 
                user_g_msg = "Su usuario es Valido"
                return user_g_msg
            else:
                user_b_msg = "Su usario es invalido"
                return user_b_msg
        except:
            ValueError
                
    def password_check(self, password):
        try:
            if len(password) >= 6 and has_numbers(password):
                pass_msg = "La contraseñalen() es valida."
                return pass_msg, 
            else:
                raise InputError("La contraseña ingresada no cumple con las condiciones necesarias.")
        except ValueError:
            print("Se ingresaron caracteres incorrectos.")
                
    def email_check(self, email):
        try:
            if has_simbols(email):
                email_msg = "El email es correcto."
                return email_msg
            else:
                raise InputError("El email no cumple con las condiciones necesarias.")
        except ValueError:
            print("Se ingresaron caracteres incorrectos.")

class InputError(Exception):
    """Raised when user input is incorrect
    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """
    def __init__(self, msg):
        pass



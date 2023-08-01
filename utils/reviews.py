import customtkinter as ctk
import os
import json


class db():
    """access to database"""
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




class Review_gen():
    def __init__(self, id_evento, id_usuario, calificacion, comentario, animo):
        self.id = self.generar_review_id()
        self.id_evento = id_evento # debe obtener el id del evento
        self.id_usuario = id_usuario #debe obtener el id de usuario.
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    def to_dict(self):
        data = db.load_data()
        data[str(self.id)] = {
            'id_evento': self.id_evento,
            'id_usuario': self.id_usuario,
            'calificacion': self.calificacion,
            'comentario': self.comentario,
            'animo': self.animo
        }
        db.save_data(data)

    def generar_review_id(self): #generamos el user id.
        data = db.load_data() #cargamos la base de datos
        if data:
            max_review_id = max(map(int, data.keys())) #si en la db hay una key numeral la pasamos a int para realizarle una suma.
            return str(max_review_id + 1)
        else:
            return "1" #si no existe data usamos esto.

    def crear_review(self):
        self.id_evento = int(self.entry_id_evento.get())
        self.id_usuario = int(self.entry_id_usuario.get())
        self.calificacion = int(self.entry_calificacion.get())
        # que le digas que si te ingresan un 0(o menos) o mas de 5.  Te diga que no son validos.
        self.comentario = self.entry_comentario.get()
        self.animo = self.entry_animo.get() # que solo acepte 3 variables. Triste, Neutral, Feliz.
        
        
    #### Falta la funcion para VER reviews!! que esta funcion cargue rewiews.json y te muestre en pantalla los reviews.





class Review_frame(ctk.CTkScrollableFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        ctk.CTkScrollableFrame.__init__(self, parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback

        # Etiquetas
        label_calificacion = ctk.CTkLabel(self, text='Calificación:')
        label_comentario = ctk.CTkLabel(self, text='Comentario:')
        label_animo = ctk.CTkLabel(self, text='Ánimo:')

        # Campos de entrada
        self.entry_id_evento = ctk.CTkEntry(self)
        self.entry_id_usuario = ctk.CTkEntry(self)
        self.entry_calificacion = ctk.CTkEntry(self)
        self.entry_comentario = ctk.CTkEntry(self)
        self.entry_animo = ctk.CTkEntry(self)

        # Botón para crear la revisión
        boton_crear_review = ctk.CTkButton(self, text='Crear Review', command=lambda: Review_gen().crear_review())
        boton_crear_review.grid(row=6, columnspan=2)
        # Ubicar los elementos en la ventana
        label_calificacion.grid(row=3, column=0)
        label_comentario.grid(row=4, column=0)
        label_animo.grid(row=5, column=0)

        self.entry_calificacion.grid(row=3, column=1)
        self.entry_comentario.grid(row=4, column=1)
        self.entry_animo.grid(row=5, column=1)

        
        
        self.user_id = None

    #actualiza el user_id del frame, al de la ventana maestra.
    def set_user_id(self, user_id):
        self.user_id = user_id

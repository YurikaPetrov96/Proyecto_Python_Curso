import customtkinter
import os
import json

class window(customtkinter.CTk):
    """Ventana principal"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Definimos el tamaño y configuración
        self.title("Reviews")
        window_width = 800
        window_height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight() 
        x_coordinate = ((screen_width - window_width) // 2)
        y_coordinate = ((screen_height - window_height) // 2)
        self.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
        
        # Crear la ventana principal

        # Etiquetas
        label_id_evento = customtkinter.CTkLabel(self, text='ID Evento:')
        label_id_usuario = customtkinter.CTkLabel(self, text='ID Usuario:')
        label_calificacion = customtkinter.CTkLabel(self, text='Calificación:')
        label_comentario = customtkinter.CTkLabel(self, text='Comentario:')
        label_animo = customtkinter.CTkLabel(self, text='Ánimo:')

        # Campos de entrada
        self.entry_id_evento = customtkinter.CTkEntry(self)
        self.entry_id_usuario = customtkinter.CTkEntry(self)
        self.entry_calificacion = customtkinter.CTkEntry(self)
        self.entry_comentario = customtkinter.CTkEntry(self)
        self.entry_animo = customtkinter.CTkEntry(self)

        # Botón para crear la revisión
        self.boton_crear_review = customtkinter.CTkButton(self, text='Crear Review', command= self.crear_review_main)

        # Ubicar los elementos en la ventana
        label_id_evento.grid(row=1, column=0)
        label_id_usuario.grid(row=2, column=0)
        label_calificacion.grid(row=3, column=0)
        label_comentario.grid(row=4, column=0)
        label_animo.grid(row=5, column=0)

        self.entry_id_evento.grid(row=1, column=1)
        self.entry_id_usuario.grid(row=2, column=1)
        self.entry_calificacion.grid(row=3, column=1)
        self.entry_comentario.grid(row=4, column=1)
        self.entry_animo.grid(row=5, column=1)

        self.boton_crear_review.grid(row=6, columnspan=2)
        
        
    def crear_review_main(self):
        id_evento = self.entry_id_evento.get()
        id_usuario = self.entry_id_usuario.get()
        calificacion = self.entry_calificacion.get()
        comentario = self.entry_comentario.get()
        animo = self.entry_animo.get()
        
        while True:
            Review(id_evento, id_usuario, calificacion, comentario, animo).crear_review()
            return False
        
        
    
class db():
    """access to database"""
    
    
    
    @staticmethod
    def save_data(data):
        current_data = db.load_data()
        current_data.update(data)
        with open("data/reviews.json", "w", encoding="utf-8") as file:
            json.dump(data, file)

    @staticmethod
    def load_data(filename):
        folder = "data"
        file_path = os.path.join(folder, filename)
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

class Review():
    def __init__(self, id_evento, id_usuario, calificacion, comentario, animo):
        self.review_id = self.generar_review_id()
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    def crear_review(self):
        data=db.load_data("reviews.json")
        data[str(self.review_id)]={
            'id_evento': self.id_evento,
            'id_usuario': self.load_user_id(),
            'calificacion': self.load_user_id(),
            'comentario': self.comentario,
            'animo': self.animo
        }
        db.save_data(data)
        
    def load_user_id(self):
        file = "users.json"
        data = db.load_data(file)
        for user_id, apellido, nombre in data:
            usr = data[user_id]
            apellido == data["apellido"]
            nombre == data["nombre"]
            

    @classmethod
    def generar_review_id(cls): #generamos el user id.
        data = db.load_data("reviews.json") #caragamos la base de datos
        if data:
            max_review_id = max(map(int, data.keys())) #si en la db hay una key numeral la pasamos a int para realizarle una suma.
            return str(max_review_id + 1)
        else:
            return "1"#si no existe data usamos esto.





if __name__ == "__main__":
    app = window()
    app.mainloop()
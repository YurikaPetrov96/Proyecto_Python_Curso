import tkinter as tk
import json


class db():
    """access to database"""
    @staticmethod
    def save_data(data):
        current_data = db.load_data()
        current_data.update(data)
        with open("data/reviews.json", "w", encoding="utf-8") as file:
            json.dump(data, file)

    @staticmethod
    def load_data():
        try:
            with open("data/reviews.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

class Review():
    def __init__(self, id, id_evento, id_usuario, calificacion, comentario, animo):
        self.id = Review.generar_review_id()
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    def to_dict(self):
        data=db.load_data()
        data[str(review_id)]={
            'id_evento': self.id_evento,
            'id_usuario': self.id_usuario,
            'calificacion': self.calificacion,
            'comentario': self.comentario,
            'animo': self.animo
        }
        db.save_data(data)

    @classmethod
    def generar_review_id(cls): #generamos el user id.
        data = db.load_data() #caragamos la base de datos
        if data:
            max_review_id = max(map(int, data.keys())) #si en la db hay una key numeral la pasamos a int para realizarle una suma.
            return str(max_review_id + 1)
        else:
            return "1"#si no existe data usamos esto.

    def crear_review(self):
        self.id_evento = int(entry_id_evento.get())
        self.id_usuario = int(entry_id_usuario.get())
        self.calificacion = int(entry_calificacion.get())
        self.comentario = entry_comentario.get()
        self.animo = entry_animo.get()


# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Crear Review')

# Etiquetas
label_id_evento = tk.Label(ventana, text='ID Evento:')
label_id_usuario = tk.Label(ventana, text='ID Usuario:')
label_calificacion = tk.Label(ventana, text='Calificación:')
label_comentario = tk.Label(ventana, text='Comentario:')
label_animo = tk.Label(ventana, text='Ánimo:')

# Campos de entrada
entry_id_evento = tk.Entry(ventana)
entry_id_usuario = tk.Entry(ventana)
entry_calificacion = tk.Entry(ventana)
entry_comentario = tk.Entry(ventana)
entry_animo = tk.Entry(ventana)

# Botón para crear la revisión
boton_crear_review = tk.Button(ventana, text='Crear Review', command=Review.crear_review(Review))

# Ubicar los elementos en la ventana
label_id_evento.grid(row=1, column=0)
label_id_usuario.grid(row=2, column=0)
label_calificacion.grid(row=3, column=0)
label_comentario.grid(row=4, column=0)
label_animo.grid(row=5, column=0)

entry_id_evento.grid(row=1, column=1)
entry_id_usuario.grid(row=2, column=1)
entry_calificacion.grid(row=3, column=1)
entry_comentario.grid(row=4, column=1)
entry_animo.grid(row=5, column=1)

boton_crear_review.grid(row=6, columnspan=2)

ventana.mainloop()

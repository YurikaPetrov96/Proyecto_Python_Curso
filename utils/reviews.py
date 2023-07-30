import customtkinter as ctk
from models.users import db

class Review_create(ctk.CTkFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback

        
        for i in range(6):
            self.rowconfigure(i, weight=0)
            self.columnconfigure(i, weight=0)
        
        master_label = ctk.CTkLabel(self, text= "Reviews")
        master_label.grid(0)
        # Etiquetas
        label_id_evento = ctk.CTkLabel(self, text='ID Evento:')
        label_calificacion = ctk.CTkLabel(self, text='Calificación:')
        label_comentario = ctk.CTkLabel(self, text='Comentario:')
        label_animo = ctk.CTkLabel(self, text='Ánimo:')

        # Campos de entrada
        self.entry_id_evento = ctk.CTkEntry(self)
        self.entry_calificacion = ctk.CTkEntry(self)
        self.entry_comentario = ctk.CTkEntry(self)
        self.entry_animo = ctk.CTkEntry(self)

        # Botón para crear la revisión
        boton_crear_review = ctk.CTkButton(self, text='Crear Review', command=lambda: Review_func.crear_review())
        # Ubicar los elementos en la ventana
        label_id_evento.grid(row=1, column=0)
        label_calificacion.grid(row=3, column=0)
        label_comentario.grid(row=4, column=0)
        label_animo.grid(row=5, column=0)

        self.entry_id_evento.grid(row=1, column=1)
        self.entry_calificacion.grid(row=3, column=1)
        self.entry_comentario.grid(row=4, column=1)
        self.entry_animo.grid(row=5, column=1)

        boton_crear_review.grid(row=6, columnspan=2)   
        
        
class Review_show(ctk.CTkFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback

class Review_func():
    def __init__(self, id_evento, id_usuario, apellido, nombre,calificacion, comentario, animo):
        self.id = self.generar_review_id()
        self.id_evento = id_evento
        self.id_usuario = self.user_id_get()
        self.apellido = self.user_info(apellido)
        self.nombre = self.user_info(nombre)
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo
        
        
    def user_id_get(self, user_id):
        self.user_id = user_id
        
    def user_info(self, user_id_got, apellido, nombre):
        data = db.load_data("users.json")
        user_id_got = self.user_id_get()
        for user_id, user_data in data.items():
            if user_id_got == user_id:
                apellido == user_data["apellido"]
                nombre == user_data["nombre"]
                return apellido, nombre
            else:
                return ValueError
            

    def to_dict(self):
        data = db.load_data("reviews.json")
        data[str(self.id)] = {
            'id_evento': self.id_evento,
            'id_usuario': self.id_usuario,
            'apellido': self.apellido,
            'nombre': self.nombre,
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
        self.calificacion = int(self.entry_calificacion.get())
        self.comentario = self.entry_comentario.get()
        self.animo = self.entry_animo.get()

    




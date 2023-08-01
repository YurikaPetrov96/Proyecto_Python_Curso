import customtkinter as ctk
import tkinter as tk
from PIL import Image
from utils.buscador import cargarjson, Buscador, Filtros
from utils.indice_carga_eventos import Evento, Indice

class Frame1(ctk.CTkScrollableFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        for i in range(10):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i, weight=1)
        
        ruta_archivo_json = 'data/basededatos.json'
        eventos = cargarjson(ruta_archivo_json)

        # Instancio filtros
        self.buscador = Buscador(eventos)
        self.filtros = Filtros(eventos)
        
        self.indice = Indice('data/basededatos.json')
        eventos = self.indice.carga()
        
        self.mostrar_eventos()
        
        
    def mostrar_eventos(self):
    # Obtener los eventos desde el índice
        eventos = self.indice.mostrar()

        # Mostrar los eventos
        if eventos:
            row = 0  # Start from row 1 (since row 0 has the image_label)
            for evento in eventos:
                # Create a frame to hold the image and text
                event_frame = tk.Frame(self, bg="#000000")
                event_frame.grid(row=row, column=0, sticky="NEWS")

                # Load the image for the event
                imagen_evento = evento['imagen']

                # Convert the image to PhotoImage (required for CTkLabel)
                image_evento_ctk = ctk.CTkImage(dark_image=Image.open(imagen_evento), size=(100, 200))

                # Create the label for the image
                image_label = ctk.CTkLabel(event_frame, image=image_evento_ctk, bg_color="transparent", fg_color="transparent")
                image_label.grid(row=0, column=0, padx=10, pady=10)

                # Update the event details in the label text
                evento_text = (
                    f"Evento N°: {evento['indice']}\n"
                    f"Nombre: {evento['nombre']}\n"
                    f"Artista: {evento['artista']}\n"
                    f"Género: {evento['genero']}\n"
                    f"Ubicación: {evento['ubicacion']}\n"
                    f"Horario de inicio: {evento['horario_ini']}\n"
                    f"Horario de finalización: {evento['horario_fin']}\n"
                    f"Descripción: {evento['descripcion']}\n"
                    f"Fecha: {evento['fecha']}\n"
                    f"Provincia: {evento['provincia']}\n"
                )

                # Create the label for the text
                text_label = ctk.CTkLabel(event_frame, text=evento_text, bg_color="transparent", fg_color="transparent", text_color="green", anchor="w")
                text_label.grid(row=0, column=1, padx=10, pady=10, sticky="W")

                row += 1





class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Definimos el tamaño y configuración
        ctk.set_default_color_theme("data/cimne_theme.json")
        self.title("Test")
        window_width = 800
        window_height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight() 
        x_coordinate = ((screen_width - window_width) // 2)
        y_coordinate = ((screen_height - window_height) // 2)
        self.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        frame1 = Frame1(self)
        frame1.grid(row=0, column=0, sticky="NEWS")


if __name__ == "__main__":
    app = App()
    app.mainloop()
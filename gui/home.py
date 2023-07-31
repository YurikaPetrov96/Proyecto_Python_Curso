import customtkinter
from models.users import db
from utils.Indice_carga_eventos import Evento, Indice

class Indice_gui(customtkinter.CTkFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        from utils.buscador import Buscador, Filtros, cargarjson
        
        #configuración de las lineas
        for i in range(0,6):
            self.grid_rowconfigure(i, weight=0)
        self.grid_rowconfigure(7, weight=1)
        
        #configuracion de las columnas
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        self.grid_columnconfigure(4, weight= 2)
        self.grid_columnconfigure(5, weight= 1)
        self.grid_columnconfigure(6, weight= 0)
        
        #labels
        label0 = customtkinter.CTkLabel(self, text="Buscar:", font=("", 15, "bold"))
        label0.grid(row=0, column= 4, sticky= "ne")
        self.label3 = customtkinter.CTkLabel(self, text="", font=("", 12))
        self.label3.grid(row=3, column=5, columnspan= 2, sticky= "news")
        
        #entries
        self.entry0 = customtkinter.CTkEntry(self)
        self.entry0.grid(row=0, column=5, sticky="nwe", padx=5)
        
        
        
        
        #botones
        button1 = customtkinter.CTkButton(self, text="Buscar", command= self.show_search)
        button1.grid(row=0, column=6, sticky="NE")

        button2 = customtkinter.CTkButton(self, text="Agregar Evento", command=self.ventana_agregar)
        button2.grid(row=1, column=4, sticky="NE")

        #Radio buttons para el filtro
        self.filtro_seleccionado = customtkinter.StringVar()
        radio_btn1 = customtkinter.CTkRadioButton(self, text="Filtro por Nombre", variable=self.filtro_seleccionado, value="nombre")
        radio_btn1.grid(row=1, column=6, padx=5, pady=5, sticky="w")

        radio_btn2 = customtkinter.CTkRadioButton(self, text="Filtro por Género", variable=self.filtro_seleccionado, value="genero")
        radio_btn2.grid(row=2, column=6, padx=5, pady=5, sticky="w")

        radio_btn3 = customtkinter.CTkRadioButton(self, text="Filtro por Artista", variable=self.filtro_seleccionado, value="artista")
        radio_btn3.grid(row=3, column=6, padx=5, pady=5, sticky="w")

        radio_btn4 = customtkinter.CTkRadioButton(self, text="Filtro por Ubicación", variable=self.filtro_seleccionado, value="ubicacion")
        radio_btn4.grid(row=4, column=6, padx=5, pady=5, sticky="w")

        radio_btn5 = customtkinter.CTkRadioButton(self, text="Filtro por Horario", variable=self.filtro_seleccionado, value="horario")
        radio_btn5.grid(row=5, column=6, padx=5, pady=5, sticky="w")
        
        
        #boxes
        self.boxbox1 = customtkinter.CTkTextbox(self, width= 500, corner_radius=0)
        self.boxbox1.configure(state="disabled")
        self.boxbox1.grid(row=0, column=0, rowspan=7, columnspan=4, padx= 5, pady=5)
        

        #Carga de archivo json
        ruta_archivo_json = 'data/basededatos.json'
        eventos = cargarjson(ruta_archivo_json)

        # Instancia de filtros
        self.buscador = Buscador(eventos)
        self.filtros = Filtros(eventos)

        # Instancia de Indice
        self.indice = Indice('data/basededatos.json')
        eventos = self.indice.carga()
        
        # Inicio de agregar las fincionalidades del indice a la aplicacion
        self.mostrar_eventos()
    
        
        # Muestra los eventos constantemente en el textbox
    def mostrar_eventos(self):
        # Obtener los eventos desde el índice
        eventos = self.indice.mostrar()

        # Mostrar los eventos en el TextBox1
        self.boxbox1.configure(state="normal")
        self.boxbox1.delete('1.0', 'end')
        if eventos:
            for evento in eventos:
                evento_str = (
                    f"Evento N°: {evento['indice']}\n"
                    f"Nombre: {evento['nombre']}\n"
                    f"Artista: {evento['artista']}\n"
                    f"Género: {evento['genero']}\n"
                    f"Ubicación: {evento['ubicacion']}\n"
                    f"Horario de inicio: {evento['horario_ini']}\n"
                    f"Horario de finalización: {evento['horario_fin']}\n"
                    f"Descripción: {evento['descripcion']}\n"
                    f"Imagen: {evento['imagen']}\n"
                    f"Fecha: {evento['fecha']}\n"
                    f"Provincia: {evento['provincia']}\n\n"
                )
                self.boxbox1.insert("end", evento_str)
        else:
            self.boxbox1.insert("end", "No hay eventos registrados.\n")
        self.boxbox1.configure(state="disabled")

    # Crea una nueva ventana TopLevel para agregar evento
    def ventana_agregar(self):
        self.ventana_agregar = customtkinter.CTkToplevel(self)
        self.ventana_agregar.title("Agregar Evento")
        self.ventana_agregar.resizable(False, False)

        # Label y entry de la ventana top level
        label_nombre = customtkinter.CTkLabel(self.ventana_agregar, text="Nombre del evento:")
        label_nombre.grid(row=0, column=0, padx=5, pady=5)
        self.entry_nombre = customtkinter.CTkEntry(self.ventana_agregar)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        label_artista = customtkinter.CTkLabel(self.ventana_agregar, text="Nombre del artista:")
        label_artista.grid(row=2, column=0, padx=5, pady=5)
        self.entry_artista = customtkinter.CTkEntry(self.ventana_agregar)
        self.entry_artista.grid(row=2, column=1, padx=5, pady=5)

        label_genero = customtkinter.CTkLabel(self.ventana_agregar, text="Genero musical:")
        label_genero.grid(row=3, column=0, padx=5, pady=5)
        self.entry_genero = customtkinter.CTkEntry(self.ventana_agregar)
        self.entry_genero.grid(row=3, column=1, padx=5, pady=5)

        label_ubicacion = customtkinter.CTkLabel(self.ventana_agregar, text="Ubicaccion del evento:")
        label_ubicacion.grid(row=4, column=0, padx=5, pady=5)
        self.entry_ubicacion = customtkinter.CTkEntry(self.ventana_agregar)
        self.entry_ubicacion.grid(row=4, column=1, padx=5, pady=5)

        label_horario_ini = customtkinter.CTkLabel(self.ventana_agregar, text="Horario de inicio:")
        label_horario_ini.grid(row=5, column=0, padx=5, pady=5)
        self.entry_horario_ini = customtkinter.CTkEntry(self.ventana_agregar)
        self.entry_horario_ini.grid(row=5, column=1, padx=5, pady=5)

        label_horario_fin = customtkinter.CTkLabel(self.ventana_agregar, text="Horario de finalizacion:")
        label_horario_fin.grid(row=6, column=0, padx=5, pady=5)
        self.entry_horario_fin = customtkinter.CTkEntry(self.ventana_agregar)
        self.entry_horario_fin.grid(row=6, column=1, padx=5, pady=5)

        label_descripcion = customtkinter.CTkLabel(self.ventana_agregar, text="Descripcion del evento:")
        label_descripcion.grid(row=7, column=0, padx=5, pady=5)
        self.entry_descripcion = customtkinter.CTkEntry(self.ventana_agregar)
        self.entry_descripcion.grid(row=7, column=1, padx=5, pady=5)

        label_imagen = customtkinter.CTkLabel(self.ventana_agregar, text="Imagen del evento:")
        label_imagen.grid(row=8, column=0, padx=5, pady=5)
        self.entry_imagen = customtkinter.CTkEntry(self.ventana_agregar)
        self.entry_imagen.grid(row=8, column=1, padx=5, pady=5)

        label_fecha = customtkinter.CTkLabel(self.ventana_agregar, text="Fecha del evento:")
        label_fecha.grid(row=9, column=0, padx=5, pady=5)
        self.entry_fecha = customtkinter.CTkEntry(self.ventana_agregar)
        self.entry_fecha.grid(row=9, column=1, padx=5, pady=5)

        label_provincia = customtkinter.CTkLabel(self.ventana_agregar, text="Provincia del evento:")
        label_provincia.grid(row=10, column=0, padx=5, pady=5)
        self.entry_provincia = customtkinter.CTkEntry(self.ventana_agregar)
        self.entry_provincia.grid(row=10, column=1, padx=5, pady=5)
        
         # Botón guardar de la ventana top level
        boton_guardar = customtkinter.CTkButton(self.ventana_agregar, text="Guardar", command=self.guardar_evento)
        boton_guardar.grid(row=11, column=0, padx=5, pady=5)

    def guardar_evento(self):
        nombre = self.entry_nombre.get()
        artista = self.entry_artista.get()
        genero = self.entry_genero.get()
        ubicacion = self.entry_ubicacion.get()
        horario_ini = self.entry_horario_ini.get()
        horario_fin = self.entry_horario_fin.get()
        descripcion = self.entry_descripcion.get()
        imagen = self.entry_imagen.get()
        fecha = self.entry_fecha.get()
        provincia = self.entry_provincia.get()

        nuevo_evento = Evento(nombre, artista, genero, ubicacion, horario_ini, horario_fin, descripcion, imagen, fecha, provincia)
        self.indice.agregar(nuevo_evento)
        self.ventana_agregar.destroy()
    
    def show_history():
        pass
    
    def show_search(self):
        """Para mostrar lo que se requiera en el buscador"""
        busqueda = self.entry0.get().strip()
        filtro_seleccionado = self.filtro_seleccionado.get()
        if not busqueda and not filtro_seleccionado:
            self.mostrar_eventos()
            return
        resultados = []
        if not filtro_seleccionado:
            resultados = self.buscador.buscar_por_palabra(busqueda)
        else:
            if filtro_seleccionado == "nombre":
                resultados = self.filtros.por_nombre(busqueda)
            elif filtro_seleccionado == "genero":
                resultados = self.filtros.por_genero(busqueda)
            elif filtro_seleccionado == "artista":
                resultados = self.filtros.por_artista(busqueda)
            elif filtro_seleccionado == "ubicacion":
                resultados = self.filtros.por_ubicacion(busqueda)
            elif filtro_seleccionado == "horario":
                resultados = self.filtros.por_horario(busqueda)

        #TextBox Buscador
        self.boxbox1.configure(state="normal")
        self.boxbox1.delete('1.0', 'end')
        if resultados:
            for evento in resultados:
                self.boxbox1.insert("end", str(evento) + "\n")
        else:
            self.boxbox1.insert("end", "No se encontraron resultados\n")
        self.boxbox1.configure(state="disabled")

    
    def destroy_indice_frame(self):
        # Clear the contents of the frame
        for widget in self.winfo_children():
            widget.destroy()    
        
class Mapa(customtkinter.CTkFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        self.current_frame = None
        
        for i in range(5):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i, weight=1)
            
        self.grid_columnconfigure(6, weight=0)
        self.grid_columnconfigure(7, weight=0)
        self.grid_columnconfigure(8, weight=0)
        self.grid_rowconfigure(6, weight=0)
            
        print(f"{self.master.user_id}")
        
    


        
        
        
    def reviews_view(self):
        data = db.load_data("users.json")
        user_token = str(self.master.user_id)
        for user_id, user_data in data.items():
            if user_id == user_token:
                apellido = user_data["apellido"]
                nombre = user_data["nombre"]
                return f"Este review fue realizado por {user_id, apellido, nombre}"
        # Return a default message if no match is found
        return "Este usuario no tiene reviews o no existe en la base de datos."
    
        
        

class Home(customtkinter.CTkScrollableFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        customtkinter.CTkScrollableFrame.__init__(self, parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        self.current_frame = None
        
        #configuracion de columnas
        
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=2)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)
        self.grid_columnconfigure(3, weight=1)
            
        #labels
        
        #botones
        button1 = customtkinter.CTkButton(self, text="Pagina Principal", font=("ROBOTO", 14), command= self.go_main_frame)
        button1.grid(row=0, column= 1, sticky ="ne", padx=5, ipadx=20)
        button2 = customtkinter.CTkButton(self, text="Mapa y Reviews", font=("ROBOTO", 14), command= self.go_map)
        button2.grid(row=0, column= 2, sticky="n", padx=5, ipadx=20)
        log_out_button = customtkinter.CTkButton(self, text="Cerrar Sesion", command= self.cerrar_sesion)
        log_out_button.grid(row=0, column= 4, sticky = "ne")
        
        placeholder_label = customtkinter.CTkLabel(self, text = "")
        placeholder_label.grid(row=1, column= 0, columnspan=4)
        
        
        #le entrega un valor de user_id al frme actual
        self.user_id = None


    #actualiza el user_id del frame, al de la ventana maestra.
    def set_user_id(self, user_id):
        self.user_id = user_id

        
    def show_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.grid_forget()  # Oculta el frame actual si hay alguno.
        self.current_frame = frame_class(self, self.switch_frame_callback)
        self.current_frame.grid(row=2, column=0, columnspan=5, sticky="nsew")
    
    
    def go_main_frame(self):
        if self.current_frame and isinstance(self.current_frame, Mapa):
            self.current_frame.destroy()
        self.show_frame(Indice_gui)
        
            
    def go_map(self):
        self.show_frame(Mapa)
            
    def cerrar_sesion(self):
        self.master.user_id = None
        self.switch_frame_callback("Start_page")
        

        
        
             
    
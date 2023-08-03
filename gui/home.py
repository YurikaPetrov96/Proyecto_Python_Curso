import customtkinter
from models.users import db
from utils.indice_carga_eventos import Evento, Indice

class Indice_gui(customtkinter.CTkFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        from utils.buscador import Buscador, Filtros, cargarjson
        
        #configuración de las lineas
        for i in range(0,6):
            self.grid_rowconfigure(i, weight=0)
        self.grid_rowconfigure(7, weight=1)
        self.grid_rowconfigure(8, weight=1)
        
        #configuracion de las columnas
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        self.grid_columnconfigure(4, weight= 2)
        self.grid_columnconfigure(5, weight= 0)
        self.grid_columnconfigure(6, weight= 1)
        self.grid_columnconfigure(7, weight= 0)
        
        self.event_frames = []
        
        #labels
        placerholder_label = customtkinter.CTkLabel(self, text="")
        placerholder_label.grid(row=0, column=5, rowspan= 7, sticky="w")
        label0 = customtkinter.CTkLabel(self, text="Buscar:", font=("", 15, "bold"))
        label0.grid(row=0, column= 5, sticky= "ne")
        
        #entries
        self.entry0 = customtkinter.CTkEntry(self)
        self.entry0.grid(row=0, column=6, sticky="nwe", padx=5)
        
        
        #botones
        button1 = customtkinter.CTkButton(self, text="Buscar", command= self.show_search)
        button1.grid(row=0, column=7, sticky="NE")
        
        button2 = customtkinter.CTkButton(self, text="Agregar Evento", command=self.ventana_agregar)
        button2.grid(row=6, column=7, sticky="NE")

        #Radio buttons para el filtro
        self.filtro_seleccionado = customtkinter.StringVar()
        radio_btn1 = customtkinter.CTkRadioButton(self, text="Filtro por Nombre", variable=self.filtro_seleccionado, value="nombre")
        radio_btn1.grid(row=1, column=7, padx=5, pady=5, sticky="w")

        radio_btn2 = customtkinter.CTkRadioButton(self, text="Filtro por Género", variable=self.filtro_seleccionado, value="genero")
        radio_btn2.grid(row=2, column=7, padx=5, pady=5, sticky="w")

        radio_btn3 = customtkinter.CTkRadioButton(self, text="Filtro por Artista", variable=self.filtro_seleccionado, value="artista")
        radio_btn3.grid(row=3, column=7, padx=5, pady=5, sticky="w")

        radio_btn4 = customtkinter.CTkRadioButton(self, text="Filtro por Ubicación", variable=self.filtro_seleccionado, value="ubicacion")
        radio_btn4.grid(row=4, column=7, padx=5, pady=5, sticky="w")

        radio_btn5 = customtkinter.CTkRadioButton(self, text="Filtro por Horario", variable=self.filtro_seleccionado, value="horario")
        radio_btn5.grid(row=5, column=7, padx=5, pady=5, sticky="w")
        
        

        #Cargo archivo json
        ruta_archivo_json = 'data/basededatos.json'
        eventos = cargarjson(ruta_archivo_json)

        # Instancio filtros
        self.buscador = Buscador(eventos)
        self.filtros = Filtros(eventos)


        # Instancia de Indice
        self.indice = Indice('data/basededatos.json')
        eventos = self.indice.carga()

        #Frame resultados
        self.frame_resultados = customtkinter.CTkFrame(self)
        self.frame_resultados.grid(row=1, column=0, sticky="NEWS")

        # Almacenar el frame resultados
        self.resultados_frame = None
        
        # Muestra los eventos almacenados en basededatos.json
        self.abrir_main_frame()

        
    
    
    # Muestra los eventos constantemente en el textbox
    def mostrar_eventos(self):
    # Obtener los eventos desde el índice
        from PIL import Image
        eventos = self.indice.mostrar()

        # Mostrar los eventos
        if eventos:
            row = 0
            self.event_frames = []
            main_frame = customtkinter.CTkScrollableFrame(self, height= 800)
            main_frame.grid(row=1, rowspan=7, column=0, columnspan=5, sticky="news")
            
            for evento in eventos:
                # creamos un frame que integra dentro de si los frame labels.
                
                event_frame = customtkinter.CTkFrame(main_frame)
                event_frame.grid(row=row, column=0, sticky="NEWS")

                # Cargamos la imagen del evento
                imagen_evento = evento['imagen']

                # Convertimos a la imagen en PhotoImage
                image_evento_ctk = customtkinter.CTkImage(dark_image=Image.open(imagen_evento), size=(100, 200))

                # Creamos el label para las imagenes
                image_label = customtkinter.CTkLabel(event_frame, image=image_evento_ctk, text="")
                image_label.grid(row=0, column=0, padx=10, pady=10)

                # Actualizamos los detalles de los eventos
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

                # creamos el Label para el texto.
                text_label = customtkinter.CTkLabel(event_frame, text=evento_text, anchor="w")
                text_label.grid(row=0, column=1, padx=10, pady=10, sticky="W")

                row += 1
                self.event_frames.append(event_frame)

    
    def abrir_main_frame(self):
        # Limpia y muestra los eventos en el main frame
        self.limpiar_resultados()
        self.mostrar_eventos()
    
    
    def limpiar_resultados(self):
        for widget in self.frame_resultados.winfo_children():
            widget.destroy()


    def crear_resultados_frame(self):
        if self.resultados_frame:
            self.resultados_frame.destroy()

        self.resultados_frame = customtkinter.CTkScrollableFrame(self, height=800)
        self.resultados_frame.grid(row=1, rowspan=7, column=0, columnspan=5, sticky="news")

    
                
                
    def show_search(self):
        """Para mostrar lo que se requiera en el buscador"""
        busqueda = self.entry0.get()
        filtro_seleccionado = self.filtro_seleccionado.get()
        if not busqueda and not filtro_seleccionado:
            return self.mostrar_eventos()
        else:
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
            self.crear_resultados_frame()
            cont = 1
            for evento in resultados:
                evento_str = str(evento)
                label_evento = customtkinter.CTkLabel(self.resultados_frame, text=evento_str, anchor="w")
                label_evento.grid(row=cont, column=0, sticky="NEWS")
                cont += 1


        
    def ventana_agregar(self):
        # Crea una nueva ventana TopLevel para agregar evento
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
    

    
        
class Mapa(customtkinter.CTkFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        self.current_frame = None
        
        from gui.mapa import Mapa
        from utils.reviews import Review_frame
        
        for i in range(5):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i, weight=1)
            
        mapa_frame = Mapa(self, switch_frame_callback)
        mapa_frame.grid(row=0, column=0, rowspan=5, columnspan=5, sticky="news")
        
        
        

class Home(customtkinter.CTkFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
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
        button1 = customtkinter.CTkButton(self, text="Pagina Principal", command= self.go_main_frame)
        button1.grid(row=0, column= 1, sticky ="ne", padx=5, ipadx=20)
        button2 = customtkinter.CTkButton(self, text="Mapa y Reviews", command= self.go_map)
        button2.grid(row=0, column= 2, sticky="n", padx=5, ipadx=20)
        log_out_button = customtkinter.CTkButton(self, text="Cerrar Sesion", command= self.cerrar_sesion)
        log_out_button.grid(row=0, column= 4, sticky = "ne")
        
        placeholder_label = customtkinter.CTkLabel(self, text = "")
        placeholder_label.grid(row=1, column= 0, columnspan=4)
        
        
        #le entrega un valor de user_id al frame actual
        self.user_id = None
        
        ###
        self.show_frame(Indice_gui)

    #actualiza el user_id del frame, al de la ventana maestra.
    def set_user_id(self, user_id):
        self.user_id = self.master.user_id
        print(self.user_id)

        
    def show_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.grid_forget()  # Oculta el frame actual si hay alguno.
        self.current_frame = frame_class(self, self.switch_frame_callback)
        self.current_frame.grid(row=2, column=0, columnspan=5, sticky="nsew")
    
    
    def go_main_frame(self):
        self.show_frame(Indice_gui)
        
            
    def go_map(self):
        self.show_frame(Mapa)
            
    def cerrar_sesion(self):
        self.master.user_id = None
        self.switch_frame_callback("Start_page")
import tkinter as tk
import customtkinter as ctk
import os.path
import math
import json
import random
from PIL import Image, ImageTk
from tkintermapview import TkinterMapView
from datetime import datetime

ctk.set_default_color_theme("blue")

class App(ctk.CTk):

    APP_NAME = "Salta (Capital) Argentina  - Tour Musical -"
    WIDTH = 800
    HEIGHT = 600
    markers = {}
    list_text = []
    global_market =""
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)

        self.marker_list = []
        
        # ============ create two CTkFrames ============

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = ctk.CTkFrame(master=self, width=150, corner_radius=0, fg_color=None)
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.frame_right = ctk.CTkFrame(master=self, corner_radius=0)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")

        # ============ frame_left ============

        self.frame_left.grid_rowconfigure(8, weight=1)

        self.map_label = ctk.CTkLabel(self.frame_left, text="♬🎵 Eventos 🎵♬", anchor="w")
        self.map_label.grid(row=0, column=0, padx=(1, 20), pady=(10, 0))

        self.button_1 = ctk.CTkButton(master=self.frame_left,
                                                text="Agregar",
                                                command = lambda: self.set_option("Si"))
        self.button_1.grid(pady=(5, 0), padx=(20, 20), row=1, column=0)

        self.button_2 = ctk.CTkButton(master=self.frame_left,
                                                text="Borrar",
                                                command = lambda: self.set_option("No"))
        self.button_2.grid(pady=(5, 0), padx=(20, 20), row=2, column=0)
        
        self.listbox = tk.Listbox(master=self.frame_left, selectforeground = "#ffffff",
                            selectbackground = "#00aa00",
                            selectborderwidth = 3, height = 10, cursor = "heart #ff0000")

                        # Agregar los elementos a la lista
                        #scrollbar = ttk.Scrollbar(listbox, orient = tkinter.VERTICAL)
                        #listbox = tk.Listbox(self.frame_left, yscrollcommand = scrollbar.set)
                        #scrollbar.config(command = listbox.yview)
                        # Ubicarla a la derecha.
                        #scrollbar.pack(side=tkinter.RIGHT, fill = tkinter.Y)
        
        for elemento in self.list_text:
            self.listbox.insert(tk.END, elemento)
                        # Empaquetar la lista en la ventana
                        #listbox.grid_remove()
                        #frame.pack()
        self.listbox.grid(pady=(5, 0), padx=(1, 1),row=3, column=0)

        self.map_label = ctk.CTkLabel(self.frame_left, text="Rutas:", anchor="w")
        self.map_label.grid(row=4, column=0, padx=(5, 20), pady=(5, 0))
        
        self.button_6 = ctk.CTkButton(master=self.frame_left,
                                                text="Dibujar",
                                                command = self.createRutEvent)
        self.button_6.grid(pady=(5, 0), padx=(20, 20), row=5, column=0)

        self.button_7 = ctk.CTkButton(master=self.frame_left,
                                                text="Borrar",
                                                command = self.delRuta)
        self.button_7.grid(pady=(5, 0), padx=(20, 20), row=6, column=0)

        self.button_3 = ctk.CTkButton(master=self.frame_left,
                                                text="Guardar",
                                                command=self.guardar_RutaVisita)
        self.button_3.grid(pady=(20, 0), padx=(20, 20), row=7, column=0)

        self.map_label = ctk.CTkLabel(self.frame_left, text="Modos:", anchor="w")
        self.map_label.grid(row=9, column=0, padx=(20, 20), pady=(20, 0))

        self.map_option_menu = ctk.CTkOptionMenu(self.frame_left, values=["OpenStreetMap", "Google normal", "Google satellite"],
                                                                       command=self.change_map)
        self.map_option_menu.grid(row=10, column=0, padx=(20, 20), pady=(10, 0))

        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.frame_left, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode)
        self.appearance_mode_optionemenu.grid(row=11, column=0, padx=(20, 20), pady=(10, 20))

        # ============ frame_right ============

        self.frame_right.grid_rowconfigure(0, weight=0)
        self.frame_right.grid_rowconfigure(1, weight=1)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)

        self.map_widget = TkinterMapView(self.frame_right, corner_radius=0)
        self.map_widget.grid(row=1, rowspan=1, column=0, columnspan=6, sticky="nswe", padx=(0, 0), pady=(0, 0))

        #self.entry = customtkinter.CTkEntry(master=self.frame_right,
         #                                   placeholder_text="type address")
        #self.entry.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)
        #self.entry.bind("<Return>", self.search_event)
       
        self.labelEvent = ctk.CTkLabel(self.frame_right, text = "", anchor = "w", 
                                       fg_color = "#ffffff", justify = "center", compound= "center")
        self.labelEvent.grid(row = 0, column = 0, sticky = "we", padx=(12, 0), pady = 12)

        self.button_5 = ctk.CTkButton(master = self.frame_right,
                                                text="Cartelera",
                                                width = 90,
                                                command=self.info_evento)
        self.button_5.grid(row = 0, column = 1, sticky = "w", padx = (12, 0), pady = 12)

        self.button_9 = ctk.CTkButton(master = self.frame_right,
                                                text="Review",
                                                width = 90,
                                                command=self.review)
        self.button_9.grid(row = 0, column = 2, sticky = "w", padx = (12, 0), pady = 12)
        
        self.radio_var = tk.IntVar(value=0)
        self.radio_1 = ctk.CTkRadioButton(master=self.frame_right, text="★", text_color="yellow", border_color= "yellow",command=self.radio_event, variable=self.radio_var, value=1)
        self.radio_2 = ctk.CTkRadioButton(master=self.frame_right, text="★★",text_color="yellow",border_color= "yellow", command=self.radio_event, variable=self.radio_var, value=2)
        self.radio_3 = ctk.CTkRadioButton(master=self.frame_right, text="★★★",text_color="yellow",border_color= "yellow", command=self.radio_event, variable=self.radio_var, value=3)        
        self.radio_1.grid(row = 0, column = 3, sticky = "w", padx = (12, 0), pady = 12)
        self.radio_2.grid(row = 0, column = 4, sticky = "w", padx = (12, 0), pady = 12)
        self.radio_3.grid(row = 0, column = 5, sticky = "w", padx = (12, 0), pady = 12)
        # ==================== Set Usuario ======================
        pos1 = -24.7868489
        pos2 = -65.4120303
        self.nombreUsuario = "Facundo Ovejero"

        usuario_image = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                            "images", "usuario1.jpg")).resize((100, 100)))
        
        #usuario_icono = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"images", "usuario1.jpg")).resize((35, 35)))
        
        self.marker_0 = self.map_widget.set_marker(pos1, pos2, text = self.nombreUsuario, image = usuario_image,
                                                    image_zoom_visibility = (14, float("inf"))
                                                    , command = self.click_usuario)
        
        self.marker_0.hide_image(True)  # hide image
        self.marker_0.set_text(self.nombreUsuario)
        self.marker_0.marker_color_circle = "#006400"
        self.marker_0.marker_color_outside = "#00FF00"
        self.marker_0.text_color = "#006400"

        self.marcaPos = []
        self.marcaPos += (self.marker_0.position,)

        # Set Evento
        # ------------------------------EVENTOS-------------------------------------------------------------
        # set current widget position by address
        # Cargar de un json las cordenadas de los Eventos
        # Se cargan las imagenes

        self.diccionario = {"marker_1": {"position": (-24.7825492, -65.4167884), "text": "MUSIC Festival",    "image": "image3.jpg", "calificacion":"★★★"},
                    "marker_2": {"position": (-24.7854359, -65.41249414),"text": "Music Nostalgia",   "image": "image4.jpg", "calificacion":"★★"},
                    "marker_3": {"position": (-24.7830168, -65.4110807), "text": "Music Folklore",    "image": "image5.jpg", "calificacion":"★"},
                    "marker_4": {"position": (-24.7895177, -65.4180384), "text": "DJ Gloria",         "image": "image7.jpg", "calificacion":"★★"},
                    "marker_5": {"position": (-24.7887507, -65.4070912), "text": "Charanga Habanera", "image": "image8.jpeg","calificacion":""},
                    }

        numero1=list(range(13))
        numero2=list(range(13))
        imagen=list(range(13))
        for i in range(13):
            numero1[i] = random.uniform(-24.7463100, -24.8386949)
            #numero_redondeado = round(numero1[i], 7)
            numero2[i] = random.uniform(-65.3749002, -65.4775537)
            #numero_redondeado = round(numero2[i], 7)
            ign=9+i
            imagen[i]= "image"+str(ign)+".jpg"
            key="marker_"+str(i+5)
            agregar={key:{"position": (numero1[i], numero2[i]), "text": "Nuevo aleatorio", "image": imagen[i] ,"calificacion":""}}                                                                                                                       
            self.diccionario.update(agregar)

        evento_images = {}
        self.markers = {}
        marcaPos = []
        marcaPos += (self.marker_0.position,)
        
        for key in self.diccionario:
            image_name = self.diccionario[key]["image"]
            positions1 = self.diccionario[key]["position"][0]
            positions2 = self.diccionario[key]["position"][1]
            texts = self.diccionario[key]["text"] + self.diccionario[key]["calificacion"]
            evento_images[key] = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                                            "images", image_name)).resize((250,200)))
            self.markers[key] = self.map_widget.set_marker(positions1,positions2, text=texts, image=evento_images[key],
                                        image_zoom_visibility=(0, float("inf")), command=self.click_usuario)
            self.markers[key].hide_image(True)  
            self.markers[key].set_text(texts)
            if len(self.diccionario[key]["calificacion"]) == 0:
                self.markers[key].text_color="black"
                self.markers[key].marker_color_circle = "orange"
            else:
                self.markers[key].marker_color_circle = "red"
    
        # =======================Set default values=========================
        #self.map_widget.set_address("Salta Capital, Argentina")

        self.map_widget.set_position(pos1,pos2)  # Salta Usuario
        self.map_widget.set_zoom(16)
        self.map_option_menu.set("OpenStreetMap")
        self.appearance_mode_optionemenu.set("Dark")
        self.map_widget.add_right_click_menu_command(label="Marcar Ruta",
                                        command=self.add_ruta_event,
                                        pass_coords=True)

    # ================== ========METODOS ====================================
    def crear_evento(self):

        self.diccionario = {}
        self.diccionario = {"marker_1": {"position": (-24.7825492, -65.4167884), "text": "MUSIC Festival",    "image": "image3.jpg", "calificacion":"★★★"},
                    "marker_2": {"position": (-24.7854359, -65.41249414),"text": "Music Nostalgia",   "image": "image4.jpg", "calificacion":"★★"},
                    "marker_3": {"position": (-24.7830168, -65.4110807), "text": "Music Folklore",    "image": "image5.jpg", "calificacion":"★"},
                    "marker_4": {"position": (-24.7895177, -65.4180384), "text": "DJ Gloria",         "image": "image7.jpg", "calificacion":"★★"},
                    "marker_5": {"position": (-24.7887507, -65.4070912), "text": "Charanga Habanera", "image": "image8.jpeg","calificacion":""},
                    }

        numero1=list(range(13))
        numero2=list(range(13))
        imagen=list(range(13))
        for i in range(13):
            numero1[i] = random.uniform(-24.7463100, -24.8386949)
            #numero_redondeado = round(numero1[i], 7)
            numero2[i] = random.uniform(-65.3749002, -65.4775537)
            #numero_redondeado = round(numero2[i], 7)
            ign=9+i
            imagen[i]= "image"+str(ign)+".jpg"
            key="marker_"+str(i+5)
            agregar={key:{"position": (numero1[i], numero2[i]), "text": "Nuevo aleatorio", "image": imagen[i] ,"calificacion":""}}                                                                                                                       
            self.diccionario.update(agregar)

        evento_images = {}
        self.markers = {}
        marcaPos = []
        marcaPos += (self.marker_0.position,)
        
        for key in self.diccionario:
            image_name = self.diccionario[key]["image"]
            positions1 = self.diccionario[key]["position"][0]
            positions2 = self.diccionario[key]["position"][1]
            texts = self.diccionario[key]["text"] + self.diccionario[key]["calificacion"]
            evento_images[key] = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                                            "images", image_name)).resize((250,200)))
            self.markers[key] = self.map_widget.set_marker(positions1,positions2, text=texts, image=evento_images[key],
                                        image_zoom_visibility=(0, float("inf")), command=self.click_usuario)
            self.markers[key].hide_image(True)  
            self.markers[key].set_text(texts)
            if len(self.diccionario[key]["calificacion"]) == 0:
                self.markers[key].text_color="black"
                self.markers[key].marker_color_circle = "orange"
            else:
                self.markers[key].marker_color_circle = "red"


    def radio_event(self):
        print("Radio button cambiado, valor actual:", self.radio_var.get())
        #self.crear_evento()
        for k in self.diccionario:
            text = len(self.diccionario[k]["calificacion"])
            if text == self.radio_var.get():
                print("Filtrado")
            else:    
                self.markers[k].delete()

    def click_usuario(self, marker):
        # d8 Click mouse izq. Marca un evento y desmarca un evento mostrando Imagen
        print("marker clicked:",marker.text)
        self.global_market = marker.text
        self.labelEvent.configure(text="  "+self.global_market)

        if marker.image_hidden is True:
            for key in self.diccionario:
                self.markers[key].hide_image(True) 
                #self.markers[key].marker_color_circle = "red" # <<<<<< no cambia de color
            marker.hide_image(False)
        else:
            marker.hide_image(True)
        #self.marker.marker_color_circle = "green" 

    def set_option(self,value):
        # d6 Opciones de los botones Agregar y Borrar de la lista de Eventos para crear Ruta

        if self.nombreUsuario == self.global_market:
            return

        global option
        option = value

        if option == "Si" and len(self.global_market) > 0 and self.global_market not in self.list_text:
            print("Guardado")
            print(self.global_market)
            self.list_text.append(self.global_market)
            print(self.list_text) 
            self.listbox.insert(tk.END, self.global_market)

            for k, v in self.diccionario.items():

                    if str(v["text"] + v["calificacion"])== self.global_market:
                        clave =  k
                        posicion=list(self.diccionario.keys()).index(clave)
                        print(f"La clave {clave} se encuentra en la posición {posicion}.")    
                        #self.markers[clave].marker_color_circle = "green"       
                        break

        if option == "No" and len(self.list_text) > 0 and self.global_market in self.list_text:
            print("Borrado")
            self.list_text.remove(self.global_market)
            print(self.list_text)
            self.listbox.delete(self.listbox.get(0, tk.END).index(self.global_market))

        option = ""

 #************************************************************************************************


 #************************************************************************************************
    def review(self):
        # d6.5 Boron de Review
        #global global_market 
        if len(self.global_market) == 0:
            return
        self.crear_evento()

 
        print(self.global_market)

    def info_evento(self):
        # d7 Muestra en una ventana toda la Info de un Evento
        #global global_market 
        if len(self.global_market) == 0:
            return
        ban = 0
        texto = ""
        hora = "21hs."
        direccion = "Balcarce 212."
        telefono = "387-1221122."
        comentarios = "Muy Bueno. Nos divertimos. Excelente. Recomendable."
        for k in self.diccionario:
            text = self.diccionario[k]['text']+self.diccionario[k]["calificacion"]
            if str(self.global_market) == text:
                texto = self.diccionario[k]["calificacion"]
                if len(texto) == 0:
                    texto = "Este evento no tiene todavia ninguna calificación"
                    comentarios = " No tiene."
                else:
                    texto = "Este evento se lo califico con " + str(self.diccionario[k]["calificacion"])
                ban = 1
                break
                    
        if ban == 1:        
            print("Info Evento")
            tk.messagebox.showinfo(title = str(self.global_market), message=texto + ". Se encuentra en "
                            + direccion + " Comienza a las: " + hora + "Se pueden contactar para reservas al "
                            + telefono + " -->Comentarios de Usuarios<-- " + comentarios
                                    )
            
    def add_ruta_event(self, coords):
        # d2 Boton derecho para marcar en el mapa ruta
        print("Marcar Ruta:", coords)
        self.marcaPos.append(coords)
        pasar=self.marcaPos
        self.calcularDistancia(pasar)
        self.path_1 = self.map_widget.set_path(self.marcaPos)

    def delRuta(self):
            # d3 Boton Del que borra el recorrido en el Mapa de los Eventos
            global marcaPos
            self.marcaPos = []
            self.marcaPos += (self.marker_0.position,)
            self.map_widget.delete_all_path()
            palabra=""    
            self.labelEvent.configure(text=palabra)
            #path_1.delete()

    def createRutEvent(self):
        # d4 Boton Crear Ruta, dibuja el recorrido de la lista de Eventos y calcula los km
        if len(self.list_text) == 0:
            return
         
        self.delRuta()
        marcaPos = []
        marcaPos += (self.marker_0.position,)
            
        for evento  in self.list_text:
            for marker in self.diccionario:
                text = self.diccionario[marker]['text'] + self.diccionario[marker]["calificacion"]
                
                if evento == text:
                    print("Ruta de ", evento, " Existe.")
                    pos = self.diccionario[marker]['position']
                    #markers[marker].hide_image(False) 
                    print(pos)
                    marcaPos.append(pos)
                    break
                
        pasar = marcaPos
        self.calcularDistancia(pasar)
        self.path_1 = self.map_widget.set_path(marcaPos)

    def calcularDistancia(self, pasar):
        # d5 Calcula la distancia en Km de una lista de Eventos Guardados
        tot_km = 0
        for i in range(len(pasar)-1):

            x0,y0  = pasar[i]
            x1,y1  = pasar[1+i]

            distancia = math.sqrt((x1-x0)**2 + (y1-y0)**2)
            distancia_km = distancia * 111.139
            tot_km += distancia_km
        palabra="  Total del recorrido en Km :  " + "{:.3f}".format(tot_km)    
        self.labelEvent.configure(text=palabra)
        print("{:.3f}".format(tot_km))

    def search_event(self, event=None):
        self.map_widget.set_address(self.entry.get())

    def set_marker_event(self):
        current_position = self.map_widget.get_position()
        self.marker_list.append(self.map_widget.set_marker(current_position[0], current_position[1]))

    def clear_marker_event(self):
        for marker in self.marker_list:
            marker.delete()

    def change_appearance_mode(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_map(self, new_map: str):
        if new_map == "OpenStreetMap":
            self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif new_map == "Google normal":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        elif new_map == "Google satellite":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

    def guardar_RutaVisita(self):
        # Guarda todas las rutas elegidas por un usuario en un json "ruta_visita.json"
        if len(self.list_text) == 0:
            return
        id = 4
        id_usuario = 1
        ultimo_id = "0"
        dicc = {}   
        txt = ""
        nro=0
        # nombre = input("Ingrese el nombre de la ruta de visita: ")
        # Obtenemos la fecha y hora actual usando el método now()
        fecha_hora = datetime.now()
        nombre = fecha_hora.isoformat()
        destinos = []
        for evento  in self.list_text:
            txt += str(nro+1)+") "+evento+" "
            nro += 1
            for clave, valor in self.diccionario.items():
                if valor["text"]+ valor["calificacion"] == evento:
                    clave_principal = clave
                    destinos.append(clave_principal)
                    break
        elemento = {
            "id_usuario": id_usuario,
            "nombre": nombre,
            "destinos": destinos
            }
        #if not os.path.exists("data"):
        #    os.makedirs("data")

        #elemento = [elemento for elemento in ultimo_id.split("_") if elemento.isdigit()] 
        #ultimo_id ="".join(elemento)

        # Define the file path
        nombre_archivo = "ruta_visita.json"
        file_path = ""
        ruta_archivo = os.path.join(nombre_archivo)
        # Check if the file exists
        if os.path.isfile(ruta_archivo):
            # If the file exists, open it and load its contents into a variable
            print("entra")
            with open(ruta_archivo, "r") as archivo:
                contenido = json.load(archivo)
                ultimo_id, ultimo_elemento = contenido.popitem()
                dicc[str(int(ultimo_id))] = [ultimo_elemento]
        else:
            # If the file does not exist, create an empty dictionary
            contenido = {}
        
        # Agrega el nuevo diccionario al diccionario existente o al diccionario vacío
        dicc[str(int(ultimo_id)+1)] = [elemento]
        contenido.update(dicc)
        print(contenido)
        with open("ruta_visita.json", "w") as f:
            json.dump(contenido, f, indent = 4)
        print("Guardando ruta en Json")    
        tk.messagebox.showinfo(title = "Guardar", message= " Se Guardaron las rutas de los eventos seleccionados.  "+txt)
        self.list_text=[]
        self.listbox.delete(0, "end")     
        self.marcaPos = []
        self.marcaPos += (self.marker_0.position,)
        self.map_widget.delete_all_path()   

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()

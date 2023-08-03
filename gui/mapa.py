import tkinter as tk
import customtkinter as ctk
import os.path
import math
import json
import random
from PIL import Image, ImageTk
from tkintermapview import TkinterMapView
from datetime import datetime
from models.users import db
from CTkListbox import CTkListbox

class Mapa(ctk.CTkFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback

        
        self.user_id = self.master.user_id
        self.markers = {}
        self.list_text = []
        self.global_market =""
        self.nombreUsuario = self.get_username()
        self.diccionario = {}
        self.marker_list = []
        
        global otro
        otro = ""
        
        print(self.nombreUsuario)
        print(f"EL id en mapa es: {self.user_id}")
        
        
        
        
        
        # ============ create two CTkFrames ============
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=0)
        self.grid_columnconfigure(4, weight=0)
        self.grid_columnconfigure(5,weight=0)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = Frame_left(self, switch_frame_callback, fg_color=None)
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.frame_right = Frame_right(self, switch_frame_callback, corner_radius=0)
        self.frame_right.grid(row=0, column=1, columnspan=2, pady=0, padx=0, sticky="nsew")
        
        self.frame_review = Review_frame(self, switch_frame_callback)
        self.frame_review.grid(row=0, column=3, columnspan=3, pady=0, padx=0, sticky="news")
      
        
    # ============ Metodo de la Clase Mapa ============
    # def set_user_id(self, user_id):
    #     self.user_id = self.master.user_id
    #     print(self.user_id)
        
    def get_username(self):
        data = db.load_data("users.json")
        for user_id, user_data in data.items():
            if user_id == self.user_id:
                return user_data["username"]
        return "El usuario no fue encontrado."


class Frame_left(ctk.CTkFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        #self.var = Frame_right(parent, switch_frame_callback)

        self.markers = {}
        self.list_text = []
        self.global_market = ""
        
        self.marker_list = []
        self.user_id = self.master.user_id
        # ============ frame_left ============

        self.grid_rowconfigure(8, weight=1)

        self.map_label = ctk.CTkLabel(self, text="♬🎵 Eventos 🎵♬", anchor="w")
        self.map_label.grid(row=0, column=0, padx=(1, 20), pady=(10, 0))

        self.button_1 = ctk.CTkButton(master=self,
                                                text="Agregar",
                                                command = self.agregar)
        self.button_1.grid(pady=(5, 0), padx=(20, 20), row=1, column=0)

        self.button_2 = ctk.CTkButton(master=self,
                                                text="Borrar",
                                                command = self.borrar)
        self.button_2.grid(pady=(5, 0), padx=(20, 20), row=2, column=0)
        
        self.listbox = tk.Listbox(self, selectforeground = "#ffffff",
                            selectbackground = "#00aa00",
                            selectborderwidth = 3, height = 10, cursor = "heart #ff0000")
        for elemento in self.list_text:
            self.listbox.insert(tk.END, elemento)
        self.listbox.grid(pady=(5, 0), padx=(1, 1),row=3, column=0)

        self.map_label = ctk.CTkLabel(self, text="Rutas:", anchor="w")
        self.map_label.grid(row=4, column=0, padx=(5, 20), pady=(5, 0))
        
        self.button_6 = ctk.CTkButton(master=self,
                                                text="Dibujar",
                                                command = self.create_rut_event_selected)
        self.button_6.grid(pady=(5, 0), padx=(20, 20), row=5, column=0)

        self.button_7 = ctk.CTkButton(master=self,
                                                text="Borrar",
                                                command = self.del_rut_event_selected)
        self.button_7.grid(pady=(5, 0), padx=(20, 20), row=6, column=0)

        self.button_3 = ctk.CTkButton(master=self,
                                                text="Guardar",
                                                command=self.save_rut_event)
        self.button_3.grid(pady=(20, 0), padx=(20, 20), row=7, column=0)

        self.map_label = ctk.CTkLabel(self, text="Modos:", anchor="w")
        self.map_label.grid(row=9, column=0, padx=(20, 20), pady=(20, 0))

        self.map_option_menu = ctk.CTkOptionMenu(self, values=["OpenStreetMap", "Google normal", "Google satellite"],
                                                                       command= self.on_map_option_selected)
        self.map_option_menu.grid(row=10, column=0, padx=(20, 20), pady=(10, 0))

    # -----------------------------------------------------------------------------------------------
    # ----------------------------- Metodos de Frame_left -------------------------------------------
    # -----------------------------------------------------------------------------------------------
 
    def agregar(self):
        self.set_option("Si")
    
    def borrar(self):
        self.set_option("No")
        
    def create_rut_event_selected(self):
        # d4 Boton Crear Ruta, dibuja el recorrido de la lista de Eventos y calcula los km
        self.var = Frame_right(self.master, self.switch_frame_callback)
        if len(self.list_text) == 0:
            return
        self.delRuta()
        marcaPos = []
        marcaPos += (self.var.marker_0.position,)
      
        for evento  in self.list_text:
            for marker in self.var.diccionario:
                text = self.var.diccionario[marker]['text'] + self.var.diccionario[marker]["calificacion"]
                if evento == text:
                    print("Ruta de ", evento, " Existe.")
                    pos = self.var.diccionario[marker]['position']
                    #markers[marker].hide_image(False) 
                    print(pos)
                    self.var.marcaPos.append(pos)
                    break
        pasar = self.var.marcaPos
        self.calcularDistancia(pasar)
        self.master.frame_right.ruta_map(pasar)
        #self.var.map_widget.set_path(pasar)
        #self.var.path_1 = self.var.map_widget.set_path(pasar)
        #self.var.path_1.set_position_list(pasar)

    def delRuta(self):
        # d3 Boton Del que borra el recorrido en el Mapa de los Eventos
        global marcaPos
        self.var = Frame_right(self.master, self.switch_frame_callback)
        self.marcaPos = []
        self.marcaPos += (self.var.marker_0.position,)
        self.var.map_widget.delete_all_path()
        palabra = ""    
        self.master.frame_right.actualiza_labe_km(palabra)
        #self.var.labelEvent.configure(text=palabra)
        #path_1.delete()

    def calcularDistancia(self, pasar):
        # d5 Calcula la distancia en Km de una lista de Eventos Guardados
        #self.var = Frame_right(self.master, self.switch_frame_callback)        
        tot_km = 0
        for i in range(len(pasar)-1):
            x0,y0  = pasar[i]
            x1,y1  = pasar[1+i]
            distancia = math.sqrt((x1-x0)**2 + (y1-y0)**2)
            distancia_km = distancia * 111.139
            tot_km += distancia_km

        palabra = "  Total del recorrido en Km :  " + "{:.3f}".format(tot_km)    
        self.master.frame_right.actualiza_labe_km(palabra)
        #self.var.labelEvent.configure(text=palabra)
        print("{:.3f}".format(tot_km))

    def del_rut_event_selected(self):
        self.master.frame_right.delRuta()
        
    def save_rut_event(self):
        # Guarda todas las rutas elegidas por un usuario en un json "ruta_visita.json"
        if len(self.list_text) == 0:
            return
        id_usuario = self.master.user_id
        username = self.get_username()
        ultimo_id = "0"
        dicc = {}   
        txt = ""
        nro = 0
        # nombre = input("Ingrese el nombre de la ruta de visita: ")
        # Obtenemos la fecha y hora actual usando el método now()
        fecha_hora = datetime.now()
        nombre = fecha_hora.isoformat()
        destinos = []
        for evento  in self.list_text:
            txt += str(nro+1)+") " + evento + " "
            nro += 1
            for clave, valor in self.var.diccionario.items():
                if valor["text"]+ valor["calificacion"] == evento:
                    clave_principal = clave
                    destinos.append(clave_principal)
                    break
        elemento = {
            "id_usuario": id_usuario,
            "nombre de usuario": username,
            "nombre": nombre,
            "destinos": destinos
            }
        #if not os.path.exists("data"):
        #    os.makedirs("data")
        #elemento = [elemento for elemento in ultimo_id.split("_") if elemento.isdigit()] 
        #ultimo_id ="".join(elemento)

        # Define the file path
        nombre_archivo = "data/ruta_visita.json"
        file_path = ""
        ruta_archivo = os.path.join(nombre_archivo)
        # Check if the file exists
        if os.path.isfile(ruta_archivo):
            # If the file exists, open it and load its contents into a variable
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
        with open("data/ruta_visita.json", "w") as f:
            json.dump(contenido, f, indent = 4)
        print("Guardando ruta en Json")    
        tk.messagebox.showinfo(title = "Guardar", message = " Se Guardaron las rutas de los eventos seleccionados.  " + txt)
        self.list_text = []
        self.listbox.delete(0, "end")     
        self.marcaPos = []
        self.marcaPos += (self.var.marker_0.position,)
        self.var.map_widget.delete_all_path()   
        
    def on_map_option_selected(self, selected_map):
        # Call the change_map method in the right frame with the selected_map value
        self.master.frame_right.change_map(selected_map)

    def set_option(self,value):
        # d6 Opciones de los botones Agregar y Borrar de la lista de Eventos para crear Ruta
        if self.master.nombreUsuario == otro:
           return
        option = value
        self.global_market = otro

        if option == "Si" and len(self.global_market) > 0 and self.global_market not in self.list_text:
            print("Guardado")
            print(self.global_market)
            self.list_text.append(self.global_market)
            print(self.list_text) 
            self.listbox.insert(tk.END, self.global_market)
            self.var = Frame_right(self.master, self.switch_frame_callback)
            var = self.var.diccionario.items()
            var1 = self.var.diccionario.keys()
            for k, v in var:
                 if str(v["text"] + v["calificacion"]) == self.global_market:
                    clave =  k
                    posicion=list(var1).index(clave)
                    print(f"La clave {clave} se encuentra en la posición {posicion}.")    
                    #self.markers[clave].marker_color_circle = "green"       
                    break
        if option == "No" and len(self.list_text) > 0 and self.global_market in self.list_text:
            print("Borrado")
            self.list_text.remove(self.global_market)
            print(self.list_text)
            self.listbox.delete(self.listbox.get(0, tk.END).index(self.global_market))
        option = ""
        
    def get_username(self):
        data = db.load_data("users.json")
        for user_id, user_data in data.items():
            if user_id == self.user_id:
                return user_data["username"]
        return "El usuario no fue encontrado."

#########
def get_image_path(image_filename):
        # Get the absolute path to the "src" folder
        src_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        # Combine the "src" folder path with the "images" folder and the provided image filename
        image_path = os.path.join(src_folder, "src", image_filename)
        return image_path
    
#########

# ============ Ckase Frame_right ============
        
class Frame_right(ctk.CTkFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        
        self.markers = {}
        self.list_text = []
        self.global_market = ""
        self.marker_list = []
        self.user_id = self.master.user_id

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)

        self.map_widget = TkinterMapView(self, corner_radius=0)
        self.map_widget.grid(row=1, rowspan=1, column=0, columnspan=6, sticky="nswe", padx=(0, 0), pady=(0, 0))

        self.labelEvent = ctk.CTkLabel(self, text = "", anchor = "w", text_color="black",
                                       fg_color = "#ffffff", justify = "center", compound = "center")
        self.labelEvent.grid(row = 0, column = 0, sticky = "we", padx=(12, 0), pady = 12)

        self.button_5 = ctk.CTkButton(master = self,
                                                text = "Cartelera",
                                                width = 90,
                                                command = self.info_evento)
        self.button_5.grid(row = 0, column = 1, sticky = "w", padx = (12, 0), pady = 12)

        self.button_9 = ctk.CTkButton(master = self,
                                                text="Review",
                                                width = 90,
                                                command = self.review)
        self.button_9.grid(row = 0, column = 2, sticky = "w", padx = (12, 0), pady = 12)
        
        # ==================== Set Usuario ======================
        pos1 = -24.7868489
        pos2 = -65.4120303
        self.nombreUsuario = self.get_username()
        
        image_path = get_image_path("usuario1.jpg")
        usuario_image = ImageTk.PhotoImage(Image.open(image_path).resize((100, 100)))
        # usuario_image = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.relpath(__file__)),
        #                                                     "src", "usuario1.jpg")).resize((100, 100)))
                #usuario_icono = ImageTk.PhotoImage(Image.open(image_path).resize((35, 35)))
        
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
                    "marker_5": {"position": (-24.7887507, -65.4070912), "text": "Charanga Habanera", "image": "image8.jpg","calificacion":""},
                    }

        numero1 = list(range(13))
        numero2 = list(range(13))
        imagen = list(range(13))
        tex = list(range(13))
        for i in range(13):
            numero1[i] = random.uniform(-24.7463100, -24.8386949)
            #numero_redondeado = round(numero1[i], 7)
            numero2[i] = random.uniform(-65.3749002, -65.4775537)
            #numero_redondeado = round(numero2[i], 7)
            ign=9+i
            imagen[i]= "image"+str(ign)+".jpg"
            tex[i]= "Evento : "+str(ign)
            key="marker_"+str(i+6)
            agregar={key:{"position": (numero1[i], numero2[i]), "text": tex[i], "image": imagen[i] ,"calificacion":""}}                                                                                                                       
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
            image_path = get_image_path(image_name)
            evento_images[key] = ImageTk.PhotoImage(Image.open(image_path).resize((100, 100)))
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
        # self.map_option_menu.set("OpenStreetMap")
        # self.appearance_mode_optionemenu.set("Dark")
        self.map_widget.add_right_click_menu_command(label="Marcar Ruta",
                                        command=self.add_ruta_event,
                                        pass_coords=True)

    # -----------------------------------------------------------------------------------------------
    # ----------------------------- Metodos de Frame_right-------------------------------------------
    # -----------------------------------------------------------------------------------------------
    def crear_evento(self):

        self.diccionario = {}
        self.diccionario = {"marker_1": {"position": (-24.7825492, -65.4167884), "text": "MUSIC Festival",    "image": "image3.jpg", "calificacion":"★★★"},
                    "marker_2": {"position": (-24.7854359, -65.41249414),"text": "Music Nostalgia",   "image": "image4.jpg", "calificacion":"★★"},
                    "marker_3": {"position": (-24.7830168, -65.4110807), "text": "Music Folklore",    "image": "image5.jpg", "calificacion":"★"},
                    "marker_4": {"position": (-24.7895177, -65.4180384), "text": "DJ Gloria",         "image": "image7.jpg", "calificacion":"★★"},
                    "marker_5": {"position": (-24.7887507, -65.4070912), "text": "Charanga Habanera", "image": "image8.jpeg","calificacion":""},
                    }

        numero1 = list(range(13))
        numero2 = list(range(13))
        imagen = list(range(13))
        tex = list(range(13))
        for i in range(13):
            numero1[i] = random.uniform(-24.7463100, -24.8386949)
            #numero_redondeado = round(numero1[i], 7)
            numero2[i] = random.uniform(-65.3749002, -65.4775537)
            #numero_redondeado = round(numero2[i], 7)
            ign = 9 + i
            imagen[i] = "image" + str(ign) + ".jpg"
            tex[i] = "Evento : "+str(ign)
            key = "marker_" + str(i+6)
            agregar = {key:{"position": (numero1[i], numero2[i]), "text": tex[i], "image": imagen[i] ,"calificacion":""}}                                                                                                                       
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
            image_path = get_image_path(image_name)
            evento_images[key] = ImageTk.PhotoImage(Image.open(image_path).resize((100, 100)))
            # evento_images[key] = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.relpath(__file__)),
            #                                                                 "src", image_name)).resize((250,200)))
            self.markers[key] = self.map_widget.set_marker(positions1,positions2, text=texts, image=evento_images[key],
                                        image_zoom_visibility=(0, float("inf")), command=self.click_usuario)
            self.markers[key].hide_image(True)  
            self.markers[key].set_text(texts)
            if len(self.diccionario[key]["calificacion"]) == 0:
                self.markers[key].text_color = "black"
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
        global otro
        otro = self.global_market
        self.labelEvent.configure(text ="  " + self.global_market)

        if marker.image_hidden is True:
            for key in self.diccionario:
                self.markers[key].hide_image(True) 
                #self.markers[key].marker_color_circle = "red" # <<<<<< no cambia de color
            marker.hide_image(False)
        else:
            marker.hide_image(True)
        #self.marker.marker_color_circle = "green" 

    def set_option1(self,value):
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
            Frame_left.listbox.insert(tk.END, self.global_market)

            for k, v in self.diccionario.items():
                    if str(v["text"] + v["calificacion"]) == self.global_market:
                        clave =  k
                        posicion=list(self.diccionario.keys()).index(clave)
                        print(f"La clave {clave} se encuentra en la posición {posicion}.")    
                        #self.markers[clave].marker_color_circle = "green"       
                        break

        if option == "No" and len(self.list_text) > 0 and self.global_market in self.list_text:
            print("Borrado")
            self.list_text.remove(self.global_market)
            print(self.list_text)
            Frame_left.listbox.delete(self.listbox.get(0, tk.END).index(self.global_market))
        option = ""

    def review(self):
        # d6.5 Boron de Review
        #global global_market 
        if len(self.global_market) == 0:
            return
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
                            + telefono )
            
    def ruta_map(self, pasar):
        self.path_1 = self.map_widget.set_path(pasar)
 
    def actualiza_labe_km(self, mensaje):
        self.labelEvent.configure(text=mensaje)
 
    def add_ruta_event(self, coords):
        # d2 Boton derecho para marcar en el mapa ruta
        print("Marcar Ruta:", coords)
        self.marcaPos.append(coords)
        pasar = self.marcaPos
        self.calcularDistancia(pasar)
        self.path_1 = self.map_widget.set_path(self.marcaPos)

    def calcularDistancia(self, pasar):
        # d5 Calcula la distancia en Km de una lista de Eventos Guardados
        tot_km = 0
        for i in range(len(pasar)-1):
            x0,y0  = pasar[i]
            x1,y1  = pasar[1+i]
            distancia = math.sqrt((x1-x0)**2 + (y1-y0)**2)
            distancia_km = distancia * 111.139
            tot_km += distancia_km
        palabra = "  Total del recorrido en Km :  " + "{:.3f}".format(tot_km)    
        self.labelEvent.configure(text = palabra)
        print("{:.3f}".format(tot_km))

    def delRuta(self):
        # d3 Boton Del que borra el recorrido en el Mapa de los Eventos
        global marcaPos
        self.marcaPos = []
        self.marcaPos += (self.marker_0.position,)
        self.map_widget.delete_all_path()
        palabra = ""    
        self.labelEvent.configure(text = palabra)

    def search_event(self, event=None):
        self.map_widget.set_address(self.entry.get())

    def set_marker_event(self):
        current_position = self.map_widget.get_position()
        self.marker_list.append(self.map_widget.set_marker(current_position[0], current_position[1]))

    def clear_marker_event(self):
        for marker in self.marker_list:
            marker.delete()

    def change_map(self, new_map: str):
        if new_map == "OpenStreetMap":
            self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif new_map == "Google normal":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        elif new_map == "Google satellite":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
            
    def get_username(self):
        data = db.load_data("users.json")
        for user_id, user_data in data.items():
            if user_id == self.user_id:
                return user_data["username"]
        return "El usuario no fue encontrado."

##### frame review

class Review_frame(ctk.CTkFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        
        self.user_id = self.master.user_id
        print(f"Este print es del review frame: {self.user_id}")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        
        frame1 = Most_review(self, switch_frame_callback)
        frame1.grid(row=0, rowspan=2, column=0, sticky="news")
        frame2 = Review_gen(self, switch_frame_callback)
        frame2.grid(row=2, column=0, sticky="news")
        
        
        
class Most_review(ctk.CTkScrollableFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.select = ctk.CTkComboBox(self,
                                     values=["Music Festival", "Music Nostalgia", "Music Folklore", "Concierto de DJ Gloria", "Charanga Habanera Music Show"],
                                     command=self.insert_reviews, state="readonly")
        self.select.grid(row=0, column=0, columnspan=2)
        self.label = ctk.CTkTextbox(self, height= 300, state="disabled")
        self.label.grid(row=1, column= 0, columnspan=2)
        
    def insert_reviews(self, event=None):
        data = db.load_data("reviews.json")
        selection = self.select.get()
        
        self.label.configure(state="normal")
        self.label.delete(1.0, "end")
        reviews_found = False
        for key, review_data in data.items():
            if selection == review_data["nombre_evento"]:
                self.label.insert("end", f"Usuario: {review_data['apellido_nombre']} \n")
                self.label.insert("end", f"Calificación: {review_data['calificacion']}\n")
                self.label.insert("end", f"Comentario: {review_data['comentario']}\n")
                self.label.insert("end", f"Ánimo: {review_data['animo']}\n")
                self.label.insert("end", "--------------------\n")
                reviews_found = True
        
        if not reviews_found:
            self.label.insert("end", "No hay reviews disponibles.")
        self.label.configure(state="disabled")
        
class Review_gen(ctk.CTkFrame):
    def __init__(self, parent, switch_frame_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        self.id_evento = None
        self.id_usuario = self.master.user_id
        self.apellido = self.get_apellido()
        self.nombre = self.get_nombre()
        self.calificacion = None
        self.comentario = None
        self.animo = None
        
        for r in range(6):
            self.grid_rowconfigure(r, weight=0)
        
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0)
        
        placeholder = ctk.CTkLabel(self, text="")
        placeholder.grid(row= 0, column=0, columnspan=2, sticky = "news")
        
        self.lista = ctk.CTkComboBox(self,
                                     values=["Music Festival", "Music Nostalgia", "Music Folklore", "Concierto de DJ Gloria", "Charanga Habanera Music Show"],
                                     command=self.show_value, state="readonly")
        self.lista.grid(row=1, column=0, columnspan= 2, sticky= "news")
        # self.lista.insert(0, "Music Festival")
        # self.lista.insert(1, "Music Nostalgia")
        # self.lista.insert(2, "Music Folklore")
        # self.lista.insert(3, "Concierto de DJ Gloria")
        # self.lista.insert(4, "Charanga Habanera Music Show")
        
        
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
        boton_crear_review = ctk.CTkButton(self, text='Crear Review', command=lambda: self.crear_review())
        # Ubicar los elementos en la ventana
        label_calificacion.grid(row=3, column=0)
        label_comentario.grid(row=4, column=0)
        label_animo.grid(row=5, column=0)
        
        self.entry_calificacion.grid(row=3, column=1)
        self.entry_comentario.grid(row=4, column=1)
        self.entry_animo.grid(row=5, column=1)

        boton_crear_review.grid(row=6, columnspan=2)
        
    def show_value(self, selected_option):
        data = db.load_data_from_eventos("basededatos.json") 
        selected_event_name = self.lista.get()
        
        for event in data:
            if event.get("nombre") == selected_event_name:
                selected_indice = event.get("indice")
                return selected_indice

        return None
        
    
    def crear_review(self):
        selected_event_name = self.lista.get()
        self.id_evento = self.show_value(selected_event_name)
        
        calificacion = self.entry_calificacion.get()
        comentario = self.entry_comentario.get()
        animo = self.entry_animo.get().capitalize()
        
        
        if self.id_evento is None:
            # If the selected event is not found, show an error message
            tk.messagebox.showerror("Error", "Por favor seleccione un evento.")
            return


        # Validación de la calificación (entre 1 y 5)
        try:
            self.calificacion = int(calificacion)
            if self.calificacion <= 0 or self.calificacion > 5:
                raise ValueError()
        except ValueError:
            tk.messagebox.showerror("Error", "La calificación debe ser un número entre 1 y 5.")
            return

        # Validación del ánimo (aceptando solo "Triste", "Neutral" o "Feliz")
        animo_permitidos = ["Triste", "Neutral", "Feliz"]
        if animo not in animo_permitidos:
            tk.messagebox.showerror("Error", "El ánimo debe ser 'Triste', 'Neutral' o 'Feliz'.")
            return
        
        self.comentario = comentario
        self.animo = animo
        
        self.id_review = self.generar_review_id()

        # Resto del código para crear el review
        nuevo_review = {
            "id_evento": self.id_evento,
            "nombre_evento": selected_event_name,
            "id_usuario": self.id_usuario,
            "apellido_nombre": f"{self.apellido} {self.nombre}",
            "calificacion": self.calificacion,
            "comentario": comentario,
            "animo": animo
        }

        reviews = db.load_data("reviews.json")
        
        # Si el review.json no tiene información lo iniciamos desde 0
        if reviews is None:
            reviews = {}
        

        # Store the new review using the id_review as the key
        reviews[self.id_review] = nuevo_review
            
        

        db.save_data(reviews, "reviews.json")

        # Validación de la calificación (entre 1 y 5)
        if self.calificacion <= 0 or self.calificacion > 5:
                tk.messagebox.showerror("Error", "La calificación debe estar entre 1 y 5.")
                return
        self.comentario = self.entry_comentario.get()

        # Validación del ánimo (aceptando solo "Triste", "Neutral" o "Feliz")
        animo_permitidos = ["Triste", "Neutral", "Feliz"]
        self.animo = self.entry_animo.get().capitalize()
        if self.animo not in animo_permitidos:
            tk.messagebox.showerror("Error", "El ánimo debe ser 'Triste', 'Neutral' o 'Feliz'.")
            return
         

    def generar_review_id(self):
        # Load reviews data from the JSON database
        data = db.load_data("reviews.json")

        # Find the maximum review ID in the existing data
        max_review_id = 0
        if data:
            for review_id in data.keys():
                max_review_id = max(max_review_id, int(review_id))

        # Increment the max_review_id by 1 to generate a new review ID
        new_review_id = max_review_id + 1
        return str(new_review_id)
        
    def get_apellido(self):
        data = db.load_data("users.json")
        for user_id, user_data in data.items():
            if user_id == self.id_usuario:
                return user_data["apellido"]
                
            
    def get_nombre(self):
        data = db.load_data("users.json")
        for user_id, user_data in data.items():
            if user_id == self.id_usuario:
                return user_data["nombre"]
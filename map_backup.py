"""
Agrego boton para crear rutas de los eventos seleccionados y me dice el total de km
"""
import customtkinter

from CTkMessagebox import CTkMessagebox
from CTkListbox import CTkListbox
import tkintermapview
import math
import os
from PIL import Image, ImageTk
import tkinter

# Inicializacion de variables 
list_text=[]
option = ""
global_market=""
coordenadas=[]
marcapos=[]

# Funciones 

def delRuta():
    # Borra la ruta en el Mapa
    global marcapos
    marcapos=[]
    marcapos+=(Map.marker_0.position,)
    #path_1.delete()
    Map.map_widget.delete_all_path()
    #With map_widget.delete_all_path() all path on the map will be deleted.
    #path_1 = map_widget.set_path(marcapos)
    Map.palabra.set("")

def createRutEvent():
    
    if len(list_text) == 0:
        return
    delRuta()
    marcapos=[]
    marcapos+=(Map.marker_0.position,)
    
    for evento  in list_text:
     for marker in Map.diccionario:
         text = Map.diccionario[marker]['text']+Map.diccionario[marker]["calificacion"]
         
         if evento==text:
            print("Ruta de ", evento, " Existe.")
            pos=Map.diccionario[marker]['position']
            #markers[marker].hide_image(False) 
            print(pos)
            marcapos.append(pos)
            break
    pasar=marcapos
    calcularDistancia(pasar)
    path_1 = Map.map_widget.set_path(marcapos)

def calcularDistancia(pasar):
    tot_km=0
    for i in range(len(pasar)-1 ):

        x0,y0  = pasar[i]
        x1,y1  = pasar[1+i]

        distancia = math.sqrt((x1-x0)**2 + (y1-y0)**2)
        distancia_km = distancia * 111.139
        tot_km += distancia_km
    
    Map.palabra.set("Tot Km: "+"{:.3f}".format(tot_km)) 
    print("{:.3f}".format(tot_km))

def set_option(value):
    global global_market 

    if Map.nombreUsauario == global_market:
        return
    
    global option
    option = value
    #root.destroy()

    if option=="Si" and len(global_market)>0 and global_market not in list_text:
              
        print("Guardado")
        list_text.append(global_market)
        print(list_text) 
        Map.listbox.insert(tkinter.END, global_market)  

    if option=="No" and len(list_text)>0 and global_market in list_text:
        print("Borrado")
        list_text.remove(global_market)
        print(list_text)
        Map.listbox.delete(Map.listbox.get(0, tkinter.END).index(global_market))
        #global_market=""
    option=""

def info_evento():
    global global_market 

    if len(global_market)==0:
       return
    ban=0
    texto=""
    hora="21hs."
    direccion="Balcarce 212."
    telefono="387-1221122."
    comentarios="Muy Bueno. Nos divertimos. Excelente. Recomendable."
    for k in Map.diccionario:
        text = Map.diccionario[k]['text']+Map.diccionario[k]["calificacion"]
        if str(global_market)==text:
            texto = Map.diccionario[k]["calificacion"]
            if len(texto)==0:
                texto="Este evento no tiene todavia ninguna calificación"
                comentarios=" No tiene."
            else:
                texto = "Este evento se lo califico con "+str(Map.diccionario[k]["calificacion"])
            ban=1
            break
            
    if ban==1:        
        print("Info Evento")
        CTkMessagebox.showinfo(title=str(global_market), message=texto+". Se encuentra en "+direccion+" Comienza a las: "+hora+
                                     "Se pueden contactar para reservas al "+telefono+" -->Comentarios de Usuarios<-- "+comentarios
                                     )
   
   
       

def click_usuario(marker):
   # Click mouse izq. Marca un evento y desmarca un evento mostrando Imagen
    print("marker clicked:", marker.text)
    global global_market
    global_market=marker.text
    Map.label_palabra.set(str(marker.text))

    if marker.image_hidden is True:
        for key in Map.diccionario:
            Map.markers[key].hide_image(True) 
            Map.markers[key].marker_color_circle="red"
        marker.hide_image(False)
        #tkinter.messagebox.showinfo(title="", message="Quiere guardar este evento a su lista?")
    else:
         marker.hide_image(True)
    marker.marker_color_circle="green" 
    #marker.text_color="green"
    #marker.set_text("nombreUsauario")
    #marker.marker_color_circle="green"
   
"""
def marker_callback(marker):
    print(marker.text)
    marker.delete()
"""
# create tkinter window

class Map(customtkinter.CTkFrame):
    """clase para abrir el Frame MAPA"""
    def __init__(self, Frame, switch_frame_callback, *args, **kwargs):
        super().__init__(Frame, *args, **kwargs)
        self.switch_frame_callback = switch_frame_callback
        
        # configuración de columnas
        for i in range(6):
            self.grid_columnconfigure(i, weight=0)
            
        # configuración de filas
        for i in range(6):
            self.grid_rowconfigure(i, weight=0)
        
        
        palabra= customtkinter.StringVar(self)
        label_palabra = customtkinter.StringVar(self)

        # create map widget
        map_widget = tkintermapview.TkinterMapView(self, width=800, height=600, corner_radius=0)
        map_widget.grid(row=0, column=1, columnspan=5, rowspan=5)


        boton_DelKm = customtkinter.CTkButton(self, text="Del", font=("Courier",8), bg_color="#00a8e8", fg_color="white", command=delRuta)
        boton_DelKm.grid(row=3, column=0)

        boton_CreateRutEvent = customtkinter.CTkButton(self, text="Crea Ruta", font=("Courier",8), bg_color="#00a8e8", fg_color="white", command=createRutEvent)
        boton_CreateRutEvent.grid(row=4, column=0)


        labelRutaKm= customtkinter.CTkLabel(self, text="Ruta Km :", textvariable=palabra, fg_color="white", bg_color="black", justify="center" )
        labelRutaKm.grid(row=2, column=0)

        labelEvent= customtkinter.CTkLabel(self, text="", textvariable=label_palabra, fg_color="white", bg_color="black", justify="center" )
        labelEvent.grid(row=3, column=0)

        boton_DelEvent = customtkinter.CTkButton(self, text="Borrar ", font=("Courier",8), bg_color="#00a8e8", fg_color="white", command=lambda: set_option("No"))
        boton_DelEvent.grid(row=6, column=0)

        boton_AddEvent = customtkinter.CTkButton(self, text="Agregar", font=("Courier",8), bg_color="#00a8e8", fg_color="white",command=lambda: set_option("Si"))
        boton_AddEvent.grid(row=5, column=0)

        boton_InfoEvent = customtkinter.CTkButton(self, text="  Info   ", font=("Courier",8), bg_color="#00a8e8", fg_color="white",command=info_evento)
        boton_InfoEvent.grid(row=6, column=0)

        listbox = tkinter.Listbox(self)
        # Agregar los elementos a la lista
        scrollbar = tkinter.Scrollbar(listbox, orient=tkinter.VERTICAL)
        listbox = tkinter.Listbox(self)
        scrollbar.config(command=listbox.yview)
        # # Ubicarla a la derecha.
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        listbox = tkinter.Listbox(self)

        for elemento in list_text:
            listbox.insert(tkinter.END, elemento)

        # Empaquetar la lista en la ventana
        #listbox.grid_remove()
        #frame.pack()
        listbox.pack(side="bottom")

        #(side="bottom",fill=customtkinter.NONE, expand=0)

        #-------------------------------------USUARIO------------------------------------------
        """
        Ingresar posicion o coordenadas del Usuario mas imagenes
        """

        image_path = Map.get_image_path("usuario1.jpg")
        usuario_image = ImageTk.PhotoImage(Image.open(image_path).resize((100, 100)))
        
        #usuario_image = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.relpath(__file__)), "src", "usuario1.jpg")).resize((100, 100)))

        pos1=-24.7868489
        pos2=-65.4120303
        nombreUsauario="Facundo Ovejero"

        marker_0 = map_widget.set_marker(pos1, pos2, text=nombreUsauario, image=usuario_image,
                                        image_zoom_visibility=(14, float("inf")), command=click_usuario)
        marker_0.hide_image(True)  # hide image
        marker_0.set_text(nombreUsauario)
        marker_0.marker_color_circle="#006400"
        marker_0.marker_color_outside="#00FF00"
        marker_0.text_color="#006400"


        #------------------------------EVENT-------------------------------------------
        # set current widget position by address
        # Cargar de un json las cordenadas de los Eventos

        # Se cargan las imagenes
        diccionario = {"marker_1": {"position": (-24.7825492,-65.4167884), "text": "MUSIC Festival", "image": "image3.jpg", "calificacion":"★★★"},
                    "marker_2": {"position": (-24.7854359, -65.41249414), "text": "Music Nostalgia", "image": "image4.jpg","calificacion":"★★"},
                    "marker_3": {"position": (-24.7830168, -65.4110807), "text": "Music Folklore", "image": "image5.jpg","calificacion":"★"},
                    "marker_4": {"position": (-24.7895177, -65.4180384), "text": "DJ Gloria", "image": "image7.jpg","calificacion":"★★"},
                    "marker_5": {"position": (-24.7887507, -65.4070912), "text": "Charanga Habanera", "image": "image8.jpeg","calificacion":""}
                    }

        evento_images = {}
        markers={}
        marcapos=[]
        marcapos+=(marker_0.position,)

        for key in diccionario:
            image_name = diccionario[key]["image"]
            positions1 = diccionario[key]["position"][0]
            positions2 = diccionario[key]["position"][1]
            texts = diccionario[key]["text"]+diccionario[key]["calificacion"]
            
            image_path = Map.get_image_path(image_name)
            evento_images[key] = ImageTk.PhotoImage(Image.open(image_path).resize((100, 100)))

            #evento_images[key] = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.relpath(__file__)), "src", image_name)).resize((250,200)))
        
            markers[key] = map_widget.set_marker(positions1,positions2, text=texts, image=evento_images[key],
                                        image_zoom_visibility=(0, float("inf")), command=click_usuario)
            markers[key].hide_image(True)  
            markers[key].set_text(texts)
            markers[key].marker_color_circle="red"
        
            
        #--------------------------------MAP---------------------------------------------------
        # set current widget position and zoom
        map_widget.set_position(pos1,pos2)  # Salta Usuario
        map_widget.set_zoom(16)

        #-------------------------------------BOTTOM MOUSE----------------------------------------------
        def add_ruta_event(coords):
            print("Add Ruta:", coords)
            marcapos.append(coords)
            pasar=marcapos
            calcularDistancia(pasar)
            path_1 = map_widget.set_path(marcapos)

        map_widget.add_right_click_menu_command(label="Add Ruta",
                                                command=add_ruta_event,
                                                pass_coords=True)


        def left_click_event(coordinates_tuple):
            coordenadas.append(coordinates_tuple)
            print("Left click event with coordinates:", coordinates_tuple)
            
        map_widget.add_left_click_map_command(left_click_event)

    ### path to the images: 
    def get_image_path(image_filename, folder_path="src/"):
        # Combine the "images" folder path with the provided image filename
        image_path = os.path.join(folder_path, image_filename)

        return image_path
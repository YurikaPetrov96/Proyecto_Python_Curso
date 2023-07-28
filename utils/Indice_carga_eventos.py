import json
import os


class Evento:
    def __init__(self, nombre, artista, genero, ubicacion, horario_ini, horario_fin, descripcion, imagen, fecha, provincia):
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.ubicacion = ubicacion
        self.horario_ini = horario_ini
        self.horario_fin = horario_fin
        self.descripcion = descripcion
        self.imagen = imagen
        self.fecha = fecha
        self.provincia = provincia


class Indice:
    def __init__(self, archivo):
        self.archivo = archivo
        self.eventos = self.carga()

    def carga(self):
        try:
            with open(self.archivo, 'r') as f:
                eventos = json.load(f)
        except FileNotFoundError:
            eventos = []
        return eventos

    def guardar(self):
        with open(self.archivo, 'w') as f:
            json.dump(self.eventos, f, indent=4)

    def agregar(self, evento):
        if not self.eventos:
            self.eventos = []

        indice = len(self.eventos) + 1
        evento_dict = evento.__dict__
        evento_dict['indice'] = indice
        self.eventos.append(evento_dict)
        self.guardar()

    def mostrar(self):
        if len(self.eventos) == 0:
            print("No hay eventos registrados")
        else:
            print("Eventos registrados: ")
            for evento in self.eventos:
                print(f"Evento {evento['indice']}:")
                print(f"Nombre: {evento['nombre']}")
                print(f"Artista: {evento['artista']}")
                print(f"Genero: {evento['genero']}")
                print(f"Ubicacion: {evento['ubicacion']}")
                print(f"Horario de inicio: {evento['horario_ini']}")
                print(f"Horario de finalizacion: {evento['horario_fin']}")
                print(f"Descripcion del evento: {evento['descripcion']}")
                print(f"Imagen: {evento['imagen']}")
                print(f"Fecha del evento: {evento['fecha']}")
                print(f"Provincia del evento: {evento['provincia']}")

            self.guardar()


archivo_json = "C:/Users/HP/Documents/GitHub/Proyecto_Python_Curso/data/basededatos.json"

indice = Indice(archivo_json)
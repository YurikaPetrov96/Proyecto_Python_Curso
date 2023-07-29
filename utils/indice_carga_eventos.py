import json
from models.users import db


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
        self.evento_id = self.generate_evento_id


    @classmethod
    def generate_evento_id(cls): #generamos el user id.
        data = db.load_data("basededatos.json") #caragamos la base de datos
        if data:
            max_evento_id = max(map(int, data.keys())) #si en la db hay una key numeral la pasamos a int para realizarle una suma.
            return str(max_evento_id + 1)
        else:
            return "1" #si no existe data usamos esto.
        
    

class Indice:
    def __init__(self, archivo):
        self.archivo = archivo
        self.eventos = self.carga()

    def agregar(self, evento):
        db.load_data("basededatos.json")
        

    def mostrar(self):
        if len(self.eventos) == 0:
            return f"No hay eventos registrados."
        else:
            eventos_indice = {}
            for evento in self.eventos:
                evento_dict = {
                    "indice": evento[int('indice')],
                    "nombre": evento['nombre'],
                    "artista": evento['artista'],
                    "genero": evento['genero'],
                    "ubicacion": evento['ubicacion'],
                    "horario_ini": evento['horario_ini'],
                    "horario_fin": evento['horario_fin'],
                    "descripcion": evento['descripcion'],
                    "imagen": evento['imagen'],
                    "fecha": evento['fecha'],
                    "provincia": evento['provincia']
                }
                eventos_indice.update(evento_dict)
            return eventos_indice
        
        
archivo_json = 'data/basededatos.json'
indice = Indice(archivo_json)



# while True:
#     print("\n--- Índice de Eventos ---")
#     print("1. Agregar evento")
#     print("2. Mostrar eventos")
#     print("3. Salir")

#     opcion = input("Seleccione una opción: ")

#     if opcion == "1":
#         nombre = input("Ingrese el nombre del evento: ")
#         artista = input("Ingrese el nombre del artista: ")
#         genero = input("Ingrese el género musical: ")
#         ubicacion = input("Ingrese la ubicación del evento: ")
#         horario_i = input("Ingrese el horario de inicio: ")
#         horario_f = input("Ingrese el horario de finalizacion: ")
#         descripcion = input("Ingrese una descripcion: ")
#         imagen = input("Ingrese la url de la imagen: ")
#         fecha = input("Ingrese la fecha del evento: ")
#         provincia = input("Ingrese la provincia: ")

#         evento = Evento(nombre, artista, genero, ubicacion, horario_i, horario_f, descripcion, imagen, fecha, provincia)
#         indice.agregar(evento)
#     elif opcion == "2":
#         indice.mostrar()
#     elif opcion == "3":
#         print("¡Hasta luego!")
#         break
#     else:
#         print("Opción inválida. Por favor, ingresa una opción válida.")
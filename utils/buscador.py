import json

class Buscador:
    def __init__(self, nombre, genero, artista, ubicacion):
        self.nombre = nombre
        self.genero = genero
        self.artista = artista
        self.ubicacion = ubicacion

    def __str__(self):
        return f"Nombre: {self.nombre}, Género: {self.genero}, Artista: {self.artista}, Ubicación: {self.ubicacion}"

class Filtros:
    def __init__(self, filters): #cambiar por el archivo creado por indice
        self.eventos = self.cargar_eventos_json(filters) #cambiar por el archivo creado por indice

    def cargar_eventos_json(self, filters): #cambiar por el archivo creado por indice 
        eventos = []
        with open('data/filters.json', 'r', encoding="utf-8") as archivo: #cambiar por el archivo creado por indice 
            datos_eventos = json.load(archivo)
            for datos_evento in datos_eventos:
                evento = Buscador(datos_evento['nombre'], datos_evento['genero'], datos_evento['artista'], datos_evento['ubicacion'])
                eventos.append(evento)
        return eventos
    
    def filtrar_atributo(self, atributo, valor):
        resultados = []
        for evento in self.eventos:
            if getattr(evento, atributo).lower() == valor.lower():
                resultados.append(evento)
        if resultados:
            for evento in resultados:
                print(evento)
        return resultados

    def por_nombre(self, nombre):
        return self.filtrar_atributo("nombre", nombre)


    def por_genero(self, genero):
        return self.filtrar_atributo("genero", genero)

    def por_artista(self, artista):
        return self.filtrar_atributo("artista", artista)

    def por_ubicacion(self, ubicacion):
        return self.filtrar_atributo("ubicacion", ubicacion)
    
#Ejemplo de uso:

buscar = Filtros('data/filters.json') #cambiar por el archivo creado por indice

resultados_nombre = buscar.por_nombre("Evento 1")

resultados_genero = buscar.por_genero("Pop")

resultados_artista = buscar.por_artista("Artista 3")

resultados_ubicacion = buscar.por_ubicacion("Lugar 2")
import json

class Buscador:
    def __init__(self, nombre, genero, artista, ubicacion, horario):
        self.nombre = nombre
        self.genero = genero
        self.artista = artista
        self.ubicacion = ubicacion
        self.horario = horario

class Filtros:
    def __init__(self, eventos):
        self.eventos = eventos

    def por_nombre(self, nombre):
        resultados = []
        for evento in self.eventos:
            if evento.nombre.lower() == nombre.lower():
                resultados.append(evento)
        return resultados

    def por_genero(self, genero):
        resultados = []
        for evento in self.eventos:
            if evento.genero.lower() == genero.lower():
                resultados.append(evento)
        return resultados

    def por_artista(self, artista):
        resultados = []
        for evento in self.eventos:
            if evento.artista.lower() == artista.lower():
                resultados.append(evento)
        return resultados

    def filtro_ubicacion(self, ubicacion):
        resultados = []
        for evento in self.eventos:
            if evento.ubicacion.lower() == ubicacion.lower():
                resultados.append(evento)
        return resultados

    def filtro_horario(self, horario):
        resultados = []
        for evento in self.eventos:
            if evento.horario == horario:
                resultados.append(evento)
        return resultados
    
def cargar_eventos_json(filters):
    eventos = []
    with open(filters, 'r') as archivo:
        datos_eventos = json.load(archivo)
        for datos_evento in datos_eventos:
            evento = Buscador(datos_evento['nombre'], datos_evento['genero'], datos_evento['artista'], datos_evento['ubicacion'], datos_evento['horario'])
            eventos.append(evento)
    return eventos

#Ejemplo de uso:

eventos = cargar_eventos_json('filters.json')
buscador = Filtros(eventos)

resultados_nombre = buscador.por_nombre("Concierto A")
print("Resultados de búsqueda por nombre:")
for evento in resultados_nombre:
    print("Nombre:", evento.nombre)
    print("Género:", evento.genero)
    print("Artista:", evento.artista)
    print("Ubicación:", evento.ubicacion)
    print("Horario:", evento.horario)
    print()

resultados_genero = buscador.por_genero("Rock")
print("Resultados de búsqueda por género:")
for evento in resultados_genero:
    print("Nombre:", evento.nombre)
    print("Género:", evento.genero)
    print("Artista:", evento.artista)
    print("Ubicación:", evento.ubicacion)
    print("Horario:", evento.horario)
    print()

resultados_artista = buscador.por_artista("Banda A")
print("Resultados de búsqueda por artista:")
for evento in resultados_artista:
    print("Nombre:", evento.nombre)
    print("Género:", evento.genero)
    print("Artista:", evento.artista)
    print("Ubicación:", evento.ubicacion)
    print("Horario:", evento.horario)
    print()

resultados_ubicacion = buscador.filtro_ubicacion("Ciudad B")
print("Resultados de filtrado por ubicación:")
for evento in resultados_ubicacion:
    print("Nombre:", evento.nombre)
    print("Género:", evento.genero)
    print("Artista:", evento.artista)
    print("Ubicación:", evento.ubicacion)
    print("Horario:", evento.horario)
    print()

resultados_horario = buscador.filtro_horario("19:30")
print("Resultados de filtrado por horario:")
for evento in resultados_horario:
    print("Nombre:", evento.nombre)
    print("Género:", evento.genero)
    print("Artista:", evento.artista)
    print("Ubicación:", evento.ubicacion)
    print("Horario:", evento.horario)
    print()
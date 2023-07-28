import json

class Buscador:
    def __init__(self, eventos):
        self.eventos = eventos

    def buscar_clave_valor(self, clave, valor):
        resultados = []
        for evento in self.eventos:
            if hasattr(evento, clave) and getattr(evento, clave) == valor:
                resultados.append(evento)
        return resultados

class Filtros:
    def __init__(self, eventos):
        self.eventos = eventos

    def por_nombre(self, nombre):
        return self.filtrar_atributo("nombre", nombre)

    def por_genero(self, genero):
        return self.filtrar_atributo("genero", genero)

    def por_artista(self, artista):
        return self.filtrar_atributo("artista", artista)

    def por_ubicacion(self, ubicacion):
        return self.filtrar_atributo("ubicacion", ubicacion)

    def por_horario(self, horario):
        return self.filtrar_atributo("horario", horario)

    def filtrar_atributo(self, atributo, valor):
        resultados = []
        for evento in self.eventos:
            if hasattr(evento, atributo) and getattr(evento, atributo) == valor:
                resultados.append(evento)
        return resultados
    
def cargarjson():
        with open('data/filters.json', 'r', encoding="utf-8") as archivo:
            datos_eventos = json.load(archivo)
            eventos = [Buscador(**datos_evento) for datos_evento in datos_eventos]
        return eventos


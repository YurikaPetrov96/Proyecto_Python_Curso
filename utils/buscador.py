import json

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

    def __str__(self):
        return f"Nombre: {self.nombre}\nArtista: {self.artista}\nGénero: {self.genero}\nUbicación: {self.ubicacion}\nHorario de inicio: {self.horario_ini}\nHorario de finalización: {self.horario_fin}\nDescripción: {self.descripcion}\nImagen: {self.imagen}\nFecha: {self.fecha}\nProvincia: {self.provincia}\n"

class Buscador:
    def __init__(self, eventos):
        self.eventos = eventos

    def buscar_por_palabra(self, palabra_clave):
        resultados = []
        for evento in self.eventos:
            if palabra_clave.lower() in str(evento).lower():
                resultados.append(evento)
        return resultados

class Filtros:
    def __init__(self, eventos):
        self.eventos = eventos

    def por_nombre(self, nombre):
        return self.filtrar_atributo("nombre", nombre.lower())

    def por_genero(self, genero):
        return self.filtrar_atributo("genero", genero.lower())

    def por_artista(self, artista):
        return self.filtrar_atributo("artista", artista.lower())

    def por_ubicacion(self, ubicacion):
        return self.filtrar_atributo("ubicacion", ubicacion.lower())

    def por_horario(self, horario_ini):
        return self.filtrar_atributo("horario_ini", horario_ini.lower())
    
    def filtrar_atributo(self, atributo, valor):
        resultados = []
        for evento in self.eventos:
            if hasattr(evento, atributo) and str(getattr(evento, atributo)).lower() == valor:
                resultados.append(evento)
        return resultados
    
def cargarjson(ruta_archivo_json):
    with open(ruta_archivo_json, 'r', encoding="utf-8") as archivo:
        datos_eventos = json.load(archivo)
        eventos = []
        for datos_evento in datos_eventos:
            evento = Evento(
                nombre=datos_evento.get('nombre', 'Nombre Desconocido'),
                artista=datos_evento.get('artista', 'Artista Desconocido'),
                genero=datos_evento.get('genero', 'Género Desconocido'),
                ubicacion=datos_evento.get('ubicacion', 'Ubicación Desconocida'),
                horario_ini=datos_evento.get('horario_ini', 'Horario Desconocido'),
                horario_fin=datos_evento.get('horario_fin', 'Horario Desconocido'),
                descripcion=datos_evento.get('descripcion', 'Descripción Desconocida'),
                imagen=datos_evento.get('imagen', 'Imagen Desconocida'),
                fecha=datos_evento.get('fecha', 'Fecha Desconocida'),
                provincia=datos_evento.get('provincia', 'Provincia Desconocida')
            )
            eventos.append(evento)
    return eventos

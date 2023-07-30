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
            return "No hay eventos registrados."
        else:
            eventos_lista = []
            for evento in self.eventos:
                evento_dict = {
                    "indice": evento['indice'],
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
                eventos_lista.append(evento_dict)
            return eventos_lista
import json

class Evento:
    def __init__(self, nombre, artista, genero, ubicacion, horario_ini, horario_fin, descripcion, imagen):
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.ubicacion = ubicacion
        self.horario_ini = horario_ini
        self.horario_fin = horario_fin
        self.descripcion = descripcion
        self.imagen = imagen

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
        self.eventos.append(evento.__dict__)
        self.guardar()

    def mostrar(self):
        if len(self.eventos) == 0:
            print("No hay eventos registrados")
        else:
            print("Eventos regitrados: ")
            for index, evento in enumerate(self.eventos, start = 1):
                print(f"Evento {index}:")
                print(f"Nombre: {evento['nombre']}")
                print(f"Artista: {evento['artista']}")
                print(f"Genero: {evento['genero']}")
                print(f"Ubicacion: {evento['ubicacion']}")
                print(f"Horario de inicio: {evento['horario inicio']}")
                print(f"Horario de finalizacion: {evento['horario fin']}")
                print(f"Horario de finalizacion: {evento['descripcion']}")
                print(f"Horario de finalizacion: {evento['imagen']}")

indice = Indice('basededatos.json')
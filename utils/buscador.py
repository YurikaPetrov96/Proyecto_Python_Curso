import json

class Buscador:
    def __init__(self, tipo, ingredientes, precios, calificacion, eventos):
        self.tipo = tipo
        self.ingredientes = ingredientes
        self.precios = precios
        self.calificacion = calificacion
        self.eventos = eventos

class Filtros:
    def __init__(self, destinos):
        self.destinos = destinos
    
    def por_tipo(self, tipo):
        resultados = []
        for destino in self.destinos:
            if destino.tipo == tipo:
                resultados.append(destino)
        return resultados
    
    def por_ingredientes(self, ingredientes):
        resultados = []
        for destino in self.destinos:
            if all(ingrediente in destino.ingredientes for ingrediente in ingredientes):
                resultados.append(destino)
        return resultados
    
    def por_precio(self, min_precio=0, max_precio=float('inf')):
        resultados = []
        for destino in self.destinos:
            if min_precio <= min(destino.precios) <= max_precio:
                resultados.append(destino)
        return resultados
    
    def por_calificacion(self, min_calificacion=0):
        resultados = []
        for destino in self.destinos:
            if destino.calificacion >= min_calificacion:
                resultados.append(destino)
        return resultados
    
    def por_eventos(self, extra=True):
        resultados = []
        for destino in self.destinos:
            if destino.eventos == extra:
                resultados.append(resultados)
        return resultados

def inicializar_buscador(ruta_json):
    with open("data/filters.json", 'r') as file:
        datos = json.load(file)

    destinos = []
    for restaurante in datos["restaurantes"]:
        destino = Buscador(restaurante["tipo"],
                                   restaurante["ingredientes"],
                                   restaurante["precios"],
                                   restaurante["calificacion"],
                                   restaurante["eventos"])
        destinos.append(destino)

    filtros = Filtros(destinos)
    return filtros

# Prueba del buscador
def ejecutar_buscador():
    ruta_json = r"c:\Users\HP\Desktop\prueba app jorge\buscador\data.json"
    filtros = inicializar_buscador(ruta_json)

    resultados_tipo = filtros.por_tipo("regional")
    resultados_ingredientes = filtros.por_ingredientes(["arroz"])
    resultados_precio = filtros.por_precio(300)
    resultados_calificacion = filtros.por_calificacion(4.7)
    resultados_eventos = filtros.por_eventos(True)

    print("Resultados del filtro por tipo:")
    for resultado in resultados_tipo:
        print(f"Tipo: {resultado.tipo}")

    print("Resultados del filtro por ingredientes:")
    for resultado in resultados_ingredientes:
        print(f"Ingredientes: {', '.join(resultado.ingredientes)}")

    print("Resultados del filtro por precio:")
    for resultado in resultados_precio:
        print(f"Precios: {', '.join(map(str, resultado.precios))}")

    print("Resultados del filtro por calificación:")
    for resultado in resultados_calificacion:
        print(f"Calificación: {resultado.calificacion}")

    print("Resultados del filtro por eventos:")
    for resultado in resultados_eventos:
        print(f"Evento: {resultado.eventos}")

# Ejecutar el buscador
ejecutar_buscador()


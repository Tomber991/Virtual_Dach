import json

def cargar_datos(archivo):
    try:
        with open(archivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def guardar_datos(archivo, datos):
    with open(archivo, 'w') as file:
        json.dump(datos, file, indent=4)
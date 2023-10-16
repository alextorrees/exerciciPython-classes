import json

import character

ruta_archivo = "StarWars.json"

def leer_archivo_json(ruta_archivo):
    with open(ruta_archivo, "r") as archivo:
        datos = json.load(archivo)

        return datos

def __init__():
    leer_archivo_json(ruta_archivo)
    character.print_info()
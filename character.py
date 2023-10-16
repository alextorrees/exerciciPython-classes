import json


class Character:
    ruta_archivo = "StarWars.json"

    def leer_archivo_json(ruta_archivo):
        with open(ruta_archivo, "r") as archivo:
            datos = json.load(archivo)
            return datos

    def __init__(self, datos):
        self.edited = datos['edited']
        self.name = datos['name']
        self.created = datos['created']
        self.gender = datos['gender']
        self.skin_color = datos['skin_color']
        self.hair_color = datos['hair_color']
        self.height = datos['height']
        self.eye_color = datos['eye_color']
        self.mass = datos['mass']
        self.home_world = datos['homeworld']
        self.birth_year = datos['birth_year']

    def print_info(self):
        character = self.name, self.gender, self.home_world, self.birth_year
        print(character)

import json
import os

from character import Character
from character_films import CharacterFilms


def load_characters(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)

    characters = []
    for item in data:
        character_data = item["fields"]
        character = CharacterFilms(**character_data)
        characters.append(character)
    return characters

def update_characters_info(characters):
    for character in characters:
        match character.name:
            case 'Luke Skywalker':
                character.num_of_films = 6
                character.first_film = 'Star Wars: Episodio IV - Una nueva esperanza'
                character.alive_at_the_end = False
            case 'Chewbacca':
                character.num_of_films = 5
                character.first_film = 'Star Wars: Episodio IV - Una nueva esperanza'
                character.alive_at_the_end = False
            case 'Anakin Skywalker':
                character.num_of_films = 5
                character.first_film = 'Star Wars: Episodio IV - Una nueva esperanza'
                character.alive_at_the_end = False

        print(f"Personaje --> {character.name}, {character.gender}, {character.home_world}, {character.birth_year}, {character.num_of_films}, {character.first_film}, {character.alive_at_the_end}")

def create_json_characters(characters):
    if os.path.exists('NewStarWars.json'):
        return True

    else:
        datos_json = json.dumps([character.__dict__ for character in characters])
        with open('NewStarWars.json', 'w') as archivo_json:
            archivo_json.write(datos_json)
            return False

def main():
    json_filename = 'StarWars.json'
    characters = load_characters(json_filename)

    update_characters_info(characters)
    if create_json_characters(characters) == True:
        print("Archivo Json ya fue creado")
    else:
        print("Archivo Json creado correctamente")

main()

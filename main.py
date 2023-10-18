import json


def read_characters():
    file = open('StarWars.json')
    data = json.load(file)
    for fields in data:
        print("Hola")
        for character in fields:
            print("Hola2")
            print(character.gender, character.home_world, character.birth_year)


def main():
    read_characters()


main()

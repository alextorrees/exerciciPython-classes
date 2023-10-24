from character import Character

class CharacterFilms(Character):
    def __init__(self, edited, name, created, gender, skin_color, hair_color, height, eye_color, mass, homeworld,
                 birth_year):
        super().__init__(edited, name, created, gender, skin_color, hair_color, height, eye_color, mass, homeworld,
                         birth_year)
        self._num_of_films = None
        self._first_film = None
        self._alive_at_the_end = None

    @property
    def num_of_films(self):
        return self._num_of_films

    @num_of_films.setter
    def num_of_films(self, num):
        self._num_of_films = num

    @property
    def first_film(self):
        return self._first_film

    @first_film.setter
    def first_film(self, film):
        self._first_film = film

    @property
    def alive_at_the_end(self):
        return self._alive_at_the_end

    @alive_at_the_end.setter
    def alive_at_the_end(self, alive):
        self._alive_at_the_end = alive

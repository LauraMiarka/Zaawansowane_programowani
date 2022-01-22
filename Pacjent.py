from Dieta import Dieta


class Pacjent:
    def __init__(self, imie: str, nazwisko: str,
                 id_pacjenta: int, id_diety: Dieta):
        self._imie = imie
        self._nazwisko = nazwisko
        self._id_pacjenta = id_pacjenta
        self._id_diety = id_diety

    def __str__(self):
        return f'Imię i nazwisko: {self._imie} ' \
               f'{self._nazwisko}, ' \
               f'ID: {self._id_pacjenta}, ' \
               f'Dieta: {self._id_diety}'

    @property
    def imie(self) -> str:
        return self._imie

    @imie.setter
    def imie(self, imie):
        self._imie = imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @nazwisko.setter
    def nazwisko(self, nazwisko):
        self._nazwisko = nazwisko

    @property
    def id_pacjenta(self) -> int:
        return self._id_pacjenta

    @id_pacjenta.setter
    def id_pacjenta(self, id_pacjenta):
        self._id_pacjenta = id_pacjenta

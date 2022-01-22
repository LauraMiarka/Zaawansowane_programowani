class Dietetyk:
    def __init__(self, imie_d: str, nazwisko_d: str,
                 id_dietetyka: int, nr_tel: str):
        self._imie_d = imie_d
        self._nazwisko_d = nazwisko_d
        self._id_dietetyka = id_dietetyka
        self._nr_tel = nr_tel

    def __str__(self):
        return f'Imię i nazwisko: {self._imie_d}' \
               f'{self._nazwisko_d}, ' \
               f'Nr telefonu: {self._nr_tel}' \
               f'Id: {self._id_dietetyka}'

    @property
    def imie_d(self) -> str:
        return self._imie_d

    @imie_d.setter
    def imie_d(self, imie_d):
        self._imie_d = imie_d

    @property
    def nazwisko_d(self) -> str:
        return self._nazwisko_d

    @nazwisko_d.setter
    def nazwisko_d(self, nazwisko_d):
        self._nazwisko_d = nazwisko_d

    @property
    def id_dietetyka(self) -> int:
        return self._id_dietetyka

    @id_dietetyka.setter
    def id_dietetyka(self, id_dietetyka):
        self._id_dietetyka = id_dietetyka

    @property
    def nr_tel(self) -> str:
        return self._nr_tel

    @nr_tel.setter
    def nr_tel(self, nr_tel):
        self._nr_tel = nr_tel

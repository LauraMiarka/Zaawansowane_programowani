from typing import Tuple


class Odcinek:

    def __init__(self, nazwa_odcinka: str,
                 kierunek: str,
                 punkt_a: Tuple[int, int],
                 punkt_b: Tuple[int, int]):
        self._nazwa_odcinka = nazwa_odcinka
        self._kierunek = kierunek
        self._punkt_a = punkt_a
        self._punkt_b = punkt_b

    def __str__(self):
        return f'Odcinek: {self._nazwa_odcinka}, ' \
               f'{self._kierunek},' \
               f'{self._punkt_a},' \
               f'{self._punkt_b}'

    @property
    def nazwa_odcinka(self) -> str:
        return self._nazwa_odcinka

    @nazwa_odcinka.setter
    def nazwa_odcinka(self, nazwa_odcinka: str):
        self._nazwa_odcinka = nazwa_odcinka

    @property
    def kierunek(self):
        return self._kierunek

    @kierunek.setter
    def kierunek(self, kierunek):
        self._kierunek = kierunek

    @property
    def punkt_a(self) -> Tuple[int, int]:
        return self._punkt_a

    @punkt_a.setter
    def punkt_a(self, punkt_a: Tuple[int, int]):
        self._punkt_a = punkt_a

    @property
    def punkt_b(self) -> Tuple[int, int]:
        return self._punkt_b

    @punkt_b.setter
    def punkt_b(self, punkt_b: Tuple[int, int]):
        self._punkt_b = punkt_b

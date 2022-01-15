from Pacjent import Pacjent
from Dieta import Dieta
from Dietetyk import Dietetyk


class Zamowienie:
    def __init__(self, zamowienie: int,
                 imie: Pacjent,
                 nazwisko: Pacjent,
                 id_dietetyka: Dietetyk,
                 id_diety: Dieta,
                 cena: Dieta,
                 il_kalorii: Dieta):
        self._zamowienie = zamowienie
        self._imie = imie
        self._nazwisko = nazwisko
        self._id_dietetyka = id_dietetyka
        self._id_diety = id_diety
        self._cena = cena
        self._il_kalorii = il_kalorii

    def __str__(self):
        return f'Zamowienie: {self._zamowienie}: ' \
               f'Pacjent: {self._imie} {self._nazwisko}, ' \
               f'dieta: {self._id_diety}, ' \
               f'cena: {self._cena}, ' \
               f'kalorie: {self._il_kalorii}'

    @property
    def zamowienie(self) -> int:
        return self._zamowienie

    @zamowienie.setter
    def zamowienie(self, zamowienie):
        self._zamowienie = zamowienie

    def suma_kcal(self) -> int:
        wynik_kalorie = 0
        for k in self._il_kalorii:
            wynik_kalorie = wynik_kalorie + k.il_kalorii
        return wynik_kalorie

    def suma_cena(self) -> float:
        wynik_cena = 0
        for c in self._cena:
            wynik_cena = wynik_cena + c.cena
        return round(wynik_cena, 2)

from typing import List

from Pojazd import Pojazd


class Firma:

    def __init__(self, nip: str,
                 nazwa_firmy: str,
                 zamowienie: str,
                 cel: str,
                 zasoby: List[Pojazd]):
        self._nip = nip
        self._nazwa_firmy = nazwa_firmy
        self._zamowienie = zamowienie
        self._cel = cel
        self._zasoby = zasoby

    def __str__(self):
        return f'Firma: {self._nip},' \
               f'{self._zasoby},' \
               f'{self._nazwa_firmy},' \
               f'{self._zamowienie},' \
               f'{self._cel}'

    @property
    def nip(self):
        return self._nip

    @nip.setter
    def nip(self, nip):
        self._nip = nip

    @property
    def nazwa_firmy(self):
        return self._nazwa_firmy

    @nazwa_firmy.setter
    def nazwa_firmy(self, nazwa_firmy):
        self._nazwa_firmy = nazwa_firmy

    @property
    def zamowienie(self):
        return self._zamowienie

    @zamowienie.setter
    def zamowienie(self, zamowienie):
        self._zamowienie = zamowienie

    @property
    def cel(self):
        return self._cel

    @cel.setter
    def cel(self, cel):
        self._cel = cel

    @property
    def zasoby(self):
        return self._zasoby

    @zasoby.setter
    def zasoby(self, zasoby):
        self._zasoby = zasoby

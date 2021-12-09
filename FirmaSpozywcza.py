from typing import List
from Pojazd import Pojazd
from Firma import Firma


class FirmaSpozywcza(Firma):

    def __init__(self, nip: str,
                 nazwa_firmy: str,
                 zamowienie: str,
                 cel: str,
                 zasoby: List[Pojazd],
                 kasjer: str):
        super(FirmaSpozywcza, self).__init__(nip,
                                             nazwa_firmy,
                                             zamowienie,
                                             cel,
                                             zasoby)
        self._kasjer = kasjer

    def __str__(self):
        return super(FirmaSpozywcza, self).__str__() + f',{self._kasjer}'

    @property
    def kasjer(self) -> str:
        return self._kasjer

    @kasjer.setter
    def kasjer(self, kasjer: str):
        self._kasjer = kasjer

from typing import List
from Pojazd import Pojazd
from Firma import Firma


class FirmaTransportowa(Firma):

    def __init__(self, nip: str,
                 nazwa_firmy: str,
                 zamowienie: str,
                 cel: str,
                 zasoby: List[Pojazd],
                 kierowca: str):
        super(FirmaTransportowa, self).__init__(nip,
                                                nazwa_firmy,
                                                zamowienie,
                                                cel,
                                                zasoby)
        self._kierowca = kierowca

    def __str__(self):
        return super(FirmaTransportowa, self).__str__() + f',{self._kierowca}'

    @property
    def kierowca(self) -> str:
        return self._kierowca

    @kierowca.setter
    def kierowca(self, kierowca: str):
        self._kierowca = kierowca

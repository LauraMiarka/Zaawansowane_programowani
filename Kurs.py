from Odcinek import Odcinek
from Firma import Firma
from Pojazd import Pojazd
from math import sqrt


class Kurs:
    def __init__(self,
                 pojazd: Pojazd,
                 odcinek: Odcinek,
                 firma_sp: Firma,
                 firma_tr: Firma):
        self._pojazd = pojazd
        self._odcinek = odcinek
        self._firma_sp = firma_sp
        self._firma_tr = firma_tr

    def __str__(self):
        return f'Kurs: {self._pojazd.marka},' \
               f'{self._odcinek.punkt_a},' \
               f'{self._odcinek.punkt_b},' \
               f'{self._firma_tr.nazwa_firmy},' \
               f'{self._firma_sp.nazwa_firmy}'

    def print_marka(self):
        return f'Marka pojazdu to: {self._pojazd.marka}'

    def odleglosc(self):
        return sqrt((self._odcinek.punkt_b[0]
                     - self._odcinek.punkt_a[0])**2
                    + ((self._odcinek.punkt_b[1]
                        - self._odcinek.punkt_a[1])**2))


pojazd_1 = Pojazd("Scania", "V8", 2011, "niebieski", 123)
odcinek_1 = Odcinek("odcinek_1", "płn", (23, 46), (67, 34))
firma_sp_1 = Firma("123456", "Firma spożywcza",
                   "pomarańcze", "odebranie dostawy",
                   [Pojazd("Scania", "V8", 2011, "niebieski", 123)])
firma_tr_1 = Firma("765432", "Firma transportowa",
                   "pomarańcze", "dostarczenie zamowienia", [pojazd_1])


k = Kurs(pojazd_1, odcinek_1, firma_sp_1, firma_tr_1)
print(k)
print(k.odleglosc())
print(k.print_marka())

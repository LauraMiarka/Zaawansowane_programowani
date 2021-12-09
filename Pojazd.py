class Pojazd:

    def __init__(self, marka: str,
                 model: str,
                 rocznik: int,
                 kolor: str,
                 max_predkosc: int):
        self._marka = marka
        self._rocznik = rocznik
        self._model = model
        self._kolor = kolor
        self._max_predkosc = max_predkosc

    def __str__(self):
        return f'Pojazd: {self._marka},' \
               f'{self._model},' \
               f'{self._rocznik},' \
               f'{self._kolor},' \
               f'{self._max_predkosc}.'

    @property
    def marka(self) -> str:
        return self._marka

    @marka.setter
    def marka(self, marka: str):
        self._marka = marka

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, model: str):
        self._model = model

    @property
    def rocznik(self) -> int:
        return self._rocznik

    @rocznik.setter
    def rocznik(self, rocznik: int):
        self._rocznik = rocznik

    @property
    def kolor(self) -> str:
        return self._kolor

    @kolor.setter
    def kolor(self, kolor: str):
        self._kolor = kolor

    @property
    def id_pojazdu(self) -> int:
        return self._max_predkosc

    @id_pojazdu.setter
    def id_pojazdu(self, max_predkosc: int):
        self._max_predkosc = max_predkosc

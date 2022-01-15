from Dietetyk import Dietetyk


class Dieta:
    def __init__(self, id_diety: int, cena: float,
                 id_dietetyka: Dietetyk, il_kalorii: int):
        self._id_diety = id_diety
        self._cena = cena
        self._id_dietetyka = id_dietetyka
        self._il_kalorii = il_kalorii

    def __str__(self):
        return f'Id: {self._id_diety}, ' \
               f'Cena: {self._cena}, ' \
               f'Dietetyk (id): {self._id_dietetyka}, ' \
               f'Kalorie: {self._il_kalorii}'

    @property
    def id_diety(self) -> int:
        return self._id_diety

    @id_diety.setter
    def id_diety(self, id_diety):
        self._id_diety = id_diety

    @property
    def cena(self) -> float:
        return self._cena

    @cena.setter
    def cena(self, cena):
        self._cena = cena

    @property
    def il_kalorii(self) -> int:
        return self.il_kalorii

    @il_kalorii.setter
    def il_kalorii(self, value):
        pass

class Pojazd:
    _marka: str
    _model: str
    _rocznik: int
    _kolor: str
    _id_pojazdu: int

    def __init__(self, _marka, _model, _rocznik, _kolor, _id_pojazdu):
        self._marka = _marka
        self._rocznik = _rocznik
        self._model = _model
        self._kolor = _kolor
        self._id_pojazdu = _id_pojazdu

    def __str__(self):
        return f'Pojazd: {self._marka},{self._model},{self._rocznik},{self._kolor},{self._id_pojazdu}.'

    @property
    def marka(self):
        return self._marka

    @marka.setter
    def marka(self, marka):
        self._marka = marka

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @property
    def rocznik(self):
        return self._rocznik

    @rocznik.setter
    def rocznik(self, rocznik):
        self._rocznik = rocznik

    @property
    def kolor(self):
        return self._kolor

    @kolor.setter
    def kolor(self, kolor):
        self._kolor =kolor

    @property
    def id_pojazdu(self):
        return self._id_pojazdu

    @id_pojazdu.setter
    def id_pojazdu(self, id_pojazdu):
        self._id_pojazdu = id_pojazdu


class FirmaSpozywcza(Pojazd):
    _id_firmysp: int
    _id_pojazdu: int
    _nazwaFirmySp: str
    _zamowienie: str
    _cel: float

    def __init__(self, _id_firmysp, _nazwaFirmySp, _zamowienie, _cel, _id_pojazdu):
        self._id_firmysp = _id_firmysp
        self._nazwaFirmySp = _nazwaFirmySp
        self._zamowienie = _zamowienie
        self._cel = _cel
        self._id_pojazdu = _id_pojazdu

    def __str__(self):
        return f'Firma spozywcza: {self._id_firmysp},{self._id_pojazdu},{self._nazwaFirmySp},{self._zamowienie},{self._cel}.'

    @property
    def id_firmysp(self):
        return self._id_firmysp

    @id_firmysp.setter
    def id_firmysp(self, id_firmysp):
        self._id_firmysp = id_firmysp

    @property
    def nazwaFirmySp(self):
        return self._nazwaFirmySp

    @nazwaFirmySp.setter
    def nazwaFirmySp(self, nazwaFirmySp):
        self._nazwaFirmySp = nazwaFirmySp

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
    def id_pojazdu(self):
        return self._id_pojazdu

    @id_pojazdu.setter
    def id_pojazdu(self, id_pojazdu):
        self._id_pojazdu = id_pojazdu


class FirmaTransportowa(FirmaSpozywcza, Pojazd):
    _id_firmyTr: str
    _id_pojazdu: int
    _godziny_pracy: str
    _miejsce_startowe: float
    _id_firmysp: int

    def __init__(self, _id_firmyTr, _godziny_pracy, _miejsce_startowe, _id_firmysp, _id_pojazdu):
        self._id_firmyTr = _id_firmyTr
        self._godziny_pracy = _godziny_pracy
        self._miejsce_startowe = _miejsce_startowe
        self._id_firmysp = _id_firmysp
        self._id_pojazdu = _id_pojazdu

    def __str__(self):
        return f'Odcinek: {self._id_firmyTr},{self._id_pojazdu},{self._godziny_pracy},{self._miejsce_startowe},{self._id_firmysp}.'

    @property
    def id_firmyTr(self):
        return self._id_firmyTr

    @id_firmyTr.setter
    def id_firmyTr(self, id_firmyTr):
        self._id_firmyTr = id_firmyTr

    @property
    def godziny_pracy(self):
        return self._godziny_pracy

    @godziny_pracy.setter
    def godziny_pracy(self, godziny_pracy):
        self._godziny_pracy = godziny_pracy

    @property
    def miejsce_startowe(self):
        return self._miejsce_startowe

    @miejsce_startowe.setter
    def id_odcinka(self, miejsce_startowe):
        self._miejsce_startowe = miejsce_startowe

    @property
    def id_pojazdu(self):
        return self._id_pojazdu

    @id_pojazdu.setter
    def id_pojazdu(self, id_pojazdu):
        self._id_pojazdu = id_pojazdu


class Odcinek(FirmaTransportowa):
    _nazwa_odcinka: str
    _miejsce_startowe: float
    _cel: float
    _czas: str
    _id_odcinka: int

    def __init__(self, _nazwa_odcinka, _czas, _id_odcinka, _miejsce_startowe, _cel):
        self._nazwa_odcinka = _nazwa_odcinka
        self._czas = _czas
        self._id_odcinka = _id_odcinka
        super().__init__(_miejsce_startowe, _cel)


    def __str__(self):
        return f'Odcinek: {self._nazwa_odcinka}, {self._miejsce_startowe},{self._cel},{self._czas},{self._id_odcinka}.'

    @property
    def nazwa_odcinka(self):
        return self._nazwa_odcinka

    @nazwa_odcinka.setter
    def nazwa_odcinka(self, nazwa_odcinka):
        self._nazwa_odcinka = nazwa_odcinka

    @property
    def miejsce_startowe(self):
        return self._miejsce_startowe

    @miejsce_startowe.setter
    def miejsce_startowe(self, miejsce_startowe):
        self._miejsce_startowe = miejsce_startowe

    @property
    def cel(self):
        return self._cel

    @cel.setter
    def cel(self, cel):
        self._cel = cel

    @property
    def czas(self):
        return self._czas

    @czas.setter
    def czas(self, czas):
        self._czas = czas

    @property
    def id_odcinka(self):
        return self._id_odcinka

    @id_odcinka.setter
    def id_odcinka(self, id_odcinka):
        self._id_odcinka = id_odcinka


class Kurs(Odcinek):
    _id_pojazdu: int
    _id_odcinka: int
    _id_kursu: int
    _id_firmysp: int
    _id_firmytr: int
    _miejsce_startowe: float
    _cel: float
    _marka: str

    def __init__(self, _id_pojazdu, _id_odcinka, _id_kursu, _id_firmysp, _id_firmytr, _miejsce_startowe, _cel, _marka):
        super().__init__(_id_pojazdu, _id_odcinka, _id_kursu, _id_firmysp, _id_firmytr, _miejsce_startowe, _cel, _marka)

    def __str__(self):
        return f'Kurs: {self._id_pojazdu}, {self._id_odcinka},{self._id_kursu},{self._id_firmysp},{self._id_firmytr}.'

    @property
    def id_pojazdu(self):
        return self._id_pojazdu

    @id_pojazdu.setter
    def id_pojazdu(self, id_pojazdu):
        self._id_pojazdu = id_pojazdu

    @property
    def id_odcinka(self):
        return self._id_odcinka

    @id_odcinka.setter
    def id_odcinka(self, id_odcinka):
        self._id_odcinka = id_odcinka

    @property
    def id_kursu(self):
        return self._id_kursu

    @id_kursu.setter
    def id_kursu(self, id_kursu):
        self._id_kursu = id_kursu

    @property
    def id_firmysp(self):
        return self._id_firmysp

    @id_firmysp.setter
    def id_firmysp(self, id_firmysp):
        self._id_firmysp = id_firmysp

    @property
    def id_firmytr(self):
        return self._id_firmytr

    @id_firmytr.setter
    def id_firmytr(self, id_firmytr):
        self._id_firmytr = id_firmytr

    @property
    def miejsce_startowe(self):
        return self._miejsce_startowe

    @miejsce_startowe.setter
    def miejsce_startowe(self, miejsce_startowe):
        self._miejsce_startowe = miejsce_startowe

    @property
    def cel(self):
        return self._cel

    @cel.setter
    def cel(self, cel):
        self._cel = cel

    @property
    def marka(self):
        return self._marka

    @marka.setter
    def marka(self, marka):
        self._marka = marka

    def sum(self) -> float:
        return self._cel - self._miejsce_startowe

    def marka(self) -> str:
        return self._marka


pojazd_1 = Pojazd("Scania", "V8", 2011, "niebieski", 123)
Firma_Sp_1 = FirmaSpozywcza(10, "Bagietka", "piewczywo", 86.23, 123)
Firma_Tr_1 = FirmaTransportowa(1, "6:00-21:00", 25.63, 10, 123)
odcinek_1 = Odcinek("trasa_1", "2h", 4,25.63,86.23)
kurs_1 = Kurs(123, 4, 99, 10, 1)

print(kurs_1.marka())
print(kurs_1.sum())

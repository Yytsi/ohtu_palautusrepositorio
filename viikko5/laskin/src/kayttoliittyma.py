from enum import Enum
from tkinter import ttk, constants, StringVar

class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class KomentoOlio:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote
        self._edellinen_arvo = 0

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_arvo)

class Summa(KomentoOlio):
    def suorita(self):
        self._edellinen_arvo = self._sovelluslogiikka.tulos
        arvo = self._lue_syote()
        self._sovelluslogiikka.plus(arvo)

class Erotus(KomentoOlio):
    def suorita(self):
        self._edellinen_arvo = self._sovelluslogiikka.tulos
        arvo = self._lue_syote()
        self._sovelluslogiikka.miinus(arvo)

class Nollaus(KomentoOlio):
    def suorita(self):
        self._edellinen_arvo = self._sovelluslogiikka.tulos
        self._sovelluslogiikka.nollaa()

class Kumoa(KomentoOlio):
    def suorita(self):
        self.kumoa()

class Kayttoliittyma:
    def __init__(self, sovellus, root):
        self._sovellus = sovellus
        self._root = root
        self._edellinen_komento = None

        self._komennot = {
            Komento.SUMMA: Summa(sovellus, self._lue_syote),
            Komento.EROTUS: Erotus(sovellus, self._lue_syote),
            Komento.NOLLAUS: Nollaus(sovellus, self._lue_syote),
            Komento.KUMOA: Kumoa(sovellus, self._lue_syote)
        }

    def _lue_syote(self):
        return int(self._syote_kentta.get())

    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovellus.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _suorita_komento(self, komento):
        if komento == Komento.KUMOA and self._edellinen_komento:
            self._edellinen_komento.kumoa()
            self._edellinen_komento = None
        else:
            komento_olio = self._komennot[komento]
            komento_olio.suorita()
            if komento != Komento.KUMOA:
                self._edellinen_komento = komento_olio

        self._paivita_kayttoliittyma()

    def _paivita_kayttoliittyma(self):
        self._tulos_var.set(self._sovellus.tulos)
        self._kumoa_painike["state"] = constants.NORMAL if self._edellinen_komento else constants.DISABLED
        self._nollaus_painike["state"] = constants.NORMAL if self._sovellus.tulos != 0 else constants.DISABLED
        self._syote_kentta.delete(0, constants.END)
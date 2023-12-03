KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self._tarkista_kapasiteetti(kapasiteetti)
        self._tarkista_kasvatuskoko(kasvatuskoko)

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = [0] * kapasiteetti
        self.alkioiden_lkm = 0

    def _tarkista_kapasiteetti(self, kapasiteetti):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise ValueError("Väärä kapasiteetti")

    def _tarkista_kasvatuskoko(self, kasvatuskoko):
        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise ValueError("Väärä kasvatuskoko")

    def kuuluu(self, n):
        return n in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, n):
        if not self.kuuluu(n):
            if self.alkioiden_lkm == len(self.ljono):
                self.ljono += [0] * self.kasvatuskoko
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            return True
        return False

    def poista(self, n):
        if n in self.ljono:
            self.ljono.remove(n)
            self.ljono.append(0)
            self.alkioiden_lkm -= 1
            return True
        return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        for numero in a.to_int_list() + b.to_int_list():
            yhdiste.lisaa(numero)
        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        for numero in a.to_int_list():
            if numero in b.to_int_list():
                leikkaus.lisaa(numero)
        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        for numero in a.to_int_list():
            erotus.lisaa(numero)
        for numero in b.to_int_list():
            erotus.poista(numero)
        return erotus

    def __str__(self):
        alkiot = self.to_int_list()
        if not alkiot:
            return "{}"
        return "{" + ", ".join(map(str, alkiot)) + "}"

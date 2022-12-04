KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetin täytyy olla epänegatiivinen kokonaisluku")
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.lukujono = [None for luku in range(self.kapasiteetti)]
        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        if self.lukujono.count(luku) > 0:
            return True
        return False

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            self.lukujono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm == len(self.lukujono):
                taulukko_old = self.lukujono.copy()
                self.lukujono = [None for i in range(self.alkioiden_lkm + self.kasvatuskoko)]
                self.kopioi_taulukko(taulukko_old, self.lukujono)

            return True

        return False

    def poista(self, luku):
        loytyi = False

        for alkio in self.lukujono[:self.alkioiden_lkm]:
            if luku == alkio:
                kohta = self.lukujono.index(alkio)
                loytyi = True
            
        if loytyi:
            self.lukujono.pop(kohta)
            self.lukujono.append(None)
            self.alkioiden_lkm -= 1
            return True

        return False

    def kopioi_taulukko(self, a, b):
        for i in range(len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.lukujono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        a_joukko = a.to_int_list()
        b_joukko = b.to_int_list()

        for alkio in a_joukko:
            yhdiste.lisaa(alkio)

        for alkio in b_joukko:
            yhdiste.lisaa(alkio)

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        a_joukko = a.to_int_list()
        b_joukko = b.to_int_list()

        for i in range(len(a_joukko)):
            for j in range(len(b_joukko)):
                if a_joukko[i] == b_joukko[j]:
                    leikkaus.lisaa(b_joukko[j])

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        a_joukko = a.to_int_list()
        b_joukko = b.to_int_list()

        for alkio in a_joukko:
            erotus.lisaa(alkio)
        for alkio in b_joukko:
            erotus.poista(alkio)

        return erotus

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        else:
            tuotos = ", ".join(str(alkio) for alkio in self.lukujono[:self.alkioiden_lkm])
            return "{" + tuotos + "}"

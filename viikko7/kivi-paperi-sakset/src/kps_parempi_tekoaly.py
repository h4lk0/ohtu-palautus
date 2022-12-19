from kivipaperisakset import KiviPaperiSakset
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KiviPaperiSakset):
    def _alusta(self):
        self._tekoaly = TekoalyParannettu(10)
        self._ensimmainen_peli = True

    def _toinen_siirto(self, ensimmainen_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        if not self._ensimmainen_peli:
            self._tekoaly.aseta_siirto(ensimmainen_siirto)
        self._ensimmainen_peli = False
        return tokan_siirto
from kivipaperisakset import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toinen_siirto(self, ensimmainen_siirto):
        tokan_siirto = input("Toisen pelaajan siirto: ")
        return tokan_siirto
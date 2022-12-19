from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly

class Pelitehdas:
    def __init__(self):
        pass
    
    @staticmethod
    def luo(komento):
        komennot = {
            "a": KPSPelaajaVsPelaaja(),
            "b": KPSTekoaly(),
            "c": KPSParempiTekoaly()
        }
        return komennot[komento]


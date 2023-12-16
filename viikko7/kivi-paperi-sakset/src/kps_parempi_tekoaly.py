from tekoaly_parannettu import TekoalyParannettu
from kps_peli import KPSPeli


class KPSParempiTekoaly(KPSPeli):
    def __init__(self) -> None:
        self._pelaaja = TekoalyParannettu(10)
    
    def anna_siirto(self):
        return self._pelaaja.anna_siirto()

    def aseta_siirto(self, ekan_siirto):
        return self._pelaaja.aseta_siirto(ekan_siirto)



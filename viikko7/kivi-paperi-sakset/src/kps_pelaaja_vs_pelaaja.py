from kps_peli import KPSPeli

class KPSPelaajaVsPelaaja(KPSPeli):
    def __init__(self) -> None:
        self._pelaaja = None

    def anna_siirto(self):
        return input("Toisen pelaajan siirto: ")

    def __str__(self) -> str:
        return "Toinen pelaaja"

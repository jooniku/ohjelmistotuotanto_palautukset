from tuomari import Tuomari
from kps_peli import KPSPeli

class KPSPelaajaVsPelaaja(KPSPeli):
    def __init__(self) -> None:
        self._pelaaja = None
        
    def pelaa1(self):
        tuomari = Tuomari()

        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = input("Toisen pelaajan siirto: ")

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = input("Toisen pelaajan siirto: ")

        print("Kiitos!")
        print(tuomari)

    def anna_siirto(self):
        return input("Toisen pelaajan siirto: ")

    def __str__(self) -> str:
        return "Toinen pelaaja"

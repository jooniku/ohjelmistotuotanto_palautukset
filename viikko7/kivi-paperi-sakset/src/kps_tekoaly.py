from tuomari import Tuomari
from tekoaly import Tekoaly
from kps_peli import KPSPeli


class KPSTekoaly(KPSPeli):
    def __init__(self) -> None:
        self._pelaaja = Tekoaly()

    def pelaa1(self):
        tuomari = Tuomari()
        tekoaly = Tekoaly()

        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = tekoaly.anna_siirto()

            print(f"Tietokone valitsi: {tokan_siirto}")

        print("Kiitos!")
        print(tuomari)
    
    def anna_siirto(self):
        return "k"

    def __str__(self) -> str:
        return "Tietokone"


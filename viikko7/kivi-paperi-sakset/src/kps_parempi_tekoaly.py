from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from kps_peli import KPSPeli


class KPSParempiTekoaly(KPSPeli):
    def __init__(self) -> None:
        self._pelaaja = TekoalyParannettu(10)

    def pelaa1(self):
        tuomari = Tuomari()
        tekoaly = TekoalyParannettu(10)

        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = tekoaly.anna_siirto()

            print(f"Tietokone valitsi: {tokan_siirto}")
            tekoaly.aseta_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)
    
    def anna_siirto(self):
        self._pelaaja.anna_siirto()

    def aseta_siirto(self, ekan_siirto):
        self._pelaaja.aseta_siirto(ekan_siirto)

    def __str__(self) -> str:
        return "Tietokone"


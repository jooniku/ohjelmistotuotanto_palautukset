from tuomari import Tuomari


class KPSPeli:
    def __init__(self, vastustaja) -> None:
        self._tuomari = Tuomari()
        self._vastustaja = vastustaja

    def pelaa(self):
        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = self._vastustaja.anna_siirto()

        print(f"{self._vastustaja} valitsi: {tokan_siirto}")

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(self._tuomari)

            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = self._vastustaja.anna_siirto()

            #print(f"{self._vastustaja} valitsi: {tokan_siirto}")
            self._vastustaja.aseta_siirto(ekan_siirto)

        print("Kiitos!")
        print(self._tuomari)

    def anna_siirto(self):
        return
    
    def kirjaa_siirto(self):
        return
    
    def aseta_siirto(self, ekan_siirto):
        return
            
    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
    

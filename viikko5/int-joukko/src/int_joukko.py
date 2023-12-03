KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        """Luo lista annetulla kapasiteetilla.
        Aseta kasvatuskooksi annettu koko.
        """
        try:
            self.ljono = self._luo_lista(kapasiteetti)
            self.kasvatuskoko = kasvatuskoko
            
        except TypeError as error:
            print("Pitää käyttää luonnollisia lukuja")
            
        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        return luku in self.ljono

    def taynna(self):
        return self.alkioiden_lkm == len(self.ljono)

    def lisaa(self, luku):
        """Lisää alkio listaan jos ei jo listassa.
        Jos lista täynnä, luo uusi lista,
        missä vanhat alkiot.
        """
        if not self.kuuluu(luku=luku):
            self.ljono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm += 1

            if self.taynna():
                self.laajenna_lista()

            return True
        return False
    
    
    def laajenna_lista(self):
        """Lisää vanhan listan alkiot
        uuteen listaan ja aseta uusi lista päälistaksi.
        """
        taulukko_old = self.ljono
        self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi(taulukko_old, self.ljono)


    def etsi_luku(self, luku):
        """Etsi annettu luku listasta.
        Jos ei löydy, palauta -1.
        """
        for indeksi in range(self.mahtavuus()):
            if luku == self.ljono[indeksi]:
                return indeksi
        return -1

    def poista(self, luku):
        """Jos luku listassa, poista
        luku ja päivitä lista oikein.
        """
        if self.kuuluu(luku=luku):
            luvun_indeksi = self.etsi_luku(luku=luku)
            self.ljono[luvun_indeksi] = 0
            self.alkioiden_lkm -= 1

            self.siirra_listaa(luvun_indeksi)

            return True
        return False

    def siirra_listaa(self, alku_indeksi):
        """Siirrä listaa alkuindeksin
        kohdalta taaksepäin yhden alkion verran.
        """
        for indeksi in range(alku_indeksi, len(self.ljono)-1):
            self.ljono[indeksi] = self.ljono[indeksi + 1]


    def kopioi(self, kopioitava, tulos_lista):
        """Kopioi 'kopioitava' listan alkiot
        listaan 'tulos_lista'
        """
        if len(kopioitava) > len(tulos_lista):
            raise "Kopioitavan listan tulee olla lyhyempi tai saman pituinen"
        
        for kopioitava_i in range(len(kopioitava)):
            tulos_lista[kopioitava_i] = kopioitava[kopioitava_i]


    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        """Palauttaa pelkät numerot listana
        ilman loppuja 0-merkkejä.
        """
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(taulu_1, taulu_2):
        """Palauttaa taulun, missä on 
        taulu_1 ja taulu_2 alkiot siten,
        että ensin taulu_1.
        """
        super_lista = taulu_1.to_int_list() + taulu_2.to_int_list()

        tulos_taulu = IntJoukko(kapasiteetti=len(super_lista))
        
        for indeksi in range(len(super_lista)):
            tulos_taulu.lisaa(super_lista[indeksi])
        
        return tulos_taulu


    @staticmethod
    def leikkaus(taulu_1, taulu_2):
        """Palauttaa taulun, missä on
        ne alkiot, mitkä esiintyvät
        molemmissa tauluissa.
        """
        tulos_taulu = IntJoukko()

        jono_1 = taulu_1.to_int_list()

        for luku in jono_1:
            if taulu_2.kuuluu(luku):
                tulos_taulu.lisaa(luku=luku)

        return tulos_taulu
    

    @staticmethod
    def erotus(taulu_1, taulu_2):
        """Palauttaa taulun, missä
        on ne alkiot, mitkä ovat
        taulu_1:ssä, mutta ei taulu_2:ssa.
        """
        tulos_taulu = IntJoukko()

        jono_1 = taulu_1.to_int_list()

        for luku in jono_1:
            if not taulu_2.kuuluu(luku):
                tulos_taulu.lisaa(luku=luku)

        return tulos_taulu

    def __str__(self):
        """Palauttaa jonon merkkiesityksenä.
        """
        jono = [str(numero) for numero in self.ljono[:self.alkioiden_lkm]]
        return f"{{{', '.join(jono)}}}"
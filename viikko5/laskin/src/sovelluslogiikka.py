class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._muisti = [arvo]

    def nollaa(self):
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo
        self._muisti.append(arvo)

    def arvo(self):
        return self._arvo
    
    def kumoa(self):
        self._muisti = self._muisti[:-1]
        self.aseta_arvo(self._muisti[-1])

class Algebra:
    def __init__(self, sovellus, io) -> None:
        self.sovellus = sovellus
        self.io = io

    def suorita(self):
        return 0
    
    def _hae_arvo(self):
        return int(self.io())
    
class Summa(Algebra):
    def __init__(self, sovellus, io) -> None:
        super().__init__(sovellus, io)
    
    def suorita(self):
        self.sovellus.aseta_arvo(self.sovellus.arvo() + self._hae_arvo())
    
class Erotus(Algebra):
    def __init__(self, sovellus, io) -> None:
        super().__init__(sovellus, io)
    
    def suorita(self):
        self.sovellus.aseta_arvo(self.sovellus.arvo() - self._hae_arvo())
    
class Muu:
    def __init__(self, sovellus) -> None:
        self.sovellus = sovellus
    
    def suorita(self):
        return 0
    
class Nollaus(Muu):
    def __init__(self, sovellus) -> None:
        super().__init__(sovellus)

    def suorita(self):
        self.sovellus.nollaa()
    
class Kumoa(Muu):
    def __init__(self, sovellus) -> None:
        super().__init__(sovellus)

    def suorita(self):
        self.sovellus.kumoa()
from tekoaly import Tekoaly
from kps_peli import KPSPeli


class KPSTekoaly(KPSPeli):
    def __init__(self) -> None:
        self._pelaaja = Tekoaly()

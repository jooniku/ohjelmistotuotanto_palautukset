from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_peli import KPSPeli

class PeliTehdas:

    @staticmethod
    def luo_peli(pelityyli: str):
        pelityypit = {"a": KPSPelaajaVsPelaaja(),
                    "b": KPSTekoaly(),
                    "c": KPSParempiTekoaly()}
        
        vastustaja = pelityypit.get(pelityyli, None)

        if vastustaja is None:
            raise InvalidGame
        return KPSPeli(vastustaja)



class InvalidGame(Exception):
    def __str__(self) -> str:
        return "Vääränlainen syöte pelityypin valinnassa\n"
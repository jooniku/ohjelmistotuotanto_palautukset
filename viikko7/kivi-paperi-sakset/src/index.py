from pelitehdas import PeliTehdas, InvalidGame

def main():
    while True:

        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()


        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
        try:
            peli = PeliTehdas.luo_peli(pelityyli=vastaus)
            peli.pelaa()
        except InvalidGame as e:
            print("Hei hei!")
            break
        


if __name__ == "__main__":
    main()

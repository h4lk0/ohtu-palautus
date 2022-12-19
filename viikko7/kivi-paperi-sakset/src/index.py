from pelitehdas import Pelitehdas


def main():
    vaihtoehdot = ["a", "b", "c"]
    pelitehdas = Pelitehdas()

    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus[-1] in vaihtoehdot:
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            pelitehdas.luo(vastaus[-1]).pelaa()
        else:
            break


if __name__ == "__main__":
    main()

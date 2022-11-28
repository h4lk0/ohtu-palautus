# testikoodi tänne jos tarvetta
from ostoskori import Ostoskori
from tuote import Tuote

def main():
    kori = Ostoskori()
    maito = Tuote("Maito", 3)
    juusto = Tuote("Juusto", 2)
    kori.lisaa_tuote(maito)
    kori.lisaa_tuote(juusto)
    maito2 = Tuote("Maito", 3)
    kori.lisaa_tuote(maito2)
    print(kori.hinta())
    print(kori.tavaroita_korissa())
    print(len(kori.ostokset()))

main()
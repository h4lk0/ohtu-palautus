import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_tuotteen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        leipa = Tuote("Leipä", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_jalkeen_hinta_on_tuotteiden_summa(self):
        maito = Tuote("Maito", 3)
        leipa = Tuote("Leipä", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)

        self.assertEqual(self.kori.hinta(), 5)

    def test_kahden_saman_tuotteen_jalkeen_korissa_kaksi_tavaraa(self):
        maito1 = Tuote("Maito", 3)
        maito2 = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito1)
        self.kori.lisaa_tuote(maito2)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_saman_tuotteen_jalkeen_korin_hinta_sama_kuin_tuotteen_hinta_tuplana(self):
        maito1 = Tuote("Maito", 3)
        maito2 = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito1)
        self.kori.lisaa_tuote(maito2)

        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostoksia = self.kori.ostokset()
        ostos = ostoksia[0]

        self.assertEqual(len(ostoksia), 1)
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")

    def test_kahden_eri_tuotteen_jalkeen_korissa_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        leipa = Tuote("Leipä", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 2)

    def test_kahden_saman_tuotteen_jalkeen_korissa_yksi_ostos(self):
        maito1 = Tuote("Maito", 3)
        maito2 = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito1)
        self.kori.lisaa_tuote(maito2)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
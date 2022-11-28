import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 3)
        self.leipa = Tuote("Leipä", 2)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_tuotteen(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_jalkeen_hinta_on_tuotteiden_summa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)

        self.assertEqual(self.kori.hinta(), 5)

    def test_kahden_saman_tuotteen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_saman_tuotteen_jalkeen_korin_hinta_sama_kuin_tuotteen_hinta_tuplana(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.maito)
        ostoksia = self.kori.ostokset()
        ostos = ostoksia[0]

        self.assertEqual(len(ostoksia), 1)
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")

    def test_kahden_eri_tuotteen_jalkeen_korissa_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 2)

    def test_kahden_saman_tuotteen_jalkeen_korissa_yksi_ostos(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_jalkeen_ostoksella_tuotteen_nimi_ja_oikea_lukumaara(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        ostokset = self.kori.ostokset()
        ostos = ostokset[0]

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        self.assertEqual(ostos.tuotteen_nimi(), self.maito.nimi())

    def test_kahden_saman_tuotteen_ja_toisen_poiston_jalkeen_ostosten_lukumaara_yksi(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.kori.poista_tuote(self.maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.assertEqual(len(ostokset), 1)

    def test_tuotteen_lisayksen_ja_saman_poiston_jalkeen_tyhja_kori(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.poista_tuote(self.maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(ostokset), 0)

    def test_korin_tyhjennys_toimii(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)
        self.kori.tyhjenna()

        ostokset = self.kori.ostokset()

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(ostokset), 0)         
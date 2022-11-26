import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

        self.viitegeneraattori_mock.uusi.return_value = 42

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 5
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "juusto", 4)
            if tuote_id == 3:
                return Tuote(3, "jauheliha", 6)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_osto_kutsuu_pankin_tilisiirtoa_oikeilla_arvoilla(self):

        self.viitegeneraattori_mock.uusi.return_value = 67
        
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("jussi", "67890")

        self.pankki_mock.tilisiirto.assert_called_with("jussi", 67, "67890", "33333-44455", 5)

    def test_kahden_ostoksen_summa_on_oikein(self):

        self.viitegeneraattori_mock.uusi.return_value = 19

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("maija", "23456")

        self.pankki_mock.tilisiirto.assert_called_with("maija", 19, "23456", "33333-44455", 9)

    def test_loppunutta_tuotetta_ei_veloiteta(self):

        self.viitegeneraattori_mock.uusi.return_value = 98

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("paavo", "56789")

        self.pankki_mock.tilisiirto.assert_called_with("paavo", 98, "56789", "33333-44455", 4)

    def test_tuotteen_poisto_toimii(self):

        self.viitegeneraattori_mock.uusi.return_value = 35

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("veijo", "23567")

        self.pankki_mock.tilisiirto.assert_called_with("veijo", 35, "23567", "33333-44455", 4)
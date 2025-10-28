import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uuden_varaston_tilavuus_ei_mene_negatiiviseksi(self):
        varasto = Varasto(-10, 2)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_uuden_varaston_alkusaldo_nollaantuu(self):
        varasto = Varasto(10, -5)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_uusi_varasto_ei_ylitayty(self):
        varasto = Varasto(10, 11)
        self.assertAlmostEqual(varasto.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varastoon_ei_lisata_negatiivista(self):
        vanha_saldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-5)

        # saldon ei pitäisi muuttua
        self.assertAlmostEqual(self.varasto.saldo, vanha_saldo)

    def test_varastoa_ei_voi_tayttaa_liikaa(self):
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_varastosta_ei_voi_ottaa_negatiivista_maaraa(self):
        otettu_maara = self.varasto.ota_varastosta(-10)
        self.assertAlmostEqual(otettu_maara, 0)

    def test_varastosta_ei_voi_ottaa_saldoa_enempaa(self):
        self.varasto.lisaa_varastoon(5)
        otettu_maara = self.varasto.ota_varastosta(8)

        self.assertAlmostEqual(otettu_maara, 5)

    def test_varasto_merkkijono_palautuu_oikein(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
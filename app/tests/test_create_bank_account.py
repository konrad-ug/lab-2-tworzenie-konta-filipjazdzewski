import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"

    correct_pesel = "99111900536"
    incorrect_pesel = "12345"
    pesel_before_1961 = "57052603699"

    valid_coupon = "PROM_XYZ"
    invalid_coupon = "PROMXYZ"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.correct_pesel, self.name, self.surname)
        self.assertEqual(pierwsze_konto.pesel, self.correct_pesel, "Pesel nie został zapisany!")
        self.assertEqual(pierwsze_konto.imie, self.name, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.surname, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        
    def test_pesel_lenght_is_not_correct(self):
        drugie_konto = Konto(self.incorrect_pesel, self.name, self.surname)
        self.assertEqual(drugie_konto.pesel, "Niepoprawny pesel!",
            "Pesel nie posiada wartości 'Niepoprawny pesel', przy podaniu niepoprawnego peselu!")
            
    def test_saldo_with_valid_coupon(self):
        konto_z_valid_coupon = Konto(self.correct_pesel, self.name, self.surname, self.valid_coupon)
        self.assertEqual(konto_z_valid_coupon.saldo, 50, "Wartość salda nie równa się 50, mimo użycia poprawnego kuponu!")

    def test_saldo_with_invalid_coupon(self):
        konto_z_invalid_coupon = Konto(self.correct_pesel, self.name, self.surname, self.invalid_coupon)
        self.assertEqual(konto_z_invalid_coupon.saldo, 0, "Wartość salda nie równa się 0, mimo użycia niepoprawnego kuponu lub braku kuponu!")

    def test_if_coupon_is_valid_for_people_born_after_1960(self):
        konto_staruszka = Konto(self.pesel_before_1961, self.name, self.surname, self.valid_coupon)
        self.assertEqual(konto_staruszka.saldo, 0, "Kupon nie jest ważny dla osób urodzonych po 1960 roku!")
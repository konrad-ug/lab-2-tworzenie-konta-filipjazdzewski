import unittest

from ..Account import Account

class TestCreateBankAccount(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"

    correct_pesel = "99111900536"
    incorrect_pesel = "12345"
    pesel_before_1961 = "57052603699"
    pesel_after_2000 = "02222607061"

    valid_coupon = "PROM_XYZ"
    invalid_coupon = "PROMXYZ"

    def test_create_account(self):
        first_account = Account(self.correct_pesel, self.name, self.surname)
        self.assertEqual(first_account.pesel, self.correct_pesel, "Pesel nie został zapisany!")
        self.assertEqual(first_account.name, self.name, "Imie nie zostało zapisane!")
        self.assertEqual(first_account.surname, self.surname, "Nazwisko nie zostało zapisane!")
        self.assertEqual(first_account.balance, 0, "Saldo nie jest zerowe!")
        
    def test_pesel_lenght_is_not_correct(self):
        second_account = Account(self.incorrect_pesel, self.name, self.surname)
        self.assertEqual(second_account.pesel, "Niepoprawny pesel!",
            "Pesel nie posiada wartości 'Niepoprawny pesel!', przy podaniu niepoprawnego peselu!")
            
    def test_saldo_with_valid_coupon(self):
        account_with_valid_coupon = Account(self.correct_pesel, self.name, self.surname, self.valid_coupon)
        self.assertEqual(account_with_valid_coupon.balance, 50, "Wartość salda nie równa się 50, mimo użycia poprawnego kuponu!")

    def test_saldo_with_invalid_coupon(self):
        account_with_invalid_coupon = Account(self.correct_pesel, self.name, self.surname, self.invalid_coupon)
        self.assertEqual(account_with_invalid_coupon.balance, 0, "Wartość salda nie równa się 0, mimo użycia niepoprawnego kuponu lub braku kuponu!")

    def test_if_coupon_is_valid_for_people_born_after_1960(self):
        elder_account = Account(self.pesel_before_1961, self.name, self.surname, self.valid_coupon)
        self.assertEqual(elder_account.balance, 0, "Kupon nie jest ważny dla osób urodzonych po 1960 roku!")

    def test_if_coupon_is_valid_for_people_born_after_2000(self):
        youth_account = Account(self.pesel_after_2000, self.name, self.surname, self.valid_coupon)
        self.assertEqual(youth_account.balance, 50, "Kupon powinien być ważny dla ludzi po 1960 roku!")

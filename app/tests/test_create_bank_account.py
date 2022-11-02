import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class TestCreateBankAccount(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"

    correct_pesel = "99111900536"
    incorrect_pesel = "12345"
    pesel_before_1961 = "57052603699"
    pesel_after_2000 = "02222607061"

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
            "Pesel nie posiada wartości 'Niepoprawny pesel!', przy podaniu niepoprawnego peselu!")
            
    def test_saldo_with_valid_coupon(self):
        konto_z_valid_coupon = Konto(self.correct_pesel, self.name, self.surname, self.valid_coupon)
        self.assertEqual(konto_z_valid_coupon.saldo, 50, "Wartość salda nie równa się 50, mimo użycia poprawnego kuponu!")

    def test_saldo_with_invalid_coupon(self):
        konto_z_invalid_coupon = Konto(self.correct_pesel, self.name, self.surname, self.invalid_coupon)
        self.assertEqual(konto_z_invalid_coupon.saldo, 0, "Wartość salda nie równa się 0, mimo użycia niepoprawnego kuponu lub braku kuponu!")

    def test_if_coupon_is_valid_for_people_born_after_1960(self):
        konto_staruszka = Konto(self.pesel_before_1961, self.name, self.surname, self.valid_coupon)
        self.assertEqual(konto_staruszka.saldo, 0, "Kupon nie jest ważny dla osób urodzonych po 1960 roku!")

    def test_if_coupon_is_valid_for_people_born_after_2000(self):
        konto_gen_z = Konto(self.pesel_after_2000, self.name, self.surname, self.valid_coupon)
        self.assertEqual(konto_gen_z.saldo, 50, "Kupon powinien być ważny dla ludzi po 1960 roku!")


class TestBookingMoneyTransfers(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "99111900536"
    valid_coupon = "PROM_ABC"

    nazwa = "Dunder Mifflin Paper Company"
    valid_nip = "8858910020"

    def test_if_valid_transfer_changes_saldo(self):
        pierwsze_konto = Konto(self.pesel, self.name, self.surname, self.valid_coupon)
        pierwsze_konto.TransferMoney(30)
        self.assertEqual(pierwsze_konto.saldo, 20, 
            "Saldo powinno wynosić 20 po wysłaniu 30!")

    def test_if_invalid_transfer_changes_saldo(self):
        drugie_konto = Konto(self.pesel, self.name, self.surname, self.valid_coupon)
        drugie_konto.TransferMoney(200)
        self.assertEqual(drugie_konto.saldo, 50, 
            "Wartość salda powinna pozostać ta sama (50) po próbie wysłania wyższej wartości niż posiadana!")

    def test_if_receive_money_changes_saldo(self):
        trzecie_konto = Konto(self.pesel, self.name, self.surname, self.valid_coupon)
        trzecie_konto.ReceiveMoney(1000)
        self.assertEqual(trzecie_konto.saldo, 1050,
            "Wartość salda powinna wynosić 1050 po przyjęciu 1000!")

    # Valid ExpressTransfer for normal bank account
    def test_saldo_of_normal_account_after_valid_express_transfer(self):
        first_normal_acc = Konto(self.pesel, self.name, self.surname)
        first_normal_acc.saldo = 100
        first_normal_acc.ExpressTransfer(100)
        self.assertEqual(first_normal_acc.saldo, -1, "Wartość salda nie wynosi -1 po poprawnym przelewie ekspresowym!")

    # Invalid ExpressTransfer for normal bank account
    def test_saldo_of_normal_account_after_invalid_express_transfer(self):
        second_normal_acc = Konto(self.pesel, self.name, self.surname)
        second_normal_acc.saldo = 100
        second_normal_acc.ExpressTransfer(101)
        self.assertEqual(second_normal_acc.saldo, 100, "Wartość salda nie pozostala 100 po niepoprawnym przelewie ekspresowym!")

    # Valid ExpressTransfer for company bank account
    def test_saldo_of_company_account_after_valid_express_transfer(self):
        first_company_acc = KontoFirmowe(self.valid_nip, self.nazwa)
        first_company_acc.saldo = 100
        first_company_acc.ExpressTransfer(100)
        self.assertEqual(first_company_acc.saldo, -5, "Wartość salda nie wynosi -5 po poprawnym przelewie ekspresowym!")

    # Invalid ExpressTransfer for company bank account
    def test_saldo_of_company_account_after_invalid_express_transfer(self):
        second_company_acc = KontoFirmowe(self.valid_nip, self.nazwa)
        second_company_acc.saldo = 100
        second_company_acc.ExpressTransfer(101)
        self.assertEqual(second_company_acc.saldo, 100, "Wartość salda nie wynosi 100 po niepoprawnym przelewie ekspresowym!")

class TestCreateCompanyBankAccount(unittest.TestCase):
    nazwa = "Dunder Mifflin Paper Company"
    valid_nip = "8858910020"
    invalid_nip = "211337"

    def test_create_company_account(self):
        first_account = KontoFirmowe(self.valid_nip, self.nazwa)
        self.assertEqual(first_account.nazwa, self.nazwa, "Nazwa firmy nie została zapisana!")
        self.assertEqual(first_account.nip, self.valid_nip, "Nip nie został zapisany!")
        self.assertEqual(first_account.saldo, 0, "Wartość salda nie wynosi 0!")

    def test_nip_length_is_not_correct(self):
        second_account = KontoFirmowe(self.invalid_nip, self.nazwa)
        self.assertEqual(second_account.nip, "Niepoprawny NIP!", 
            "Nip nie posiada wartości 'Niepoprawny NIP!', przy podaniu niepoprawnego nipu!")

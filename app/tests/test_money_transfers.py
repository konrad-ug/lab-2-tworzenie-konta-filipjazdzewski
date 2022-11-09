import unittest

from ..Account import Account
from ..CompanyAccount import CompanyAccount

class TestBookingMoneyTransfers(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "99111900536"
    valid_coupon = "PROM_ABC"

    companyName = "Dunder Mifflin Paper Company"
    valid_nip = "8858910020"

    def test_if_valid_transfer_changes_saldo(self):
        first_account = Account(self.pesel, self.name, self.surname, self.valid_coupon)
        first_account.TransferMoney(30)
        self.assertEqual(first_account.balance, 20, 
            "Saldo powinno wynosić 20 po wysłaniu 30!")

    def test_if_invalid_transfer_changes_saldo(self):
        second_account = Account(self.pesel, self.name, self.surname, self.valid_coupon)
        second_account.TransferMoney(200)
        self.assertEqual(second_account.balance, 50, 
            "Wartość salda powinna pozostać ta sama (50) po próbie wysłania wyższej wartości niż posiadana!")

    def test_if_receive_money_changes_saldo(self):
        third_account = Account(self.pesel, self.name, self.surname, self.valid_coupon)
        third_account.ReceiveMoney(1000)
        self.assertEqual(third_account.balance, 1050,
            "Wartość salda powinna wynosić 1050 po przyjęciu 1000!")

    # Valid ExpressTransfer for normal bank account
    def test_saldo_of_normal_account_after_valid_express_transfer(self):
        first_normal_acc = Account(self.pesel, self.name, self.surname)
        first_normal_acc.balance = 100
        first_normal_acc.ExpressTransfer(100)
        self.assertEqual(first_normal_acc.balance, -1, "Wartość salda nie wynosi -1 po poprawnym przelewie ekspresowym!")

    # Invalid ExpressTransfer for normal bank account
    def test_saldo_of_normal_account_after_invalid_express_transfer(self):
        second_normal_acc = Account(self.pesel, self.name, self.surname)
        second_normal_acc.balance = 100
        second_normal_acc.ExpressTransfer(101)
        self.assertEqual(second_normal_acc.balance, 100, "Wartość salda nie pozostala 100 po niepoprawnym przelewie ekspresowym!")

    # Valid ExpressTransfer for company bank account
    def test_saldo_of_company_account_after_valid_express_transfer(self):
        first_company_acc = CompanyAccount(self.valid_nip, self.companyName)
        first_company_acc.balance = 100
        first_company_acc.ExpressTransfer(100)
        self.assertEqual(first_company_acc.balance, -5, "Wartość salda nie wynosi -5 po poprawnym przelewie ekspresowym!")

    # Invalid ExpressTransfer for company bank account
    def test_saldo_of_company_account_after_invalid_express_transfer(self):
        second_company_acc = CompanyAccount(self.valid_nip, self.companyName)
        second_company_acc.balance = 100
        second_company_acc.ExpressTransfer(101)
        self.assertEqual(second_company_acc.balance, 100, "Wartość salda nie wynosi 100 po niepoprawnym przelewie ekspresowym!")

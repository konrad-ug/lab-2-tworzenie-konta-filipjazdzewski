import unittest

from ..CompanyAccount import CompanyAccount

class TestCreateCompanyBankAccount(unittest.TestCase):
    companyName = "Dunder Mifflin Paper Company"
    valid_nip = "8858910020"
    invalid_nip = "211337"

    def test_create_company_account(self):
        first_account = CompanyAccount(self.valid_nip, self.companyName)
        self.assertEqual(first_account.companyName, self.companyName, "Nazwa firmy nie została zapisana!")
        self.assertEqual(first_account.nip, self.valid_nip, "Nip nie został zapisany!")
        self.assertEqual(first_account.balance, 0, "Wartość salda nie wynosi 0!")

    def test_nip_length_is_not_correct(self):
        second_account = CompanyAccount(self.invalid_nip, self.companyName)
        self.assertEqual(second_account.nip, "Niepoprawny NIP!", 
            "Nip nie posiada wartości 'Niepoprawny NIP!', przy podaniu niepoprawnego nipu!")
            
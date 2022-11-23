import unittest
from parameterized import parameterized

from ..Account import Account
from ..CompanyAccount import CompanyAccount

class TestTakingOutALoan(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "99111900536"

    company_name = "Dunder Mifflin Paper Company"
    nip = "8858910020"

    def setUp(self):
        self.account = Account(self.pesel, self.surname, self.name)
        self.company_account = CompanyAccount(self.nip, self.company_name)
        

    @parameterized.expand([
        ([-100, 100, 100, 100, 600], 500, True, 500), 
        ([-10000, 100, 100, 100, 600], 300, False, 0),
        ([10000, -100, 0, 100, 600], 300, False, 0),
        ([10000, -100, -100, 100, 600], 300, False, 0),
        ([300, 100, 600], 300, False, 0),
        ([], 10, False, 0),
    ])

    def test_take_out_a_loan(self, history, amount, expected_result, expected_balance):
        self.account.history = history
        is_granted = self.account.TakeOutALoan(amount)
        self.assertEqual(is_granted, expected_result)
        self.assertEqual(self.account.balance, expected_balance, "The loan has not been granted properly!")

    @parameterized.expand([
        ([1775, 2000, -1775], 2000, 900, True, 2900), 
        ([1775, 2000, -1775], 2000, 1000, False, 2000), 
        ([1775, 2000, -1775], 2000, 1500, False, 2000), 
        ([1775, 2000, 2000], 5775, 500, False, 5775), 
        ([1775, 2000, 1000], 4775, 3000, False, 4775), 
        ([], 2000, 500, False, 2000),
    ])

    def test_take_out_a_loan_company(self, history, balance, amount, expected_result, expected_balance):
        self.company_account.history = history
        self.company_account.balance = balance
        is_granted = self.company_account.TakeOutALoan(amount)
        self.assertEqual(is_granted, expected_result)
        self.assertEqual(self.company_account.balance, expected_balance, "The loan has not been granted properly!")

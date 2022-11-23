import unittest
from parameterized import parameterized

from ..Account import Account

class TestTakingOutALoan(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "99111900536"

    def setUp(self):
        self.account = Account(self.pesel, self.surname, self.name)

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

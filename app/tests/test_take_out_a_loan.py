import unittest

from ..Account import Account

class TestTakingOutALoan(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "99111900536"

    def test_5_incoming_transfers(self):
        account = Account(self.pesel, self.surname, self.name)
        account.history = [-100, 100, 100, 100, 600]
        is_granted = account.TakeOutALoan(500)
        self.assertTrue(is_granted)
        self.assertEqual(account.balance, 500)

    def test_5_incoming_transfers_too_little_sum(self):
        account = Account(self.pesel, self.surname, self.name)
        account.history = [-10000, 100, 100, 100, 600]
        is_granted = account.TakeOutALoan(500)
        self.assertFalse(is_granted)
        self.assertEqual(account.balance, 0)

    def test_last_3_transfers_not_all_positive(self):
        account = Account(self.pesel, self.surname, self.name)
        account.history = [10000, -100, 0, 100, 600]
        is_granted = account.TakeOutALoan(500)
        self.assertFalse(is_granted)
        self.assertEqual(account.balance, 0)

    def test_history_length_below_5(self):
        account = Account(self.pesel, self.surname, self.name)
        account.history = [100, 300, 100, 600]
        is_granted = account.TakeOutALoan(500)
        self.assertFalse(is_granted)
        self.assertEqual(account.balance, 0)
        
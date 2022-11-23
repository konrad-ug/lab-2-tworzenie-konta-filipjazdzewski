from .Account import Account

class CompanyAccount(Account):
    def __init__(self, nip, companyName):
        self.companyName = companyName
        self.balance = 0
        self.expressTransferCost = 5
        self.history = []
        self.NipValidation(nip)

    def NipValidation(self, nip):
        self.nip = nip if len(nip) == 10 else 'Niepoprawny NIP!'

    def balance_is_2_times_greater_than_loan(self, amount):
        return True if self.balance > amount * 2 else False

    def at_least_one_ZUS_transfer(self):
        return True if -1775 in self.history else False
 
    def check_the_terms_of_taking_out_a_loan_are_met(self, amount):
        if self.balance_is_2_times_greater_than_loan(amount) and self.at_least_one_ZUS_transfer():
            return True
        return False

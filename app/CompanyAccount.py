from .Account import Account

class CompanyAccount(Account):
    def __init__(self, nip, companyName):
        self.companyName = companyName
        self.balance = 0
        self.NipValidation(nip)

    def NipValidation(self, nip):
        self.nip = nip if len(nip) == 10 else 'Niepoprawny NIP!'

    def ExpressTransfer(self, amount):
        if (self.balance - amount >= 0):
            self.balance -= amount + 5
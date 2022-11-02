from .Konto import Konto

class KontoFirmowe(Konto):
    def __init__(self, nip, nazwa):
        self.nazwa = nazwa
        self.saldo = 0
        self.NipValidation(nip)

    def NipValidation(self, nip):
        self.nip = nip if len(nip) == 10 else 'Niepoprawny NIP!'

    def ExpressTransfer(self, amount):
        if (self.saldo - amount - 5 >= -5):
            self.saldo -= amount + 5
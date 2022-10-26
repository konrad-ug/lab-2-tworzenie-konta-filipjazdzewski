class Konto:
    def __init__(self, pesel, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.checkPeselValidation(pesel)
        
    def checkPeselValidation(self, pesel):
        self.pesel = pesel if len(pesel) == 11 else 'Niepoprawny pesel!'

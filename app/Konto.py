from tkinter.filedialog import SaveFileDialog

class Konto:
    def __init__(self, pesel, imie, nazwisko, coupon=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.checkPeselValidation(pesel)
        self.checkCouponValidation(coupon)
        
    def checkPeselValidation(self, pesel):
        self.pesel = pesel if len(pesel) == 11 else 'Niepoprawny pesel!'

    def checkCouponValidation(self, coupon):
        if (coupon != None and coupon.startswith("PROM_") and len(coupon) == 8):
            self.saldo += 50

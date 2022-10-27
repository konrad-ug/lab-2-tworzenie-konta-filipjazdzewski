from tkinter.filedialog import SaveFileDialog

class Konto:
    def __init__(self, pesel, imie, nazwisko, coupon=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.checkPeselValidation(pesel)
        self.checkCouponValidation(coupon)
        
    def checkPeselValidation(self, pesel):
        self.pesel = pesel if len(pesel) == 11 else 'Niepoprawny pesel!'

    def checkCouponValidation(self, coupon):
        isCouponValid = coupon != None and coupon.startswith("PROM_") and len(coupon) == 8
        isUserYoungEnough = self.pesel != "Niepoprawny pesel!" and (int(self.pesel[0:2]) > 60 or int(self.pesel[2:4]) > 20)
        if (isCouponValid and isUserYoungEnough):
            self.saldo = 50
        else:
            self.saldo = 0

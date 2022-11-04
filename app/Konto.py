class Konto:
    def __init__(self, pesel, imie, nazwisko, coupon=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.PeselValidation(pesel)
        self.CouponValidation(coupon)
        
    def PeselValidation(self, pesel):
        self.pesel = pesel if len(pesel) == 11 else 'Niepoprawny pesel!'

    def CouponValidation(self, coupon):
        isCouponValid = coupon != None and coupon.startswith("PROM_") and len(coupon) == 8
        isUserYoungEnough = self.pesel != "Niepoprawny pesel!" and (int(self.pesel[0:2]) > 60 or int(self.pesel[2:4]) > 20)
        if (isCouponValid and isUserYoungEnough):
            self.saldo = 50
        else:
            self.saldo = 0

    def TransferMoney(self, kwotaDoWyslania):
        if (self.saldo > kwotaDoWyslania):
            self.saldo -= kwotaDoWyslania

    def ReceiveMoney(self, kwotaDoOtrzymania):
        self.saldo += kwotaDoOtrzymania

    def ExpressTransfer(self, amount):
        if (self.saldo - amount - 1 >= -1):
            self.saldo -= amount + 1
        
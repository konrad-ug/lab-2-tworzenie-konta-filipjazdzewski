class Account:
    def __init__(self, pesel, name, surname, coupon=None):
        self.name = name
        self.surname = surname
        self.expressTransferCost = 1
        self.history = []
        self.PeselValidation(pesel)
        self.CouponValidation(coupon)
        
    def PeselValidation(self, pesel):
        self.pesel = pesel if len(pesel) == 11 else 'Niepoprawny pesel!'

    def CouponValidation(self, coupon):
        isCouponValid = coupon != None and coupon.startswith("PROM_") and len(coupon) == 8
        isUserYoungEnough = self.pesel != "Niepoprawny pesel!" and (int(self.pesel[0:2]) > 60 or int(self.pesel[2:4]) > 20)
        if (isCouponValid and isUserYoungEnough):
            self.balance = 50
        else:
            self.balance = 0

    def TransferMoney(self, amount):
        if (self.balance > amount):
            self.balance -= amount
            self.history.append(-amount)

    def ReceiveMoney(self, amount):
        self.balance += amount
        self.history.append(amount)

    def ExpressTransfer(self, amount):
        if (self.balance - amount >= 0):
            self.balance -= amount + self.expressTransferCost
            self.history.append(-self.expressTransferCost)
            self.history.append(-amount)

    def TakeOutALoan(self, amount):
        if len(self.history) < 5:
            return False
        if self.history[-3] > 0 and self.history[-2] > 0 and self.history[-1] > 0 and sum(self.history[-5:]) > amount:
            self.balance += amount
            return True
        return False
        
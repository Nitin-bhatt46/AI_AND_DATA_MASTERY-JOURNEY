class CreditCard:
    def amount(self,amount):
        print("Thank you for your credit card payment")


class UPI:
    def amount(self,amount):
        print("Thank you for your UPI payment")

class Cash:
    def amount(self,amount):
        print("Thank you for your cash payment")


for i in [CreditCard(), UPI(), Cash()]:
    i.amount(1000)


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited!")

a = BankAccount("Nitin", 1000)
a.deposit(2000)

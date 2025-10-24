class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        cash=int(input("enter the amount : "))
        self.balance=self.balance+cash


    def withdraw(self):
        cash=int(input("enter the amount : "))
        if cash<self.balance:
            print(f"Remaining balance is {self.balance}")
        else:
            print(f"Withdrawal failed due to insufficient balance")

    def show_balance(self):
        print(self.balance)

nitin = BankAccount("Nitin",100)
nitin.show_balance()
nitin.deposit()
nitin.show_balance()
nitin.withdraw()
nitin.show_balance()


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_balance(self):
        return self.balance


    def set_balance(self, amount):
        self.balance += amount

        return self.balance

nitin=BankAccount("Nitin",1000)
print(nitin.get_balance())
print(nitin.set_balance(1000))
print(nitin.get_balance())

# without encapsulation.

print(nitin.balance)



# WITH CAPSULATION.



class BankAccount2:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance


    def get_balance(self):
       return self.__balance

    def set_balance(self, amount):

        self.__balance += amount
        return self.__balance


nitin=BankAccount2("Nitin",1000)
print(nitin.get_balance())
print(nitin.set_balance(1000))
print(nitin.get_balance())

# with encapsulation.

print(nitin.__balance)


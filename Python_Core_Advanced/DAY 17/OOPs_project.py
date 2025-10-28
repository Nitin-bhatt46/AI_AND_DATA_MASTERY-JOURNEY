class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Encapsulation

    def get_salary(self):
        return self.__salary

    def set_salary(self, bonus):
        self.__salary += bonus

    def display(self):
        print(f"{self.name} earns ₹{self.get_salary()}")


class Manager(Employee):
    def __init__(self, department, name, salary):
        self.department = department
        super().__init__(name, salary)

        ## super is used to access the parent class attributes and method super().__int__(), or super().display()

    def display(self):
        print(f"{self.name} (Manager - {self.department}) earns ₹{self.get_salary()}")


class CreditCard:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card ")


class UPI:
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI ")


class Cash:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash ")


emp1 = Employee("John", 50000)
man1 = Manager("Finance", "Martin", 100000)

emp1.set_salary(5000)
man1.set_salary(20000)

emp1.display()
man1.display()

payment_emp1 = CreditCard()
payment_emp1.pay(emp1.get_salary())

payment_man1 = Cash()
payment_man1.pay(man1.get_salary())


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

# self is the cruical for identifying the current object.
  
    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        self.__salary += amount

## so, salary is private we cannot change it morally. if hr wants to change we can give access to him like this.


emp1=Employee("Alice", 50000)
emp1.get_salary()
emp1.set_salary(1000)
print(emp1.get_salary())

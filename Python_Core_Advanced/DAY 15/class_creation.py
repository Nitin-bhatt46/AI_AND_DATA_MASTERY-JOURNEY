class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"{self.name} earns {self.salary}")

arun = Employee("Arun", 20000)

arun.display()



## going into depth


class Employee:
    def __init__(self,name, salary):
        self.employee_name = name
        self.employee_salary = salary

    def display(self):
        print(f"{self.employee_name} earns ₹{self.employee_salary}")

arun = Employee("Aman", 50000)
arun.display()

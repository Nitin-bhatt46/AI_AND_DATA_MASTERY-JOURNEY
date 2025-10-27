class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    department = "Finance"

    def show_info(self):
        print(self.name, self.salary,self.department)


emp1 = Manager("John", 500000)
emp1.show_info()

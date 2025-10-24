
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade

    def get_grade(self):
        return self.__grade

std = Student("Nitin",100)
print(std.get_grade())

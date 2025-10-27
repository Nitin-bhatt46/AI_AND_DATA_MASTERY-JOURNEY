class Vehicle:
    def move(self):
        print("Moving")

class Car(Vehicle):
    def wheels(self):
        print("4 wheels")

c = Car()
c.move()
c.wheels()

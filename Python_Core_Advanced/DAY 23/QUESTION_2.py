# simple way 
# longest way 
from  turtle import Turtle, Screen


t = Turtle()

t.shape("arrow")

t.color("red","blue")

for i in range(3):
    t.left(120)
    t.forward(100)

for i in range(4):
    t.left(90)
    t.forward(100)


for i in range(5):
    t.left(72)
    t.forward(100)

for i in range(6):
    t.left(60)
    t.forward(100)


for _ in range(7):
    t.left(51.42)
    t.forward(100)


for _ in range(8):
    t.left(45)
    t.forward(100)


for _ in range(9):
    t.left(40)
    t.forward(100)

for _ in range(10):
    t.left(36)
    t.forward(100)


screen= Screen()
screen.exitonclick()


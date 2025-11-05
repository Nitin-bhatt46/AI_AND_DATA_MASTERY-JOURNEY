# shortest way 

import random
from  turtle import Turtle, Screen


t = Turtle()

t.shape("arrow")

colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'black', 'orange']

def draw(num_sides):
    angle =360/num_sides
    for i in range(num_sides):
        t.forward(100)
        t.left(angle)

for shape_sides in range(3,11):
    t.color(random.choice(colors))
    draw(shape_sides)
screen= Screen()
screen.exitonclick()

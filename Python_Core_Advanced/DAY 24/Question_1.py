"""
Draw random walk
"""
import random
from  turtle import Turtle, Screen


t = Turtle()

t.shape("arrow")
t.speed(0)
colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'black', 'orange']
direction=[ 0,90,180,270,360]
t.pensize(10)
def draw(num_sides):
    for i in range(num_sides):
        t.color(random.choice(colors))
        t.forward(20)
        t.right(random.choice(direction))


draw(500)



screen= Screen()
screen.exitonclick()

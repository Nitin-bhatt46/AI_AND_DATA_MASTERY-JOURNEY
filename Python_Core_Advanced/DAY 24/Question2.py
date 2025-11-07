"""
Draw random walk with color creation.
"""
import random
import turtle


t = turtle.Turtle()

t.shape("arrow")
t.speed(0)
turtle.colormode(255)
direction=[ 0,90,180,270]
t.pensize(10)
def draw(num_sides):
    for i in range(num_sides):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        t.color((r,g,b))
        t.forward(20)
        t.setheading(random.choice(direction))


draw(200)



screen= turtle.Screen()
screen.exitonclick()

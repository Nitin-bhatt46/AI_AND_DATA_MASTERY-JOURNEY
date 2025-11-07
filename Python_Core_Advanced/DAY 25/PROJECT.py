"""
creating a spirograph
"""
import random
import turtle

t = turtle.Turtle()
t.shape("arrow")
t.speed(0)
turtle.colormode(255)
t.teleport(y=-20,x=-20)


t.pensize(1)
def draw(n):
    for i in range(1,n):
        for _ in range(1,n):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            t.color((r, g, b))
            t.begin_fill()
            t.circle(5)
            t.end_fill()
            t.penup()
            t.forward(50)
            t.pendown()
        t.penup()
        t.left(90)
        t.forward(50)
        t.left(90)
        for j in range(1,n):
             t.forward(50)
        t.setheading(0)



draw(7)

screen= turtle.Screen()
screen.exitonclick()

"""
creating a spirograph
"""
import random
import turtle

t = turtle.Turtle()
t.shape("arrow")
t.speed(0)
turtle.colormode(255)
color_list=[ "red", "blue", "green", "yellow", "black", "pink", "gray"]

t.pensize(1)

def draw_s(gap_size):
    for _ in range(int(360 / gap_size)):
        t.color(random.choice(color_list))
        t.circle(100)
        t.setheading(t.heading() + gap_size)


draw_s(8)


screen= turtle.Screen()
screen.exitonclick()

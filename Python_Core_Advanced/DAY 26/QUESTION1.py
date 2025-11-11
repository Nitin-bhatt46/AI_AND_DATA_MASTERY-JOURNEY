from turtle import Turtle, Screen

t=Turtle()
screen = Screen()
t.setheading(90)
t.speed(0)

def move_upward():
    t.forward(100)

screen.listen()
screen.onkey(key="space",fun=move_upward)

screen.exitonclick()

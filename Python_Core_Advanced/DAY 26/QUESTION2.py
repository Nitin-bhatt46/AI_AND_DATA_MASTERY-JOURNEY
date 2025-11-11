from turtle import Turtle, Screen

t=Turtle()
screen = Screen()
t.setheading(90)
t.speed(0)

def move_upward():
    t.forward(100)
    t.setheading(90)
def move_backward():
    t.right(180)
    t.forward(100)
    t.setheading(90)
def move_left():
    t.left(90)
    t.forward(100)
    t.setheading(90)
def move_right():
    t.right(90)
    t.forward(100)
    t.setheading(90)

screen.listen()
screen.onkey(key="w",fun=move_upward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=move_left)
screen.onkey(key="d",fun=move_right)
screen.exitonclick()

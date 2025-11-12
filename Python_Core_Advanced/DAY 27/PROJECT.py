from turtle import Turtle, Screen

t=Turtle()
screen = Screen()




def move_upward():
    t.forward(20)


def move_backward():
    t.backward(20)


def counter_clockwise():
    new_heading = t.heading() + 10
    t.setheading(new_heading)

def clockwise():
    new_heading = t.heading() - 10
    t.setheading(new_heading)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(key="w",fun=move_upward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=counter_clockwise)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="c",fun=clear)
screen.exitonclick()

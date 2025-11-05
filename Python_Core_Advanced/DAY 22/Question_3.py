from  turtle import Turtle, Screen

def star():
    for _ in range(5):
        our_turtle.forward(100)
        our_turtle.right(144)

our_turtle = Turtle()

our_turtle.shape("turtle")

our_turtle.color("red","blue")

star()


screen= Screen()
screen.exitonclick()

from  turtle import Turtle, Screen

def draw_square():
    for _ in range(4):
        our_turtle.forward(100)
        our_turtle.right(90)

our_turtle = Turtle()

our_turtle.shape("turtle")

our_turtle.color("red","blue")

draw_square()

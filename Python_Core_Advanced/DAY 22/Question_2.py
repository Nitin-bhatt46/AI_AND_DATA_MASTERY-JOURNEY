from  turtle import Turtle, Screen

def draw_equilateral_triangle():
    for _ in range(3):
        our_turtle.forward(100)
        our_turtle.left(120)

our_turtle = Turtle()

our_turtle.shape("turtle")

our_turtle.color("red","blue")

draw_equilateral_triangle()

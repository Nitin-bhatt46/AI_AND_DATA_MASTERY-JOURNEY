from turtle import Turtle, Screen
# creating and giving color
t1=Turtle()
t1.color('red')
t2=Turtle()
t2.color('blue')
t3=Turtle()
t2.color('green')
t4=Turtle()
t4.color('yellow')
screen = Screen()

# giving shape
def shape_u(x):
    t1.shape(x)
    t2.shape(x)
    t3.shape(x)
    t4.shape(x)
shape_u('turtle')

# making them unable to write.
t1.penup()
t2.penup()
t3.penup()
t4.penup()
# placing them 

# making them to start frm beginning
t1.backward(300)
t2.backward(300)
t3.backward(300)
t4.backward(300)
# upward palceing.
t1.left(90)
t1.forward(200)
t1.right(90)
t2.left(90)
t2.forward(100)
t2.right(90)
 downward placing.
t4.right(90)
t4.forward(100)
t4.left(90)
# printing in screen 
screen.exitonclick()

from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = False


screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which Turtle will win the race ?  Enter a color: ")

color=['red','yellow','blue','green','purple','orange','pink']

corodinate=[-60,-30,0,30,60,90]

all_turtles = []

for i in range(0,6):
    t = Turtle(shape='turtle')
    t.color(color[i])
    t.penup()
    t.goto(-240,corodinate[i])
    all_turtles.append(t)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                is_race_on = False
                print(f"You won the {winning_color} turtle")
            else:
                print(f"You Lost! the {winning_color} turtle won the race")
                is_race_on = False

        else:
            random_distance =(random.randint(0,10))
            turtle.forward(random_distance)





screen.exitonclick()

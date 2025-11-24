# creating a pong Game.
from turtle import Screen
import creation
from ball import Ball
import time
from Score_board import Scoreboard

# screen object
s = Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
s.title("Pong")
'''
# It Stop the animation to get animation back we need to use
# Use update method to get the animation back.
'''
s.tracer(0)

# paddle object

p1 = creation.paddle_creation(xcor=350,ycor=0)
p2 = creation.paddle_creation(xcor=-350,ycor=0)
ball = Ball()
scoreboard = Scoreboard()

s.listen()
s.onkey(p1.up, "Up")
s.onkey(p1.down, "Down")
s.onkey(p2.up, "w")
s.onkey(p2.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()
    # detect the collision

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncey()
    # detect collision
    if ball.distance(p1) < 50 and ball.xcor() > 320 or ball.distance(p2) < 50 and ball.xcor() < -320 :
        ball.bouncex()

    # ball missed by the padel
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



s.exitonclick()

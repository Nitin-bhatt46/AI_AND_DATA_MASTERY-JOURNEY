"""
CREATE A SNAKE BODY
MOVE THE SNAKE
CREATE SNAKE FOOD
DETECT COLLISION WITH FOOD
CREATE AS SCOREBOARD
DETECT COLLISION WITH WALL
DETECT COLLISION WITH WALL

"""

from turtle import Screen
import snake_make
import time

s = Screen()
s.setup(600, 600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = snake_make.Snake()

game_is_on = True

while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()


s.exitonclick()

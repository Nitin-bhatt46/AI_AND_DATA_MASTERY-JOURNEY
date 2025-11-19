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
from food import Food
from score_board import ScoreBoard

s = Screen()
s.setup(600, 600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = snake_make.Snake()
food = Food()
scoreboard = ScoreBoard()

s.listen()

s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()


    #collision.

    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments:

        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()




s.exitonclick()






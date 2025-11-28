from player import Player
from turtle import Screen
from car_manager import CarManager
from score_board import Scoreboard
import time



s=Screen()
s.setup(600,600)
s.tracer(0)
p=Player()
car_manager=CarManager()
scoreboard=Scoreboard()


s.listen()
s.onkey(p.up,'Up')
s.onkey(p.down,'Down')



game_is_on =True
while game_is_on:
    s.update()
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.move_cars()

    # detection of car collision
    for x in car_manager.all_cars:
        #  it gives distance between turtles.
        if x.distance(p)< 20:
            game_is_on=False
            scoreboard.game_over()
    # detecting turtle with finsih line.
    if p.is_at_finsih_line():
        p.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()



s.exitonclick()

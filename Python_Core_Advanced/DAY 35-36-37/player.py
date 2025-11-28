from turtle import Turtle


STARTING_POINT = (0,-280)
MOVE_DISTANCE = 20
FINISH_LINE = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POINT)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.backward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POINT)




    def is_at_finsih_line(self):
        if self.ycor()>FINISH_LINE:
            return True
        else:
            return False

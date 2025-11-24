from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_movement = 10
        self.y_movement = 10
        self.move_speed =0.1

    def move(self):
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)

    def bouncey(self):
        self.y_movement *= -1
        self.move_speed *= 0.9

    def bouncex(self):
        self.x_movement *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed =0.1
        self.bouncex()

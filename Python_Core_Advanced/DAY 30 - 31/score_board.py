from turtle import Turtle
FONT = ('Courier', 20, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-50, 270)
        self.update_score()


    def update_score(self):
        self.write(f"Score: {self.score}", move=False, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER ", move=False,align="center", font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

from turtle import Turtle
FONT = ('Ariel', 15, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', 'r') as file:
            data = int(file.read())

        self.high_score = data
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} highest score : {self.high_score}",align='center', move=False, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()


    def increase_score(self):
        self.score += 1
        self.update_score()

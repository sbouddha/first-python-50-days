from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore=int(self.read_file())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def read_file(self):
        with open("data.txt") as file:
            past_high_score=file.read()
            if past_high_score:
                return past_high_score
            else:
                return 0

    def write_file(self,new_highscore):
        new_highscore=str(new_highscore)
        with open("data.txt", mode="w") as file:
            file.write(new_highscore)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            self.write_file(self.highscore)
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


 
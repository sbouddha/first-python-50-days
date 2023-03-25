from turtle import Turtle
ALIGNMENT="center"
FONT=('Ariel', 12, 'bold')

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score_value=0
        self.penup()
        self.hideturtle()
        self.goto(0,380)
        self.color("white")
        self.write(f"Score : {self.score_value}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over !!!", False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score_value +=1
        self.write(f"Score : {self.score_value}", False, align=ALIGNMENT, font=FONT)


from turtle import Turtle
ALIGNMENT="center"
FONT=('Ariel', 50, 'normal')

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-150,200)
        self.write(f"{self.l_score}", False, align=ALIGNMENT, font=FONT)
        self.goto(150,200)
        self.write(f"{self.r_score}", False, align=ALIGNMENT, font=FONT)

    def increase_score_l(self):
        self.l_score +=1
        self.update_scoreboard()    
        
    def increase_score_r(self):
        self.r_score +=1
        self.update_scoreboard()    


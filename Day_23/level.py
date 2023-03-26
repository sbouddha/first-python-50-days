from turtle import Turtle

ALIGNMENT="center"
FONT=('Ariel', 10, 'normal')
DEFAULT_LEVEL=1

class Level(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-360,270)
        self.clear()
        self.write(f"Level: {DEFAULT_LEVEL}", False, align=ALIGNMENT, font=FONT)

    def up_game_level(self):
        global DEFAULT_LEVEL
        self.hideturtle()
        self.goto(-360,270)
        self.clear()
        DEFAULT_LEVEL +=1
        self.write(f"Level: {DEFAULT_LEVEL}", False, align=ALIGNMENT, font=FONT)

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("black")
        self.hideturtle()

    def game_won(self):
        self.goto(0,0)
        self.write("You Won", False, align=ALIGNMENT, font=FONT)   
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, align=ALIGNMENT, font=FONT)

    def score_clear(self):
        self.clear()
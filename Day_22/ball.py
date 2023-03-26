from turtle import Turtle

DEFAULT_MOVE_SPEED = 0.1


class Ball(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(position)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = DEFAULT_MOVE_SPEED

    # To move the ball up the corner from center
    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.penup()
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = DEFAULT_MOVE_SPEED
        self.bounce_x()

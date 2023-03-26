from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# Creating the screen
screen = Screen()
screen.bgcolor("black")
screen.title("The Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball=Ball((0, 0))
scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision wih Paddle
    if (l_paddle.distance(ball)<50 and ball.xcor()<-320) or (r_paddle.distance(ball)<50 and ball.xcor()>320):
        ball.bounce_x()
    #Detect collision wih upper and lower walls
    if ball.ycor()>290 or ball.ycor()<-290:
        ball.bounce_y()
    #Detect if the paddles are missed and screen crossed
    #R paddle missed
    if ball.xcor()>390:
        scoreboard.increase_score_l()
        ball.reset_position()
    #L paddle missed
    if ball.xcor()<-390:
        scoreboard.increase_score_r()
        ball.reset_position()


screen.exitonclick()

from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time


# Screen Setup
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snake = Snake()
food=Food()
score=Score()
screen.listen()

screen.onkey(snake.up, "Up")  
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right ,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect Collision with food, use distance function.
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        score.update_score()

    #Detect Collision with call.
    if snake.head.xcor()>390 or snake.head.xcor()<-390 or snake.head.ycor()>390 or snake.head.ycor()<-390:
        game_is_on=False
        score.game_over()

    #Detect collision with its own tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            game_is_on=False
            score.game_over()


screen.exitonclick()

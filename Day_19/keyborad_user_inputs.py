from turtle import Turtle, Screen

tim=Turtle()
screen=Screen()
tim.pensize(5)
tim.color("Green")

def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()
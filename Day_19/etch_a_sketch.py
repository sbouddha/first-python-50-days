from turtle import Turtle, Screen

tim=Turtle()
screen=Screen()
tim.pensize(2)
tim.color("Green")

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_counter_clockwise():
    tim.left(25)
    tim.heading()

def move_clockwise():
    tim.right(25)
    tim.heading()

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


#User entry listening
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
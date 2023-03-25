import random
import turtle

tim=turtle.Turtle()
turtle.colormode(255)
tim.speed('fastest')


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color_tuple=(r,g,b)
    return color_tuple


def draw_spirograph(size_of_gap):
    for i in range (int(360/size_of_gap)):    
        tim.pencolor(random_color())
        tim.circle(120)
        tim.setheading(tim.heading()+size_of_gap)


draw_spirograph(5)

screen = turtle.Screen()
screen.exitonclick()
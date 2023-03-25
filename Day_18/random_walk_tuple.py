import turtle
import random

tim=turtle.Turtle()
turtle.colormode(255)


tim.pensize(10)
tim.speed('fastest')
steps=30

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color_tuple=(r,g,b)
    return color_tuple


directions=[0,90,180,270 ]
total_moves=250

for moves in range (total_moves):
    tim.pencolor(random_color())
    tim.forward(steps)
    tim.setheading(random.choice(directions))


screen = turtle.Screen()
screen.exitonclick()


# my_tuple=(1,3,8)
# print(my_tuple[2])
# # prints 8

#Things in tuple cannot nbe changed
#They are immutable

#To change a tuple to list
#list(my_tuple)



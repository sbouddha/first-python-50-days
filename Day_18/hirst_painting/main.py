import turtle
import random

tim = turtle.Turtle()

turtle.colormode(255)
tim.pensize(10)
tim.speed('fastest')
tim.hideturtle()

color_list = [(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107),
              (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]


def random_color():
    color_tuple = random.choice(color_list)
    return color_tuple

def move_line_up_left():
    tim.penup()
    tim.left (90)
    tim.forward(50)
    tim.pendown()
    tim.left (90)

def move_line_up_right():
    tim.penup()
    tim.right (90)
    tim.forward(50)
    tim.pendown()
    tim.right (90)

def draw_cicles_in_line():    
    for i in range(10):
        tim.dot(20, random_color())
        tim.penup()
        tim.forward(50)
        tim.pendown()
        tim.dot(20, random_color())

for i in range (5):
    draw_cicles_in_line()
    move_line_up_left()
    draw_cicles_in_line()
    move_line_up_right()



screen = turtle.Screen()
screen.exitonclick()

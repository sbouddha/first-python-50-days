# import turtle
from turtle import Turtle, Screen
import random

# tim=turtle.Turtle()
tim= Turtle()
# tim.shape('turtle')
tim.color('green')

# Tim made the square
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)

#Easy way to make square
for i in range(4):
    tim.forward(100)
    tim.right(90)

#Draw Dashed line
tim.clear()
tim.home()

for i in range(15):
    tim.forward(10)
    tim.pendown()
    tim.forward(10)
    tim.penup()

tim.pendown()
tim.clear()

def draw_shape():      
    #Draw Triangle to Hexagon
    tim.home()
    tim.pendown()
    num_sides=3
    while num_sides<10:       
        for sides in range(num_sides):
            angle=360/num_sides
            tim.forward(100)
            tim.right(angle)
        num_sides +=1


#Get Color
def change_color():
    color = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "brown", "gray", "black"]
    color_picked=(random.choice(color))
    return color_picked

#draw_shapes
def draw_shape(num_sides):
    num_sides=num_sides
    angle=360/num_sides
    for move in range (num_sides):
        tim.forward(100)
        tim.right(angle)

tim.clear()
tim.home()

for shape_sides in range (3,11):
    random_color=change_color()
    tim.color(random_color)
    draw_shape(shape_sides)





# #Draw Triange
# sides=3
# angle=360/sides
# for i in range(sides):
#     tim.pendown()
#     tim.forward(100)
#     tim.right(angle)

# #Draw Square
# sides=4
# angle=360/sides
# for i in range(sides):
#     tim.pendown()
#     tim.forward(100)
#     tim.right(angle)

# #Draw Pentagon
# sides=5
# angle=360/sides
# for i in range(sides):
#     tim.pendown()
#     tim.forward(100)
#     tim.right(angle)

# #Draw Hexagon
# sides=6
# angle=360/sides
# for i in range(sides):
#     tim.pendown()
#     tim.forward(100)
#     tim.right(angle)

# #Draw Heptagon 
# sides=7
# angle=360/sides
# for i in range(sides):
#     tim.pendown()
#     tim.forward(100)
#     tim.right(angle)

# #Draw Octagon
# sides=8
# angle=360/sides
# for i in range(sides):
#     tim.pendown()
#     tim.forward(100)
#     tim.right(angle)

# #Draw Octagon
# sides=8
# angle=360/sides
# for i in range(sides):
#     tim.pendown()
#     tim.forward(100)
#     tim.right(angle)

# #Draw Nonagon
# sides=9
# angle=360/sides
# for i in range(sides):
#     tim.pendown()
#     tim.forward(100)
#     tim.right(angle)

# #Draw Decagon
# sides=10
# angle=360/sides
# for i in range(sides):
#     tim.pendown()
#     tim.forward(100)
#     tim.right(angle)



screen = Screen()
screen.exitonclick()
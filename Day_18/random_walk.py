from turtle import Turtle, Screen
import random
tim=Turtle()
tim.pensize(10)
tim.speed('fastest')
steps=30

color = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "brown", "gray", "black"]
directions=[0,90,180,270 ]
total_moves=250


for moves in range (total_moves):
    
    tim.color(random.choice(color))
    tim.forward(steps)
    tim.setheading(random.choice(directions))




screen = Screen()
screen.exitonclick()
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=800)

user_bet = screen.textinput(title="Make Your Bet",
                            prompt="Who do you think will win ? Enter Color: ")
color = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

is_race_on=False
x=-390
y=-140

all_turtles=[]

turtle_num=7
while turtle_num>0:  
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color[turtle_num-1])  
    new_turtle.up()
    new_turtle.goto(x=x,y=y)
    new_turtle.down()
    turtle_num -=1
    y +=50
    all_turtles.append(new_turtle)

#Now making turtles to forward at variable speeds

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>370:
            is_race_on=False
            winning_color=turtle.pencolor()
            print(winning_color)
            if winning_color==user_bet:
                turtle.write("You Won")
                print(f"You have won! The {winning_color} turtle is the winner")
            else:
                turtle.write("You Lose")
                print(f"You have lost! The {winning_color} turtle is the winner")
        random_distance=random.randint(0,10)
        turtle.up()
        turtle.forward(random_distance)


screen.exitonclick()

import turtle
import pandas as pd

image = r"C:\Without_Sync\Py\python-100-days\Day_26\blank_states_img.gif"
state_file = r"C:\Without_Sync\Py\python-100-days\Day_26\50_states.csv" 

screen = turtle.Screen()
screen_score = turtle.Screen()
screen.title("US States")
screen.addshape(image)
turtle.shape(image)

location_text_turtle = turtle.Turtle()
location_text_turtle.color("black")

correct_guess=0
incorrect_guess=0
total_states=50


#Read the states in a list
states_df = pd.read_csv(state_file)
state_list = states_df.state.to_list()
#Convert the whole list to lower case
state_list = [elem.lower() for elem in state_list ]

#Check if the answer is correct
def update_score():
    global correct_guess, user_answer
    correct_guess +=1
    user_answer = screen_score.textinput(f"{correct_guess}/{total_states} States Correct", "What's the next state name ?")

#mark in map
def mark_map():
    #get co-ordinates
    state_xy = states_df.loc[states_df["state"].str.lower() == user_answer.lower(), ["x","y"]]
    x_axis = int(state_xy["x"])
    y_axis = int(state_xy["y"])
    location_text_turtle.penup()
    location_text_turtle.hideturtle()
    location_text_turtle.goto(x_axis,y_axis)
    location_text_turtle.write(user_answer.capitalize(), align="center", font=("Arial", 10, "normal"))

user_answer = screen_score.textinput(f"{correct_guess}/{total_states} Enter States Name", "What's the state name ?")

is_game_on = True
while is_game_on:
    if user_answer.lower()=='off':
        is_game_on = False
    elif user_answer.lower() in state_list:
        mark_map()
        update_score()
    elif not (states_df["state"].str.lower() == user_answer.lower()).any():
        incorrect_guess +=1
        if incorrect_guess >=5:
            turtle.write("GAME OVER!!! Too many failed trials", align="center", font=("Arial", 10, "normal"))
            is_game_on = False
        else:
            user_answer = screen_score.textinput(f"{correct_guess}/{total_states} Enter States Name", "What's the state name ?")



turtle.mainloop()
# screen.exitonclick() --as it is click game
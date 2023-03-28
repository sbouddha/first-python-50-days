import pandas as pd

image = r"C:\Without_Sync\Py\python-100-days\Day_26\blank_states_img.gif"
state_file = r"C:\Without_Sync\Py\python-100-days\Day_26\50_states.csv" 

#Read the states in a list
states_df = pd.read_csv(state_file)
state_list = states_df.state.to_list()

# print(states_df["state"] == "Florida", ['x','y'])
# print(states_df['x'] where states_df["state"] == "Florida" )

# print(states_df.loc [states_df["state"]=="Florida" , ['x','y']])
state_xy= (states_df.loc [states_df["state"]=="Florida" , ['x','y']])
state_x=state_xy["x"]
state_y=state_xy["y"]
print(state_x)
print(state_y)
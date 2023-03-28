import pandas as pd

file_path = r"C:\Without_Sync\Py\python-100-days\Day_26"
squirrel_file = r"C:\Without_Sync\Py\python-100-days\Day_26\2018_CP_Squirrel_Data.csv"

data = pd.read_csv(squirrel_file)
data_df = pd.DataFrame(data)

#Get colors
#To get all top rows for getting the actual column names
# print(data.loc[0])

#Use unique function
distinct_fur_color=data_df["Primary Fur Color"].dropna().unique()
# print(distinct_fur_color)

#DataCount
color_count = data_df["Primary Fur Color"].value_counts()
color_count = color_count.reset_index()
color_count.columns = ["Fur_Color", "Count"]
print(color_count)
#create a new file
color_count.to_csv(file_path + "\squirrel_count.csv", index=False)


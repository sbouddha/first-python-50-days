import pandas

weather = "C:\Without_Sync\Py\python-100-days\Day_25\weather_data.csv"

data = pandas.read_csv(weather)
print(type(data))
#print(data["temp"])

#DataFrame function sample 
#To Dictionary
data_dict = data.to_dict()
print(data_dict)

#Average Temperature in the list : With Pandas
#Use mean function to calculate average
avg_temp = round(data["temp"].mean(), 2)
print(avg_temp)

#Series function sample
#To List
temp_list = data["temp"].to_list()
print(temp_list)
#Average Temperature in the list : Without Pandas
average_temp = round(sum(temp_list) / len(temp_list), 2)
print(average_temp)

#Return max min with pandas
print(data["temp"].max())
print(data["temp"].min())

#Another way:
print(data.condition)

#Fetch data in a row in more Pivot form
print(data.loc[0])
print(data.iloc[0])

#Much better way to fetch the row data
print(data[data["day"] == "Monday"])
print(data[data.day == "Monday"])

#print the row which have max(temp)
max_temp=data.temp.max()
print(data[data.temp == max_temp])


#Get temp in F
monday = data[data.day == "Monday"]
temp_c = int(monday.temp)
print(f"Temp in C : {temp_c}")

#Temp in F
temp_f = (temp_c * 1.8) + 32
print(f"Temp in F : {temp_f}")

#Create a DataFrame from scratch
new_data_dict={
    "students" :["Siddharth", "Pratima", "Elon"] ,
    "scores" : [70, 80, 90]
}
#using pandas.DataFrame() function on a dictionary
new_data_frame= pandas.DataFrame(new_data_dict)
print(new_data_frame)

#create a csv file from this dataframe
new_student_file = r"C:\Without_Sync\Py\python-100-days\Day_25\new_student_file.csv"
new_data_frame.to_csv(new_student_file)

#With path (this will be used most in office work)
new_student_path = r"C:\Without_Sync\Py\python-100-days\Day_25"
new_data_frame.to_csv(new_student_path + "/new_student_file2.csv", index=False)

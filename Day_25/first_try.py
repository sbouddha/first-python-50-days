weather="C:\Without_Sync\Py\python-100-days\Day_25\weather_data.csv"

with open(weather) as file:
    unformatted_data=file.readlines()
    data=[]
    for temp in unformatted_data:
        formatted_temp=temp.strip()
        data.append(formatted_temp)
    print(data)


import csv

weather="C:\Without_Sync\Py\python-100-days\Day_25\weather_data.csv"

with open(weather) as data_file:
    data=csv.reader(data_file)
    temperatures=[]
    for row in data:
        #selecting just temperatures
        temp=row[1]
        temperatures.append(temp)
    #Slice temperatures
    temperatures=temperatures[1:]
    temperatures = [int(values) for values in temperatures] #Very important to remember
    print(temperatures)
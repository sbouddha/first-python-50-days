#first open noth the files and save the data in a list 
with open("file1.txt") as file1:
    file1_list = list(file1)

with open("file2.txt") as file2:
    file2_list = list(file2)


#Create a list called result which have union values and change to int
result = [int(num) for num in file1_list if (num in file2_list) ]

# Write your code above 👆

print(result)



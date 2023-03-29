
#first open noth the files and save the data in a list 
with open("file1.txt") as file1:
    file1_list = list(file1)
    #fix the \n issue with the List Comprehension
    file1_list_fixed = [int(num.replace("\n","")) for num in file1_list]


with open("file2.txt") as file2:
    file2_list = list(file2)
    #fix the \n issue with the List Comprehension
    file2_list_fixed = [int(num.replace("\n","")) for num in file2_list]

print(file1_list_fixed)
print(file2_list_fixed)

#Create a list called result which have union values

result = [num for num in file1_list_fixed if (num in file2_list_fixed) ]


# Write your code above 👆

print(result)



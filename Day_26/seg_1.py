#List Comprehension
# new_list = [new_item for item in list]

numbers = [1,2,3]
number_plus_one = [num+1 for num in numbers]
print(number_plus_one)

#Important : List comprehension can also turn variable varues in List 
name = "Siddharth"
name_letter_list = [letter for letter in name]
print(name_letter_list)

# #Python Sequence:
# list
# range
# string
# tuple

new_range_list = [item*2 for item in range(1,5)]
print(new_range_list)


# # Conditional List Comprehension
# new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave" ,"Eleanor", "Freddie"]
selected_names = [name for name in names if len(name)<=4]
print(selected_names)

selected_names_2 = [name.upper() for name in names if len(name)>=5]
print(selected_names_2)





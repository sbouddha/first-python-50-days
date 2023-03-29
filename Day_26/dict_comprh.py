import random

#Dictionary Comprehension on list
name_list = ["Alex", "Beth", "Caroline", "Dave" ,"Eleanor", "Freddie"]

#TODO : create student_scores{} which have random score from 70 to 99

# new_dict = {new_key:new_value for item in list}
student_scores = {name:random.randint(1,99) for name in name_list}
print(student_scores)

#Dictionary Comprehension on Dictionary
# new_dict = {new_key:new_value for (key,value) in dict.items()}

#Conditional Dictionary Comprehension on Dictionary
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}


#TODO : create a dictionay called students_passed which have >50 marks

student_passed = {student:score for (student,score) in student_scores.items() if (score>35) }
print(student_passed)




sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

#TODO : First get words from the sentense
word_list = sentence.split()

# new_dict = {new_key:new_value for item in list}

result = {word:len(word) for word in word_list}
print(result)


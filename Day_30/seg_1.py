# Learning to handle error, catch exception

# try:
# except:
# else:
# finally:


# File not found exception
try:
    file = open("afile.txt")
    a_dict = {"key": "value"}
    print(a_dict["key"])
except FileNotFoundError as error_message_1:
    print(f"There was an error {error_message_1}, now handled\n")
    file = open("afile.txt", "w")
    file.write("Something")
except KeyError as error_message_2:
    print(f"The key {error_message_2} don't exists")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was Closed")


# Raising your own exceptions:
# raise TypeError("This is an error that I made up")

# BMI
height = float(input("Height : "))
weight = float(input("Weight : "))

# Raising our own exception, if the height is above 3 Meters
if height > 3:
    raise ValueError("This is unrealistic height")
try:
    bmi = weight / height ** 2
except ValueError as error_1:
    print(f"There is wrong entry {error_1}")
else:
    print("Calculating the BMI")
finally:
    print(bmi)

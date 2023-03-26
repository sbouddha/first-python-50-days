#Way 1: Open and Read the file, and print the contents of the file
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

#Way 2: Open and Read the file, and print the contents of the file
with open("my_file.txt") as file:
    contents=file.read()
    print(contents)

# Write in a file (override)
with open("my_file.txt", mode="w") as file:
    file.write("I am at first writing with Python in this file")

# Write in a file (append)
with open("my_file.txt", mode="a") as file:
    file.write("\nThis is line 2")

# Write in a file, if it don't exists (create mew)
with open("my_second_file.txt", mode="w") as file:
    file.write("This file was not existing earlier")

# Different Path : Write in a file, if it don't exists (create mew)
file_path="C:\Without_Sync\Archives\DifferentPathFile.txt"
#file_path = file_path.replace('\\', '/') --both works
with open(file_path) as file:
    contents=file.read()
    print(contents)
    
# Different Path : Write in a file, if it don't exists (create mew)
file_path="C:\Without_Sync\Archives\DifferentPathFile2.txt"
with open(file_path, mode="w") as file:
    file.write("This file was not existing earlier at this other path")


    
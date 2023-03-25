piano_keys=["a","b","c","d","e","f","g","h"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")


#Slicing in List
print(piano_keys[2:5])
# ['c', 'd', 'e']

print(piano_keys[2:])
# ['c', 'd', 'e', 'f', 'g', 'h']

print(piano_keys[:5])
# ['a', 'b', 'c', 'd', 'e']

print(piano_keys[2:7:2])
# ['c', 'e', 'g']

print(piano_keys[: :2])
# ['a', 'c', 'e', 'g']

print(piano_keys[: :-2])
# ['h', 'f', 'd', 'b']

print(piano_keys[: :-1])
# ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

#Slicing in Tuples 
print(piano_tuple[2:5])
# ('mi', 'fa', 'so')
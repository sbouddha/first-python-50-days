#Arguments with Default Values
def my_func(a=1, b=2, c=3):
    #Do this with a
    #Do this with b
    #Do this with c
    pass
#my_func(c=5, a=10, b=20)
#my_func(a=10) # here it will take just a=10 others as defaults
#my_func()
#Here if you dont pass the values of a,b,c it will take defaults

def add(n1, n2):
    print (f"Sum of Two Values {n1+n2}")
    return n1+n2

#Very important : Any number of input Arguments *args
def add_new(*args):
    sum=0
    for n in args:
        sum += n
    print(sum)
    return sum

add(1,2)
add_new(1,2,3,4)

def add_new_2(*args):
    total = sum(args)
    print(total)
    return total
add_new_2(1,2,3,4)
#Args are internally typed as Tuples
#Unlimited Positional Arguments

#**kwargs : Key Workded Arguments
#kwargs are internally typed as Dictionaries

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)
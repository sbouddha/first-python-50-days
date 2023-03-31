class Car():
    def __init__(self, **kw) -> None:
        self.make = kw.get("make")
        self.model = kw.get("model")
        #using the .get allowes that even if nothinhg is passed, the program will not fail, it will return None

my_car = Car(make="Tesla")

print(my_car.make)
print(my_car.model)
class Animal:
    def __init__(self) -> None:
        self.num_eye=2

    def breathe(self):
        print("Inhale, Exhale")


class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()

    def breathe(self):
        super().breathe()
        print("I am Breathing underwater")

    def swim(self):
        print("I can Swim")


nemo=Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eye)
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown",
          "gray", "teal", "turquoise", "gold", "silver", "violet", "magenta", "navy", "olive", "maroon"]
STARTING_MOVE_DISTANCE = 40
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self) -> None:
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-180, 180)
            new_car.goto(390, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

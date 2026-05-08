from turtle import *
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Cars:
    def __init__(self):
        super().__init__()
        self.vehicles = []
        self.speed = STARTING_MOVE_DISTANCE


    def make_vehicle(self):
        rand = random.randint(1, len(COLORS))

        if rand == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))

            rand_y = random.randint(-280, 280)
            new_car.goto(300, rand_y)
            self.vehicles.append(new_car)


    def drive_vehicle(self):
        for vehicle in self.vehicles:
            vehicle.backward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

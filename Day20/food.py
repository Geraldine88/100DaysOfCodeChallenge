"""
    This food class is going to know how to render itself as a small circle on the screen
    and when the head of the snake touches the food, food will move to a new random location
"""

import random
from turtle import Turtle

# Food class will inherit from turtle class so that we create a food object from a turtle

class Food(Turtle):
    def __init__(self):
        # creating food as turtle object
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=1.0, stretch_wid=1.0) #10x10 circle
        self.color("brown")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        rand_x = random.randint(-260, 260)
        rand_y = random.randint(-260, 260)
        self.goto(rand_x, rand_y)


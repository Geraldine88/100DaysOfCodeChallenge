import turtle
from turtle import *
import random

turtle.colormode(255)

nunu_the_wise = turtle.Turtle()
# Changing nunu's shape
nunu_the_wise.shape("turtle")



#changing Nunu's color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)
    return random_color



direction = [0, 90, 180, 270]

# Increasing thickness
nunu_the_wise.pensize(20)

# Increasing speed
nunu_the_wise.speed("fastest")

# GENERATE RANDOM WALK

for _ in range(200):
    nunu_the_wise.color(random_color())
    nunu_the_wise.forward(20)
    nunu_the_wise.setheading(random.choice(direction))


screen =Screen()
screen.exitonclick()
from turtle import *
import random

nunu_the_wise = Turtle()
# Changing nunu's shape
nunu_the_wise.shape("turtle")

#changing Nunu's color
nunu_the_wise.color("coral")

# Change color, thickness, speed
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "magenta", "gold", "silver"]

# 0: facing east --> right
# 90: facing north --> top
# 180: facing west --> left
# 270: facing south --> south
direction = [0, 90, 180, 270]

# Increasing thickness
nunu_the_wise.pensize(20)

# Increasing speed
nunu_the_wise.speed("fastest")

# GENERATE RANDOM WALK

for _ in range(200):
    nunu_the_wise.forward(60)
    nunu_the_wise.color(random.choice(colors))
    nunu_the_wise.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()
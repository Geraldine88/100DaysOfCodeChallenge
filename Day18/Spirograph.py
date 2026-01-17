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

    color = (r, g, b)
    return color


# Increasing speed
nunu_the_wise.speed("fastest")

nunu_the_wise.color(random_color())

# DRAWING SPIROGRAPH
def draw_spirograph(size_gap):


    for _ in range(int(360/size_gap)):
        nunu_the_wise.color(random_color())
        nunu_the_wise.circle(100)
        nunu_the_wise.setheading(nunu_the_wise.heading() +size_gap)

draw_spirograph(5)



screen = turtle.Screen()
screen.exitonclick()
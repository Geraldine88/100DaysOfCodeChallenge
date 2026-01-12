from turtle import *
import random

nunu_the_wise = Turtle()
# Changing nunu's shape
nunu_the_wise.shape("turtle")

#changing Nunu's color
nunu_the_wise.color("coral")

# Make nunu draw a square
for _ in range(4):
     nunu_the_wise.forward(100)
     nunu_the_wise.left(90)


screen = Screen()

screen.exitonclick()
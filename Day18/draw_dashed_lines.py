from turtle import *
import random

nunu_the_wise = Turtle()
# Changing nunu's shape
nunu_the_wise.shape("turtle")

#changing Nunu's color
nunu_the_wise.color("purple")


# Draw a dashed line
for i in range(10):
    nunu_the_wise.forward(10)
    nunu_the_wise.penup()
    nunu_the_wise.forward(10)
    nunu_the_wise.pendown()


screen = Screen()
screen.exitonclick()
from turtle import *
import random

nunu_the_wise = Turtle()
# Changing nunu's shape
nunu_the_wise.shape("turtle")

#changing Nunu's color
nunu_the_wise.color("coral")



# # Draw a circle
# nunu_the_wise.circle(100)



# # Draw a triangle
# """
#     For triangles, 360 / 3 = 120
# """
# for t in range(2):
#     nunu_the_wise.forward(100)
#     nunu_the_wise.right(120)
#
# # Draw a square:
# nunu_the_wise.color("brown")
# for sq in range(3):
#     nunu_the_wise.forward(100)
#     nunu_the_wise.right(90)
#
# # Draw a pentagon
# """
#     For a pentagon, 360 / 5 = 72
# """
# nunu_the_wise.color("black")
# for s in range(4):
#     nunu_the_wise.forward(100)
#     nunu_the_wise.right(72)
#
# # 6 sides
# nunu_the_wise.color("blue")
# for u in range(5):
#     nunu_the_wise.forward(150)
#     nunu_the_wise.right(60)
#
# # 7 sides
# nunu_the_wise.color("red")
# for q in range(6):
#     nunu_the_wise.forward(200)
#     nunu_the_wise.right(53)
#
# # 8 sides
# nunu_the_wise.color("green")
# for r in range(7):
#     nunu_the_wise.forward(250)
#     nunu_the_wise.right(45)


"""
        SOLUTION FOR DRAWING DIFFERENT SHAPES
"""
# Drawing Different shapes

# List of different colors
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "magenta", "gold", "silver"]


def draw_shape(num_sides):
    angle = 360 / num_sides

    for s in range(num_sides):
        nunu_the_wise.forward(100)
        nunu_the_wise.right(angle)


for shape_side_n in range(3, 13):
    nunu_the_wise.color(random.choice(colors))
    draw_shape(shape_side_n)



screen = Screen()

screen.exitonclick()
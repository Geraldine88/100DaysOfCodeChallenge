# LET'S PICASSO PROJECT USES COLORGRAM AND OTHER LIBREARIES TO INVENT PAINTINGS

import colorgram
import random
from turtle import Turtle, Screen

colors = colorgram.extract("image.jpg", 100)
print(colors)


# turtle.colormode(255)
# Object
picca = Turtle()

rgb_c = []

for c in colors:
    r = c.rgb.r
    g = c.rgb.g
    b = c.rgb.b
    rgb_c.append((r,g,b))

screen = Screen()
screen.colormode(255)

def random_color():
    return random.choice(rgb_c)



# Initializing the speed
picca.speed("fastest")

picca.penup()
picca.hideturtle()
picca.setheading(225)
picca.forward(300)
picca.setheading(0)

dots = 200

# Selecting random colors for our master art
for d in range(1, dots+1):

    picca.dot(30, random_color())
    picca.forward(50)

    # for i in range(10):
    #     picca.dot(20, random_color())
    #     picca.penup()
    #     picca.left(90)
    #     picca.forward(50)
    #     picca.pendown()
    if d % 10 == 0:
        picca.setheading(90)
        picca.forward(50)
        picca.setheading(180)
        picca.forward(50*10)
        picca.setheading(0)







screen.exitonclick()


"""
    THIS FILE IS TO PRACTICE MOVING THE TURTLE AROUND SO AS TO INTERGRATE IN THE SNAKE GAME

"""

from turtle import Turtle, Screen


timmy = Turtle()
timmy.color("pink")
timmy.shape("turtle")


screen = Screen()


# TODO: MOVE TIMMY IN THE 4 DIFFERENT DIRECTIONS FOR KEYBOARD STROKES

"""
    UP -> NORTH : 90 DEGREES
    DOWN -> SOUTH : 270 DEGREES
    LEFT -> WEST : 180 DEGREES
    RIGHT -> EAST : 0 DEGREES
"""

def up():
    timmy.setheading(90)
    timmy.penup()
    timmy.forward(20)
    # timmy.left(90)

def down():
    timmy.setheading(270)
    timmy.penup()
    timmy.forward(20)


def left():
    timmy.setheading(180)
    timmy.penup()
    timmy.forward(20)

def right():
    timmy.setheading(0)
    timmy.penup()
    timmy.forward(20)



screen.listen()

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")


screen.bgcolor("blue")



screen.exitonclick()

# ETCH-A-SKETCH PROJECT

from turtle import Screen, Turtle

g = Turtle()
screen = Screen()

g.shape("arrow")
g.color("purple") # Because I'm just a girl, duhhhh


def move_forward():
    g.forward(10)

def move_backward():
    g.backward(10)

def left():

    g.left(10)
    g.setheading(g.heading()+10)

def right():
    g.right(10)
    g.setheading(g.heading()-10)

def clear():
    g.clear()
    g.home()


screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "a", fun = left)
screen.onkey(key = "d", fun = right)
screen.onkey(key = "c", fun = clear)



screen.listen()


screen.exitonclick()
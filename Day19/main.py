from turtle import Turtle, Screen

nunu = Turtle()
screen = Screen()


# Bind a functions that will be triggered when a key is struck
def move_forward():
    nunu.forward(10)
    # To start listening to events, we use .listen()
screen.listen()
# Move forward when the space bar is pressed
screen.onkey(key = "space", fun = move_forward)
screen.exitonclick()
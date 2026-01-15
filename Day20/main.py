from turtle import Turtle, Screen
from aga_snake import Snake
import time

# Create a new screen
screen = Screen()

# Creating snake object for class
snake = Snake()

# Getting our screen to listen to keyboard keystrokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Set up screen to 600 x 600
screen.setup(width=600, height=600)

# Change screen background color
screen.bgcolor("green")

# Set title of window
screen.title("Aga Snake Game")

# Step2 => turn off tracer animation
screen.tracer(0)

# STEP 1: CREATE SNAKE BODY
# TODO: Create 3 turtles shaped like a square, white in color and
#  position them turtle 1 is at (0,0), tutle 2 is 20px to the left and
#  the third turtle is 20px to the left of the second. Each turtle is 20x20





game_on = True
# While game is on, move each segment
while game_on:
    # i wanna update te screen only when all the segments have moved forward as an entire piece
    screen.update()
    time.sleep(0.08)

    snake.game_on()






screen.exitonclick()


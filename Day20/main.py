from turtle import Turtle, Screen
from aga_snake import Snake
import time
from food import Food
from score_board import Scoreboard

# Create a new screen
screen = Screen()

# Set up screen to 600 x 600
screen.setup(width=600, height=600)

# Change screen background color
screen.bgcolor("green")

# Set title of window
screen.title("Aga Snake Game")

# Ask user what would be the level of their difficulty
difficulty = screen.textinput("Difficulty", "Choose difficulty: easy, medium, hard : ")

if difficulty == "easy":
    speed = 0.2
elif difficulty == "medium":
    speed = 0.1
elif difficulty == "hard":
    speed = 0.05
else:
    speed = 0.15

# Creating snake object for class
snake = Snake()

# Initializing a food object
food = Food()

# Initializing scoreboard
scoreboard = Scoreboard()

# Getting our screen to listen to keyboard keystrokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

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
    time.sleep(speed)

    snake.game_on()

    # detect collision with food using Turtle() distance method
    # if snake's head is withing 15px from food. Food is 10x10
    if snake.head.distance(food) < 15:
        #Food should go to new location
        food.refresh()
        snake.add_body()
        scoreboard.increase_score()

    # detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    # detect tail collision
    # if head collides with any other part of the snake's body, game over
    for seg in snake.snake_parts[1:]:
        if snake.head.distance(seg) < 10:
            game_on = False
            scoreboard.game_over()






screen.exitonclick()


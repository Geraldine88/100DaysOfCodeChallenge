from turtle import *

screen = Screen()

# A python constant is in all capital letters
MOVE_DIST = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.snake_parts = []
        self.appearance_sk()
        self.head = self.snake_parts[0]

    # STEP 1: CREATE SNAKE BODY
    # TODO: Create 3 turtles shaped like a square, white in color and
    #  position them turtle 1 is at (0,0), tutle 2 is 20px to the left and
    #  the third turtle is 20px to the left of the second. Each turtle is 20x20

    def appearance_sk(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)



    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.color("gold")
        snake.penup()
        # snake.shapesize(stretch_wid=1, stretch_len=1)
        # snake.setposition(-20 * i, 0)
        snake.goto(position)
        self.snake_parts.append(snake)

        # STEP 2: MOVING THE SNAKE, GETTING SNAKE TO CHANGE DIRECTIONS
        # TODO: Move the snake, changing its direction
        #self.snake_parts.append(snake)


    #Class will increase the snake length my 1 everytime it eats food
    def add_body(self):
        self.add_segment(self.snake_parts[-1].position())




    def game_on(self):
        # To get the snake to change directions, we target from the last body part to the first
        # So we will start from 2, stop at 0 and step -1once
        # for part_num in range(start = 2, stop = 0, step = -1):
        # for part_num in range(start=len(snake_parts) - 1, stop=0, step=-1):

        for part_num in range(len(self.snake_parts)-1, 0, -1):
            # gettng a hold of the second to last part
            new_x = self.snake_parts[part_num - 1].xcor()
            new_y = self.snake_parts[part_num - 1].ycor()

            self.snake_parts[part_num].goto(new_x, new_y)

        self.snake_parts[0].forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        # timmy.left(90)

    def down(self):
        if self.head.heading() != UP:
        # self.snake_parts[0].setheading(270)
        # self.snake_parts[0].penup()
        # self.snake_parts[0].forward(20)

            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
        # self.snake_parts[0].setheading(180)
        # self.snake_parts[0].penup()
        # self.snake_parts[0].forward(20)

            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
        # self.snake_parts[0].setheading(0)
        # self.snake_parts[0].penup()
        # self.snake_parts[0].forward(20)

            self.head.setheading(RIGHT)








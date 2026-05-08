STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import *

class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shape("turtle")
        self.color("white")
        self.at_start()
        self.setheading(90)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def at_start(self):
        self.goto(STARTING_POSITION)




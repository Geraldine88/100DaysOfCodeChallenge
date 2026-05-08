from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)





"""
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_len=1, stretch_wid=5)
paddle.penup()
paddle.goto(350, 0)

#To control animation use screen.tracer(0)
# TODO: 3 - Create Paddle 2
paddle_2 = Turtle()
paddle_2.shape("square")
paddle_2.color("gold")

paddle_2.shapesize(stretch_len=1, stretch_wid=5)
paddle_2.penup()
paddle_2.goto(-350, 0)
"""
from turtle import *
FONT = ("Courier", 24, "normal")


class Points(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250,250)
        self.update_points()

    def update_points(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_points()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)
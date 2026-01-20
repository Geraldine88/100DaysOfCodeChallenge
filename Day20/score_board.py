from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        with open("high_scores.txt") as highscore_file:
            self.highest_score = int(highscore_file.read())


        self.color("white")
        self.penup()
        self.goto(0, 250)

        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"SCORE: {self.score}, HIGHEST SCORE: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            #read from file
            with open("high_scores.txt", "w") as highscore_file:
                highscore_file.write(f"{self.highest_score}")
        #reset score
        self.score = 0
        #update scoreboard
        self.update()

    def show_lives_lost(self, lives_remaining):
        self.goto(0, 0)
        self.write(f"OUCH! Lives Left: {lives_remaining}", align=ALIGNMENT, font=FONT)
        self.goto(0, 250)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()
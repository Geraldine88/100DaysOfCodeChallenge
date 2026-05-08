from turtle import *
import random

# numi = Turtle(shape = "turtle")
screen = Screen()
# numi.shape("turtle")



# Colors for other turtle instances
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# Define screensize with setup()
#screen.setup(width = 500, height = 300)

# Setting screen size automatically
screen_height = screen.window_height()
screen_width = screen.window_width()

space = screen_height // (len(colors) + 1)

start_x = -screen_width // 2 + 20
finish_line = screen_width // 2 - 20

# Bring up the popup
player_color = screen.textinput(title = "Place your bet", prompt = "Which turtle will you play?"
                                                    " Enter a color :")

#y_location = [-100, -50, 0, 50, 100, 150]

racers = []
start = False
for i, c in enumerate(colors):
    racer = Turtle(shape ="turtle")
    # numi.color(random.choice(colors))
    racer.color(c)
    racer.penup()

    y = screen_height // 2 - space * (i + 1)
    racer.goto(x= start_x, y=y)
    racers.append(racer)

# Randomize speed
if player_color:
    start = True

while start:
    # Checking to see if turtle's x_cor  >  +250
    for r in racers:
        finish_line = screen.window_width() // 2 - 20

        if r.xcor() > finish_line:
            # stop while loop
            start = False
            winner = r.pencolor()

            if winner == player_color:
                screen.textinput(
                    title = "Race Result 🏁",
                    prompt=f"You WIN! 🎉\nThe {winner} turtle won the race!"
                )
            screen.textinput(
                title="Race Result 🏁",
                prompt=f"You LOSE 😢\nThe {winner} turtle won the race!"
            )


        random_dist = random.randint(0,10)
        r.forward(random_dist)




# Take turtle to left of screen
# numi.penup()
"""
    Since we have a screen width of 500, 
        the center of (0, 0)
        the left side to the center is 250, right side is 250
    Since we have a height of 300, 
        the center of (0, 0)
        the top to the center is 150, bottom side is 150
"""
# numi.goto(x = -250, y = -100)


screen.exitonclick()
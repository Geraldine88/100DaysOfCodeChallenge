"""
            ****************** =>> MAIN SCREEN <<= ********************

"""

from turtle import *
from paddlers import Paddle
from ball_pong import Ball
import time
from track_score import ScoreBoard

# TODO : 1 - Create the Screen
screen = Screen()

MOVE_DIST = 20

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)


# TODO: 2 - Create and move the paddle
l_paddle = Paddle((-350, 0))
l_paddle.color("gold")

#To control animation use screen.tracer(0)
# TODO: 3 - Create Paddle 2
r_paddle = Paddle((350, 0))
r_paddle.color("red")

# TODO: 4 - Create the Ping-Pong Ball and make it move
ball = Ball()

scoreboard = ScoreBoard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

#Player 2
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

start_game = True
while start_game:
    time.sleep(ball.pace)
    screen.update()
    ball.move()

    # TODO: 5 - Detect collision with top and bottom wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # TODO : 6 - Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 315) or (ball.distance(l_paddle) < 50 and ball.xcor() < -315):
        ball.bounce_x()

    # TODO: 7 - Detect what occurs if paddle misses ball
    if ball.xcor() > 380:
        ball.reset_position()

        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()
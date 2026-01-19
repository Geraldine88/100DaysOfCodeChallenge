from turtle import *
from points import  Points
import time
from cars import *

from turtle_cross import *

screen = Screen()
screen.bgcolor("gray")
screen.setup(width=600, height=600)
screen.tracer(0)

#############################################
            # CREATING OBJECTS #            #
turtle_player = Player(STARTING_POSITION)   #
                                            #
vehicles = Cars()                           #
                                            #
score = Points()                            #
#############################################

screen.listen()
screen.onkey(turtle_player.go_up, "Up")
screen.onkey(turtle_player.go_down, "Down")

cross_now = True
while cross_now:
    time.sleep(0.1)
    screen.update()

    # On every refresh, a new car is created
    vehicles.make_vehicle()
    vehicles.drive_vehicle()

    # todo: Detect collision with car
    for v in vehicles.vehicles:
        """
        cars are 20px high and 40px wide. If player < 20px from car's center, player has collided with car
        """
        ALIGNMENT = "center"
        FONT = ("Courier", 24, "bold")
        if v.distance(turtle_player) <= 20:
            cross_now = False
            # v.write("GAME OVER", align=ALIGNMENT, font=FONT)
            score.game_over()


    # todo: check is turtle crossed the road successfully
    if turtle_player.at_finish():
        turtle_player.at_start()
        vehicles.increase_speed()
        score.increase_level()




screen.exitonclick()
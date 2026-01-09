# import turtle
#
# nini = turtle.Turtle()
#
# print(nini)

from turtle import Turtle, Screen

nini = Turtle()
print(nini)

# Screen represents the window in which the turtle will show up
nini_screen = Screen()
print(f"Nini\'s screen height: {nini_screen.canvheight} and width: {nini_screen.canvwidth}")


#Change nini's shape
#nini.shape("turtle")
print(f"Change Nini\'s to a turtle: {nini.shape("turtle")}")


#Changing nini's color
print(f"Change Nini\'s color to something pretty: {nini.fillcolor("darkOrchid2")}")

#Moving Nini by 100 paces
print(f"Moving Nini by 100 paces: {nini.forward(100)}")
print(f"Moving Nini to the left by 90 degree: {nini.left(90)}")
print(f"Moving Nini to the left by 180 degree: {nini.left(180)}")
print(f"Making Nini draw a circle with a radius of 100: {nini.circle(100)}")
print(f"Hiding Nini after making her draw the circile: {nini.hideturtle()}")


nini_screen.exitonclick()
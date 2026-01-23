import turtle
from turtle import Screen
import pandas as pd

screen = Screen()
screen.title("Guess the US State")

image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x, y):
#         print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

df = pd.read_csv("50_states.csv")

x_y_dict = {
    'x_coordinate' : df['x'].tolist(),
    'y_coordinate' : df['y'].tolist()
}

state_name = df['state'].tolist()



"""
    1 - Convert the guess to Title case
    2 - Check if guess is among the 50 states
    3 - Write correct guesses on the map
    4 - Use a loop to allow user to keep guessing
    5 - Record the correct guesses in a list
    6 - Keep track of the score
"""

guesses = []

while len(guesses) < 50:
    user_answer = (screen.textinput(title=f"{len(guesses)}/50 States Correct", prompt="Enter a state")).title()
    # if df[df.state == user_answer]:
    #     print(user_answer)

    if user_answer == "Exit":

        missing_states = []
        for s in state_name:
            if s not in user_answer:
                missing_states.append(s)

        missing_states_df = pd.DataFrame(missing_states)
        missing_states_df.to_csv("missing_states_to_learn.csv", index=False)
        break

    if user_answer in state_name:
        guesses.append(user_answer)
        turtle_state = turtle.Turtle()
        turtle_state.hideturtle()
        turtle_state.penup()

        st_df = df[df.state == user_answer]

        turtle_state.goto(st_df.x.item(), st_df.y.item())

        turtle_state.write(user_answer, font=("Arial", 10, "bold"))

#print(user_answer)
# un_guessed = []
# for i in un_guessed:
#     if i not in guesses:
#         un_guessed.append(i)
# un_guessed_df = pd.DataFrame(un_guessed)
# un_guessed_df.to_csv("un_guessed.csv", index=False)
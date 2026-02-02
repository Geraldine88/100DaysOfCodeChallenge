from textwrap import fill

BACKGROUND_COLOR = "#B1DDC6"
###################################     IMPORTS      ##################################
from tkinter import *
from tkinter import messagebox

#Import random to select random words
import random

# Import csv to read the csv file
import pandas as pd

import time
##################################       Data Manipulation        ###################################
# df = pd.read_csv("data/french_words.csv")
# so now that we have a to_learn.csv, we will draw data from there instead
french_df= {}
try:
    df = pd.read_csv("data/to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
    french_df = df.to_dict(orient="records")
else:
    french_df = pd.DataFrame(df)
    french_df = french_df.to_dict(orient="records")

# Take french words and translations in csv
rand_french = {}
def random_french():
    global rand_french, time_swap

    #everytime we click on the button to get to a new word, invalidate timer
    window.after_cancel(time_swap)

    rand_french = random.choice(french_df)
    #print(rand_french["French"])
    canvas.itemconfig(crd_title, text = "French", fill="black")
    canvas.itemconfig(crd_word, text = rand_french["French"], fill="black")

    canvas.itemconfig(view_img, image = front_card_img)
    time_swap = window.after(3000, func=swap_card)

# swap
def swap_card():

    canvas.itemconfig(crd_title, text = "English", fill="white")
    #getting hold of the value under english column from random french word
    canvas.itemconfig(crd_word, text = rand_french["English"], fill="white")
    canvas.itemconfig(view_img, image = back_card_img)

# Creating a csv for words to be learned and keeping out those already learned
#remove current card from list of french_random words to learn
def is_learned():
    #global rand_french, time_swap
    french_df.remove(rand_french)

    #Creating a new dataframe from random_french lis
    data = pd.DataFrame(french_df)
    data.to_csv("data/to_learn.csv", index=False)

    random_french()

########################################         UI        ###########################################
window = Tk()
window.title("Study Flash Card")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

#swap
time_swap = window.after(3000, func=swap_card)

# TODO: 2. Use the images in the image folder, to create the following user interface. The ❌ and ✅ are buttons. You can add images to buttons like this:
#
#     my_image = PhotoImage(file="path/to/image_file.png")
#     button = Button(image=my_image, highlightthickness=0)

# Creating canvas
canvas = Canvas(width=800, height=526)

# FRONT AND BACK IMAGES
front_card_img = PhotoImage(file = "images/card_front.png")
back_card_img = PhotoImage(file = "images/card_back.png")


view_img = canvas.create_image(400,263, image=front_card_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
crd_title = canvas.create_text(400, 150,  text="Title", font=("Times New Roman", 40, "italic"))
crd_word = canvas.create_text(400, 263, text = "word", font=("Times New Roman", 20, "bold"))

# WORD DISPLAY
french_word = Label(text="French")


# BUTTONS
right_img = PhotoImage(file = "images/right.png")
wrong_img = PhotoImage(file = "images/wrong.png")

right_btn = Button(image=right_img, highlightthickness=0, command=random_french)
right_btn.grid(row=1, column=1)

wrong_btn = Button(image=wrong_img, highlightthickness=0, command=is_learned)
wrong_btn.grid(row=1, column=0)



########## calling the function so that on first interaction, we see the contents of random_french
random_french()


window.mainloop()
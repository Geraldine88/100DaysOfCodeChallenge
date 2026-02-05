from tkinter import *
import requests


def get_quote():
    # TODO: 1 - Make a get() request to the Kanye Rest API
    response = requests.get("https://api.kanye.rest/")

    #TODO: 2 - Raise an exception if the request returned an unsuccessful status
    response.raise_for_status()

    #TODO 3 - Parse the JSON to obtain the quote text
    quote = response.json()

    #TODO: 4 - Display the quote in canvas' quote_text widget
    display_quote_text = quote["quote"]

    canvas.itemconfig(quote_text, text=display_quote_text)
    #Write your code here.



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye's Quote goes here", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()
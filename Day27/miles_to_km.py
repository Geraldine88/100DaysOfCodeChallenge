# CREATE A TKINTER APP THAT TAKES THE FLOAT INPUT IN MILES AND OUTPUTS THE KILOMETER CONVERSION
from tkinter import *

# TODO: CREATE A WINDOW CALLED "MILE TO KM CONVERTER" OR WHATEVER
window = Tk()
window.title("CARTHAN MILES TO KM")
# window.minsize(400, 300)
window.config(padx=60, pady=60, bg="#2C3E50")

# TODO: ONCLICK FUNCTION TO COMPUTE CONVERSION
def onClick():
    # return input entry as float
    entry = float(input.get())

    # computing miles to km by multiplying by 1.609
    miles_to_km = entry * 1.609

    #outputting the value in label (val_txt)
    val_txt.config(text=miles_to_km)
    #al_txt.config(text=f"{miles_to_km}")

# I wanna put the widgets into a frame to make it look beautiful
frame = Frame(window, bg="white", relief=RAISED, borderwidth=3)
frame.grid()


# TODO: CREATE INPUT BOX TO GET THE VALUE IN MILES AND TEXT OUTSIDE THE BOX TO THE RIGHT SAYING MILES.
input = Entry(width=20)
input.grid(column=1, row=0)

# TODO: CREATE AN OUTPUT THAT WILL SHOW THE VALUE IN KM AFTER THE CALCULATE BUTTON IS CLICKED

# Miles text is a label, KM is a label, 'is equal to' is a label, converted value is a label

# MILES
miles = Label(text=" Miles ", font=("Arial", 10))
miles.grid(column=2, row=0)
miles.config(padx=10, pady=10, bg="#2C3E50", fg="white")

# VALUE CONVERTED IS A LABEL
val_txt = Label( font=("Arial", 10))
val_txt.grid(column=1, row=1)
val_txt.config(padx=10, pady=3)

# IS EQUAL TO TEXT IS A LABEL
equal_txt = Label(text=" Is Equal to ", font=("Arial", 10))
equal_txt.grid(column=0, row=1)
equal_txt.config(padx=10, pady=10)

# KM TEXT IS A LABEL
km_txt = Label(text=" KM ", font=("Arial", 10))
km_txt.grid(column=2, row=1)
km_txt.config(padx=5, pady=5, bg="white")

# TODO: CREATE THE CALCULATE BUTTON
calc_btn = Button(text=" Calculate ", command=onClick)
calc_btn.grid(column=1, row=2)
calc_btn.config(padx=5, pady=5, bg="#3498DB", fg="white", activebackground="#2980B9")


# TODO: KEEP WINDOW OPEN
window.mainloop()
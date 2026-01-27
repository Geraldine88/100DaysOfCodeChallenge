from tkinter import *
import turtle

# Creating a new window/screen
window = Tk()

# change title of window
window.title("My first window")

# Window size
window.minsize(600, 400)
window.config(padx=20, pady=20)


# LAYOUT

# Where there's grid, you can't pack
# to get paddings, directly add on windows

# Button Click function
def click():
    print("I got clicked")
    my_lable.config(text=input.get())

# Label widget
my_lable = Label(text="My first window", font=("Arial", 25, "bold"))
#placing components into a screen with pack center
# my_lable.pack(expand=True)
# my_lable.pack(side="left")
# Placing the text in the top-left cornet
#my_lable.place(x = 0, y = 0)

my_lable['text'] = 'Nice to meet you!'
my_lable.config(text="You're still here!")
my_lable.grid(column=0, row=0)
my_lable.config(padx=10, pady=10)


# Button widget
button = Button(text="Click me", command=click)
button.grid(column=1, row=1)
button.config(padx=10, pady=10)
# button.pack()

#New button
new_btn = Button(text="New Button", command=click)
new_btn.grid(column=2, row=0)
new_btn.config(padx=10, pady=10)


# Entry widget
# Entry is basically an input
input = Entry(width=40)
print(input.get())
# input.pack()
input.grid(column=3, row=2)




# Keeps window open
window.mainloop()
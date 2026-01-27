from tkinter import *

# Creating a new window/screen
window = Tk()
# change title of window
window.title("My first window")
# Window size
window.minsize(400, 300)



# Lable class
my_lable = Label(text="My first window", font=("Arial", 25, "bold"))
#placing components into a screen with pack center
# my_lable.pack(expand=True)
# my_lable.pack(side="left")
my_lable.pack()

my_lable['text'] = 'Nice to meet you!'
my_lable.config(text="You're still here!")

# Button Click function
def click():
    print("I got clicked")
    my_lable.config(text=entry.get())



# Button properties
button = Button(text="Click me", command=click)
button.pack()
print('\n')


# Entry is basically an input
entry = Entry(width=40)
#Add some text to begin with
entry.insert(END, string="ABC DO-RE-MI")
print(entry.get())
# input.get()
entry.pack()

#Text
txt = Text(height=5 ,width=40)
#Putting cursor in textbox
txt.focus()
# Adding some text to begin with
txt.insert(END, "Do, a deer, a female deer")
# Gets current value in textbox at line 1, character 0
print(txt.get("1.0", END))
txt.pack()

# Spinbox
print("\n Spinboxes")
def Spinbox_used():
    #gets current value in spinbox
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=10, command=Spinbox_used)
spinbox.pack()


# Scale widget
print('\n Scale is used to select the scale of values you want. ')
def Scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=Scale_used)
scale.pack()

print('\n Check buttons are used to verify the state.')
# Check button
def CheckButton_used():
    # prints 1 if 'ON' button is checked. otherwise 0
    print(check_state.get())

check_state = IntVar()
checkbtn = Checkbutton(text="IS ON?", variable=check_state, command=CheckButton_used())
check_state.get()
checkbtn.pack()

print('\n Radio buttons are used to pick between different options. ')


# Radio Button widget
def Radio_used():
    print(radio_state.get())

radio_state = IntVar()
rad_btn1 = Radiobutton(text='Option 1', value=1, variable=radio_state, command=Radio_used)
rad_btn2 = Radiobutton(text='Option 2', value=2, variable=radio_state, command=Radio_used)
rad_btn1.pack()
rad_btn2.pack()


# Listbox widget
print('\n List boxes are just options created from a python list so we can select items in'
      'the box.')
def Listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=5)
fruits = ["Sour Sop", "Pineapples", "Blue berries", "Lemon", "Lime", "Guava"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListBoxSelection>>", Listbox_used)
listbox.pack()


# Keeps window open
window.mainloop()
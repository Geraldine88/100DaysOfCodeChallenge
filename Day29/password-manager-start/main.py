from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from random import randint, choice, shuffle
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# From day 5: password generator app

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
               'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
               'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = 8
    nr_symbols = 4
    nr_numbers = 4

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    pwd_entry.delete(0, END)
    pwd_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# Take inputs from entries, when the 'Add' button is clicked,save them in a file called data.txt

# TODO: 1 - Create a function called save(), mine is save_entries()
def save_entries():
    # creating data.txt
    #f = open("data.txt", "x")

    # if user did not type anything, generate message box
    if len(web_entry.get()) == 0 or len(pwd_entry.get()) == 0:
        messagebox.showerror("Error", "Please enter make sure no field is empty")
    else:
        is_good = messagebox.askokcancel(title=web_entry.get(), message=f"These are the details entered:"
                                                              f"\n Email: {email_entry.get()}\n"
                                                              f"\n Password: {pwd_entry.get()}\n"
                                                              f"Is this okay to save?")
        if is_good:

            click_count = 0
            # TODO: 2 - Write to the data inside the entries to a data.txt when the 'Add' button is clicked
            with open("data.txt", "a") as f:
                # TODO: 3 - Each website, email and password combo should be on a new line inside the file
                #everytime the 'Add' button is clicked, we write to a new line
                for i in range(click_count + 1):
                    f.write(f"{web_entry.get()} || {email_entry.get()} || {pwd_entry.get()}\n")

                # TODO: 4 - All fields need to be cleared after the 'Add' button is clicked
                web_entry.delete(0, END)
                pwd_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Manage Password with LB")
window.configure(padx=20, pady=20)

# # Load the image using PIL
# # Make sure to replace "background.jpg" with your image file path
bg_img = Image.open("personal_brand.png")
bg_img = bg_img.resize((900, 700), Image.LANCZOS)
photo = ImageTk.PhotoImage(bg_img)

# Create a Label to hold the image
background_label = Label(window, image=photo)
# # Use place() to cover the entire window
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# """
# Tkinter stacks widgets like layers:
#
# lower() → push widget to background
#
# lift() → bring widget forward
# """
background_label.lower()

################################# WHITE CONTENT FRAME #################################

content_frame = Frame(window, bg="white")
content_frame.grid(column=0, row=0, columnspan=3, rowspan=6, padx=10, pady=10)

################################# CANVAS #################################

canvas = Canvas(content_frame, width=200, height=200)
canvas.config(bg="white", highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

################################# WEBSITE #################################
website_label = Label(content_frame, text="Website", width=35, bg="white")
website_label.config(padx=1, pady=2)
website_label.grid(column=0, row=1)
# website entry
web_entry = Entry(content_frame, width=55, bg="white")
# entry.focus focuses the cursor into the particular entry. In this case website entry
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2)

################################# EMAIL/USERNAME ##########################
email_label = Label(content_frame, text="Email/Username", width=35, bg="white")
email_label.config(padx=1, pady=2)
email_label.grid(column=0, row=2)
# email/username entry
email_entry = Entry(content_frame, width=55)
email_entry.grid(column=1, row=2, columnspan=2)
# prepopulating email/user entry with most common email using insert
# 0: START-> WHERE WE WANNA FIT THE EMAIL, END WILL PLACE IT AT THE END
email_entry.insert(0, "gmail@gmail.com")

################################# PASSWORD #################################
pwd_label = Label(content_frame, text="Password", bg="white")
pwd_label.config(padx=1, pady=2)
pwd_label.grid(column=0, row=3)
# password entry
pwd_entry = Entry(content_frame, width=36)
pwd_entry.grid(column=1, row=3)

################################# BUTTONS ##################################
# 1 - GENERATE PASSWORD
generate_pwd_btn = Button(content_frame, text="Generate Password", bg="white", command=generate_password)
generate_pwd_btn.config(padx=1, pady=5)
generate_pwd_btn.grid(column=2, row=3)

# 2 - ADD BUTTON
add_btn = Button(content_frame, text="Add", bg="white", width=47, command=save_entries)
add_btn.config(padx=1, pady=5)
add_btn.grid(column=1, row=4, columnspan=2)

# # Keep a reference to the image object to prevent it from being garbage collected
background_label.image = photo

window.mainloop()

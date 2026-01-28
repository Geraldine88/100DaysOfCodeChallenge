from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():

    window.after_cancel(timer)

    canvas.itemconfig(timerTxt, text="00:00", fill="white")

    title.config(text="Timer", bg=YELLOW, fg=GREEN)

    competed_count.config(text="")

    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps

    # Increase timer reps by 1
    reps += 1

    #countDown(5 * 60)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's in the 1st, 3rd, 5th, 7th rep
    #countDown(work_sec)
    if reps % 8 == 0:
        countDown(long_break_sec)
        title.config(text="Break", bg=YELLOW, fg=RED)

    elif reps % 2 == 0:
        countDown(short_break_sec)
        title.config(text="Break", bg=YELLOW, fg=PINK)

    else:
        countDown(work_sec)
        title.config(text="Work", bg=YELLOW, fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countDown(count):

    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)


    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timerTxt, text = f"{count_min}:{count_sec}", fill="white")
    if count > 0:
        global timer
        timer = window.after(1000, countDown, count - 1)
    else:
        start_timer()

        marks = ""
        # 0 to reps/2
        workSessions = math.floor(reps / 2)
        for _ in range(workSessions):
            marks += "✔"
        competed_count.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Manage Time with Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#TIME FUNCTION WITH WINDOW
#window.after(1000, say_something, "Hello")

# CANVAS
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timerTxt = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)




# TODO: TIMER LABEL
title = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
title.grid(column=1, row=2)
title.grid(column=1, row=0)


# TODO: BUTTONS
start_btn = Button(text="START", command=start_timer, highlightthickness=0, bg="#3498DB", fg="white")
start_btn.grid(column=0, row=2)


reset_btn = Button(text="RESET", command=reset, highlightthickness=0, bg=RED, fg="white")
reset_btn.grid(column=1, row=2)
reset_btn.grid(column=2, row=2)


# TODO: COMPLETED TASK
competed_count = Label(bg=YELLOW, fg=GREEN)
competed_count.grid(column=1, row=3)

window.mainloop()
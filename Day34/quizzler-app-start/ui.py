from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizGUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("QuizAga")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", foreground="white", bg=THEME_COLOR,
                                 font=("Arial", 16, "bold"))
        self.score_label.grid(row = 0, column = 1)

        self.canvas = Canvas(bg="white", width=300, height=250)
        self.question_test = self.canvas.create_text(150,
                                                     125,
                                                     width=270,
                                                     text="Tester",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 15, "italic")
                                                    )
        self.canvas.grid(row = 1, column = 0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.true_btn = Button(
            image=true_image,
            highlightthickness=0,
            command=self.true_clicked
        )
        self.true_btn.grid(row = 2, column = 0)
        self.false_btn = Button(
            image=false_image,
            highlightthickness=0,
            command=self.false_clicked
        )
        self.false_btn.grid(row = 2, column = 1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            #self.quiz.next_question()


            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_test, text=q_text)
        else:
            self.canvas.itemconfig(self.question_test, text="You've reached the maximum number of questions.")
            #disable true and false buttons
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_clicked(self):
        is_right = self.quiz.check_answer("True")
        self.display(is_right)


    def false_clicked(self):
        is_right = self.quiz.check_answer("False")
        self.display(is_right)

    def display(self, is_right):

        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")

        self.window.after(1000, self.get_next_question)



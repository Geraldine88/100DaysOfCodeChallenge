# CREATE THE QUESTION BACK
from itertools import count

from question_model import Question
from data import question_data
from quiz_brain import  *

# CREATE THE QUESTION BANK WITH LIST OF QUESTION OBJECTS WITH QUESTIONS AND ANSWERS
question_bank = []

for q in question_data:
    question_text = q["question"]
    question_answer = q["correct_answer"]
    question_bank.append(Question(question_text, question_answer))

# CREATE NEW QUIZ
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    # If quiz still has questions
    quiz.next_question()

print("Quiz Completed!")
print(f"Your final score: {quiz.score}/{quiz.question_number}")
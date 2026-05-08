# TODO: Create the QuizBrain class with attributes question_number and  question_list
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        #Keeping track of user's performance
        self.score = 0


    def still_has_question(self):
        return self.question_number < len(self.question_list)



    # TODO: next_question() method pulls up the question from the list depending on which question we're on
    # retrieve item at the current question_number from the question_list
    #Use input to show the user's text and ask for the user's answer
    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {current_q.text}  (True/False): ")
        correct_answer = current_q.answer
        self.check_answer(user_input, correct_answer)


        # TODO: Asking the Question


    # TODO: Checking if the answer was correct
    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect!")

        # Showing the correct answer regardless of the user's answer
        print(f"The correct answer was : {correct_answer}")
        print(f" You got {self.score} / {self.question_number} points.")
        print("\n" * 2)





        # TODO: Checking if we're at the end of the quiz


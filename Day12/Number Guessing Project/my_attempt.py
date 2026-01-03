import art
from art import *
import  random

"""
# Attempting to create a Number Guessing Game.
# """
# TODO: Import logo, welcome the player and tell them the guess range of numbers

logo = art.logo
print(logo)

user_name = input("Hi Player! What is your name? : ").title()
print(f"Welcome, {user_name}, to Geraldine\'s Number Guessing Game!")
print("Geraldine is thinking of a number between 1 and 100.")


# TODO: Ask the user what level of difficulty they want their game to be
# 'easy' gets up to 10 guessing attempts and 'hard' gets only 5 attempts
levels = input("Choose a difficulty. "
                " Type 'easy' or 'hard': ").lower()

#Initializing 'target' which will be the number Geraldine is thinking of
target = random.randint(1, 100)

# Initializing 'nums' to be in range of the numbers 1 to 100 inclusive
# nums = range(101)


# TODO: Creating a function to compute guess
def make_guess(count_guess_left):
    # # Using binary search logic to search the thinking range effectively
    # global guess
    left = 1
    right = 100
    # Computing user's guesses as 'guess'
    # guess = (left + right) // 2
    # count_guess_left = 0
    while count_guess_left > 0:
        guess = int(input("Make a guess: "))
        if guess < left or guess > right:
            print(f"Out of the range. Guess again. ")
            continue

        if guess == target:
            print(f"You got it! The answer was {target}")
            return
        elif guess < target:
            left = guess + 1
            print(f"Too low. Guess again.")

        else:
            right = guess - 1
            print(f"Too high. Guess again.")

        count_guess_left -= 1
        print(f"You have {count_guess_left} attempts left.")

    print("You've run out of guesses. Refresh the page to run again.")
    # return left, right, count_guess_left, guess


# TODO: Computation on when user picks level
if levels == 'easy':

    # print(f"{user_name}, you have {count_guess_left} attempts left to "
    #      f"guess Geraldine\'s number.")

    make_guess(10)
else:
    make_guess(5)

    # print(f"{user_name}, you have {count_guess_left} attempts left to "
    #       f"guess Geraldine\'s number.")



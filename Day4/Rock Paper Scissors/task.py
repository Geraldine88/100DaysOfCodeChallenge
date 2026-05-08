import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock, paper, scissors] # 0, 1, 2

user_input = int(input("What do you choose? \n Type  0 for Rock, 1 for Paper, 2 for Scissors: "))
if user_input >=0  and user_input < 2:
    print(game_image[user_input])

opponent_choice = random.randint(0,2)
print("The opponent chose : ")
print(game_image[opponent_choice])


if user_input >= 3 or user_input <= 0:
    print("You typed an invalid option. You lose!")
elif user_input == 0 and opponent_choice == 2:
    print("You win!")
elif user_input == 2 and opponent_choice == 0:
    print("You lose!")
elif user_input  < opponent_choice:
    print("You lose!")
elif user_input > opponent_choice:
    print("You win!")
elif user_input == opponent_choice:
    print("It's a tie!")
else:
    print("Do over")




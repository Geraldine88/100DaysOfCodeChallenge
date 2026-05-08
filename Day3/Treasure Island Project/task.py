print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_right = input("You\'re at a crossroads. Where do you want to go? \n" 
                    "Do you want to go left or right? : ").lower()
# if left_right == "right":
#     print("Opps! You met a dragon's pit. Game over")
# elif left_right == "left":
#     print("Okay, next question.")
#     swim_wait = input("You\'ve come to a lake."
#                       "There\'s an island in the middle of the lake."
#                       "Would you like to swim or wait? : ").lower()
#     if swim_wait == "swim":
#         print("A dead end into the deep blue. Game over")
#     elif swim_wait == "wait":
#         print("Moving on, Adventurer.")
#         pick_door = input("You\'ve made it to the last stage."
#                           "It\'s time for you to select a door leading to the treasure."
#                           "What door would you like to pick? red, blue or yellow: ").lower()
#         if pick_door == "red" or pick_door == "blue":
#             print("Wrong door of doom, buddy. Game over")
#         elif pick_door == "yellow":
#             print("Congratulations, you found the treasure box! You Win, Adventurer!")
#         else:
#             print("No such door, try again.")
#     else:
#         print("You need to either swim or wait.")
# else:
#     print("Pick the left or right door.")

"""OPTIMIZED CODE"""
if left_right == "left":
    swim_wait = input("You\'ve come to a lake. "
                           " There\'s an island in the middle of the lake. \n"
                           "Would you like to swim or wait? : ").lower()
    if swim_wait == "wait":
        pick_door = input("Patience is a virtue to be rewarded on this journey. "
                            "You\'ve made it to the last stage. "
                            " It\'s time for you to select a door leading to the treasure.\n"
                            "What door would you like to pick? red, blue or yellow: ").lower()
        if pick_door == "red":
            print("You opened the volcano room of burns. Game over!")
        elif pick_door == "blue":
            print("You met with the titan\'s lightening of death. Game over!")
        elif pick_door == "yellow":
            print("Congratulations, Adventurer! You've found the treasure! You win!!")
        else:
            print("Wrong door of doom, buddy. Game over")
    else:
        print("A dead end into the deep blue. Game over")
else:
    print("Opps! You met a dragon's pit. Game over")




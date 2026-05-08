import art
import game_data
import random

data = game_data.data
logo = art.logo
vs = art.vs

print(logo)

def select_celeb(acc):

    name = acc['name']
    followers = acc['follower_count']
    desc= acc['description']
    cntry = acc['country']
    return f"{name}, a {desc} from {cntry}.", followers

def make_guess(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "A"
    else:
        return user_guess == "B"

#Generating random accounts per celebrity
a_celeb = random.choice(data)
b_celeb = random.choice(data)

highest_followers = 0
score_count = 0


if a_celeb == b_celeb:
    b_celeb = random.choice(data)


proceed = True
while proceed:

    a_details, a_followers = select_celeb(a_celeb)
    b_details, b_followers = select_celeb(b_celeb)


    print(f"Compare A: {a_details}.")
    print(vs)
    print(f"Against B: {b_details}.")

    most_popular = input(f"Who has more followers? Type 'A' or 'B': ").upper()

    print("\n" * 10)
    print(logo)
    
    right_choice = make_guess(most_popular, a_followers, b_followers)

    if right_choice:
        score_count += 1
        print(f"You're right! Current score: {score_count}.")

        if most_popular.upper() == "B":
            a_celeb = b_celeb
        b_celeb = random.choice(data)
        if a_celeb == b_celeb:
            b_celeb = random.choice(data)
    else:
        proceed = False
        print(f"Sorry, that's wrong. Final score: {score_count}")


#user_choice = ""



# Check user answer
# score = 0
# if most_popular == make_guess(user_guess):
#     score += 1
#
#     proceed = True
# else:
#
#     proceed = False

    #return most_popular, highest_followers, score_count

import art
from art import *

logo = art.logo
print(logo)


# TODO-1: Ask the user for input
# bidder_name = input("What is your name? : ")
# bidder_price = float(input("How much do you want to bid? : $ "))

# TODO-4: Compare bids in dictionary
def find_highest_bidder(bid_dict):
    winner = ""
    highest_bid = 0
    for bidder in bid_dict:
        bid_amt = bid_dict[bidder]

        # Getting the largest number
        if bid_amt > highest_bid:
            highest_bid = bid_amt
            winner = bidder
    print(f"The winner is {winner} and has the highest bid ${highest_bid}")

# TODO-2: Save data into dictionary {name: price}
bids = {}
# bids[bidder_name] = bidder_price


# TODO-3: Whether if new bids need to be added
# new_bidder = input(" Type 'yes' if there is another bidder, else type 'no' ").lower()
user_get = True
while user_get:

    # while continue bidding (user_get) is True, get their names and price
    bidder_name = input("What is your name? : ")
    bidder_price = float(input("How much do you want to bid? : $ "))

    #add the bid to the dictionary
    bids[bidder_name] = bidder_price

    new_bidder = input(" Type 'yes' if there is another bidder, else type 'no' ").lower()
    # Space between Bidders
    print("\n" * 10)

    if new_bidder == 'no':
        user_get = False
        find_highest_bidder(bids)
    elif new_bidder == 'yes':
        print("\n" * 10)







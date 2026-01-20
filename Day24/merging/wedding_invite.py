# TODO: Create a letter eith starting_letter
#For each name in invites.txt
# Replace [name] placeholder in starting_letter with the actual name found in invites
# Save the letter in the folder, ready_to_send

"""
    # The readlines() method returns a list containing each line in the file as a list item.
    # The strip() method removes any leading, and trailing whitespaces.
    # The replace() method replaces a specified phrase with another specified phrase.

"""

"""
    # With the help of the hints, I want to:
    #    1 - read each name as a item in the list.
    #    2 - create a variable called new_name that contains each name striped of all spaces 
    #    3 - replace old name from invites with new_name
    #    return the letter with new name replacing [name]
    # Also, create a new letter in range in every name in list
    # store each letter in ready_to_send file
"""
#    1 - read each name as a item in the list.
with open("input/names/invites.txt") as invites_file:
    invites = invites_file.readlines()
    # print(invites)

    # 3 - replace old name from invites with new_name
    with open("input/letters/starting_letter.txt") as starting_letters_file:
        wedding_invite = starting_letters_file.read()
        # print(wedding_invite)

#    2 - create a variable called new_name that contains each name stripped of all spaces
    for i in invites:

        cleaned = i.strip()
        letters_new = wedding_invite.replace("[name]",cleaned)

        # Also, create a new letter in range in every name in list
        # store each letter in ready_to_send file
        with open(f"output/ready_to_send/invite_{cleaned}.txt", "w") as invitations_file:
            invitations_file.write(letters_new)








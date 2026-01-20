"""
    This is the instructor's solution, which is way shorter and easier.

"""
PLACEHOLDER = "[name]"

with open("input/names/invites.txt") as names_f:
    names = names_f.readlines()

with open("input/letters/starting_letter.txt") as letters_f:
    letter_content = letters_f.read()

    for name in names:
        stripped = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped)

        with open(f"output/ready_to_send/letter_for_{stripped}.txt", "w") as completed_l:
            completed_l.write(new_letter)
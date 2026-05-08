Number Guessing Game
What I Learned
Functions and Parameters:
- How to define functions that take arguments (like remaining attempts).
- How to return early when the user guesses correctly.
- How to organize game logic inside a reusable function.
Loops and Conditions:
- Using a while loop to control the number of guesses.
- Using if, elif, and else to compare values and give feedback.
- How to update a guessing range based on user input.
Random Module:
- How to use random.randint() to generate a secret number.
- How randomness affects game flow and replayability.

Project
This project is a Number Guessing Game played in the terminal.
The player tries to guess a randomly selected number between 1 and 100.
The game adjusts the valid guessing range after each attempt and gives helpful feedback.

How the Program Works
- The player enters their name and chooses a difficulty:
- easy → 10 attempts
- hard → 5 attempts
- A secret number is generated using random.randint().
- The player makes guesses, and the program responds with:
- Too low
- Too high
- Correct!
- The valid guessing range shrinks after each guess.
- If the player runs out of attempts, the game ends.

Code Rules
- Using random.randint() to generate the target number.
- Using a while loop to track remaining attempts.
- Using comparison operators to guide the player.
- Using continue to handle out‑of‑range guesses.
- Using function parameters to set difficulty levels


Points For Improvements
- Should have put the levels option in a function to make it callable
- Binary search IS NOT needed for this project
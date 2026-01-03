# Hangman – Practice Project (Python)

## Overview

This project recreates the classic Hangman game using Python, turning user guesses into a loop-driven challenge where every wrong letter brings the player closer to defeat. The game continues until the word is fully revealed or all lives are lost.

The project emphasizes game flow control, state tracking, and clean separation of assets.

---

## What Was Built

* A fully playable Hangman game in the terminal
* Random word selection from an external word bank
* Visual life tracking using ASCII art stages
* Real-time feedback for correct, incorrect, and repeated guesses

---

## Core Concepts Practiced

## While Loops

* The game runs continuously until a win or loss condition is met
* Loop control depends on game state rather than a fixed number of turns

### Game State Management

* Lives are tracked and updated dynamically
* Previously guessed letters are stored and reused
* Win and loss conditions are checked every cycle

### Modular Imports

* Word data is imported from `hangman_words.py`
* Visual assets are imported from `hangman_art.py`
* Keeps logic separate from content and visuals

### Conditional Logic

* Detects repeated guesses
* Handles incorrect letters with life deduction
* Reveals only correctly guessed characters

---

## How the Game Works

1. A word is randomly selected from the word list
2. The player guesses one letter at a time
3. Correct guesses reveal letters in place
4. Incorrect guesses reduce remaining lives
5. The game ends when the word is solved or lives reach zero

---

## Why This Project Matters

This project brings together multiple programming fundamentals into a single interactive experience. It reinforces how loops, conditionals, lists, and imports work together to manage a changing game state — a skill essential for larger applications and real-world software.

---

## How to Run

1. Ensure Python 3 is installed
2. Confirm `hangman_words.py` and `hangman_art.py` are in the same directory
3. Run the game:

   ```bash
   python hangman.py
   ```
4. Start guessing — wisely

---

## Final Note

Hangman may be simple on the surface, but behind the scenes it’s a lesson in control flow and structure. Every guess matters, every loop counts — survive the gallows. 

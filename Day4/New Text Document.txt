# Rock, Paper, Scissors – Python Randomized Duel

## Overview

This project recreates the classic Rock, Paper, Scissors game using Python, combining randomness with list-based data storage. The player competes against a computer-controlled opponent whose choices are unpredictable, making every round feel fresh.

The game uses visual ASCII representations to clearly display each move before determining the winner.

---

## What Was Built

* A playable command-line game with user vs computer logic
* Visual feedback using ASCII art stored in lists
* A randomized opponent powered by Python’s `random` module
* Win, lose, tie, and invalid-input detection

---

## Concepts Practiced Today

### Randomization

* `random.randint(0, 2)` is used to simulate an opponent’s choice
* Ensures unpredictable outcomes every round

### Python Lists

* Game assets (rock, paper, scissors) are stored in a list
* List indexing connects numeric input directly to visual output

### Conditional Logic

* Game rules are enforced using ordered conditional checks
* Special cases (rock vs scissors, scissors vs rock) are handled explicitly

### User Input Validation

* Numeric input is evaluated to catch invalid selections
* Prevents unintended list indexing errors

---

## How the Game Works

1. The player selects a move using numbers (0–2)
2. The program displays the player’s choice
3. The opponent randomly selects a move
4. Both choices are compared using logical rules
5. A result is printed: win, lose, or tie

---

## Why This Project Matters

This game demonstrates how **randomness and lists work together** to create dynamic behavior. Instead of hardcoding outcomes, the program reacts in real time to both player input and chance. These techniques form the backbone of simulations, games, and decision-based systems.

---

## How to Run

1. Make sure Python 3 is installed
2. Save the script as `rock_paper_scissors.py`
3. Run the file:

   ```bash
   python rock_paper_scissors.py
   ```
4. Enter a number and challenge the machine

---

## Final Thoughts

This project shows how simple data structures and controlled randomness can turn a few lines of Python into an interactive experience. Every round is different, every outcome earned — may the odds be ever in your favor. 

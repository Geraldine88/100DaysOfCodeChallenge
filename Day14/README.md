# Day 14 - Higher-Lower Game

## Overview

A Python game where you guess which celebrity has more Instagram followers. Each correct guess increases your score, and the winner becomes the next **A** for the following round. The game continues until you guess wrong.

## How to Play

1. Two celebrities are displayed: **A** and **B**.
2. Type **A** or **B** to guess who has more followers.
3. If correct:

   * Your score increases.
   * Winner becomes **A** for the next round, new **B** is chosen.
4. If wrong, the game ends and your final score is shown.

## Features

* Random selection of celebrities from a list of dictionaries
* Functions for displaying celebrity info and checking guesses
* Looping gameplay with dynamic updates
* User input validation

## Example

```
Compare A: Selena Gomez, a musician from USA
VS
Against B: Cristiano Ronaldo, a footballer from Portugal
Who has more followers? Type 'A' or 'B': B
You're right! Current score: 1
```


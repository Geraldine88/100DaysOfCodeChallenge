#  Silent Auction – Dictionaries & Nesting (Python)

## Overview

This project simulates a silent auction where multiple bidders can enter their names and bid amounts without seeing competing offers. Once all bids are collected, the program evaluates the data and announces the highest bidder.

The focus of this project is on **storing structured data** and **processing it efficiently**.

---

## What Was Built

* A silent auction system that accepts unlimited bidders
* A dictionary-based data structure to store bids
* A comparison function to determine the winning bid
* A loop-controlled input system for multiple participants

---

## Core Concepts Practiced

### Dictionaries

* Bidder names are used as keys
* Bid amounts are stored as values
* Enables fast lookups and clean data association

### Nesting & Iteration

* The dictionary is iterated to compare stored values
* Logic is nested inside loops and conditionals to control flow

### Functions

* The winner-detection logic is isolated into a function
* Promotes readability and reuse

### While Loops

* Allows continuous bidding until the auction closes
* Keeps the program interactive and flexible

---

## How the Auction Works

1. A bidder enters their name and bid amount
2. The bid is stored in a dictionary
3. The screen clears to maintain secrecy
4. The process repeats until no new bidders remain
5. The highest bid is calculated and displayed

---

## Why This Project Matters

This project demonstrates how dictionaries make it easy to pair related data and analyze it later. Separating input, storage, and evaluation logic mirrors real-world applications such as pricing systems, leaderboards, and financial tracking tools.

---

## How to Run

1. Ensure Python 3 is installed
2. Confirm `art.py` is in the same directory
3. Run the program:

   ```bash
   python silent_auction.py
   ```
4. Enter bids and close the auction when ready

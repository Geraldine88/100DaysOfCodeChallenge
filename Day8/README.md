# Caesar Cipher – Functions with Inputs (Python)

## Overview

This project implements a Caesar Cipher encryption and decryption tool using Python functions that accept parameters. The program allows users to shift letters forward or backward through the alphabet, transforming readable text into encoded messages and back again.

The cipher can be reused continuously without restarting the program.

---

## What Was Built

* A Caesar Cipher that supports encoding and decoding
* A reusable function that accepts multiple inputs
* Alphabet wrapping using modular arithmetic
* A loop-driven restart system for repeated use

---

## Key Concepts Practiced

### Functions with Inputs

* The `caesar()` function accepts text, shift amount, and direction
* Behavior changes dynamically based on arguments passed in

### While Loops

* Keeps the program running until the user chooses to stop
* Eliminates the need to restart the script manually

### Parameter Control

* Encoding and decoding use the same function
* Direction determines whether the shift moves forward or backward

### Alphabet Indexing

* Characters are shifted using list positions
* `%` ensures shifts wrap correctly from `z` back to `a`

---

## How the Cipher Works

1. The user selects encode or decode
2. A message and shift number are provided
3. Each letter is shifted through the alphabet
4. Non-alphabet characters remain unchanged
5. The final transformed message is displayed

---

## Why This Project Matters

This lesson demonstrates how functions become more powerful when they accept inputs. Instead of writing separate logic for encryption and decryption, one function adapts its behavior based on parameters — a core concept in scalable programming.

---

## How to Run

1. Ensure Python 3 is installed
2. Confirm `art.py` is in the same directory
3. Run the program:

   ```bash
   python caesar_cipher.py
   ```
4. Encode, decode, and repeat as needed



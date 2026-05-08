# Python Calculator – Functions with Output

## Overview

This project builds an interactive calculator that performs basic arithmetic using functions that return values. Instead of printing results directly inside functions, each operation sends its output back to the main program, allowing results to be reused in future calculations.

The calculator supports chained operations without restarting the program.

---

## What We Built

* Arithmetic functions that return results
* A dictionary that maps symbols to functions
* A looping calculator that continues with previous results
* A clean separation between logic and user interaction

---

## Core Concepts Practiced

### Functions with Output

* Each math function returns a value instead of printing
* Returned results are stored and reused dynamically

### Functions as Dictionary Values

* Mathematical operators are linked to their corresponding functions
* Eliminates repetitive conditional logic
* Enables scalable operation handling

### While Loops

* Allows continuous calculations in a single session
* Supports result chaining without resetting the program

### Control Flow

* Operator selection determines which function executes
* User input controls whether the loop continues or resets

---

## How the Calculator Works

1. The user enters a starting number
2. An operator is selected (`+`, `-`, `*`, `/`)
3. A second number is entered
4. The corresponding function executes and returns a result
5. The user decides whether to continue with the result or restart

---

## Why This Project Matters

This project shows how returning values from functions makes programs more flexible and powerful. By treating functions as reusable tools instead of one-time actions, the calculator behaves more like a real application than a one-off script.

---

## How to Run

1. Ensure Python 3 is installed
2. Confirm `art.py` is available in the same directory
3. Run the program:

   ```bash
   python calculator.py
   ```
4. Chain calculations or start fresh as needed


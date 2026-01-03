# Reeborg Hurdle Challenge – Functions & While Loops

## Overview

This project solves the Reeborg hurdle challenge using Python by breaking movement logic into reusable functions and controlling repetition with `while` loops. The robot navigates obstacles autonomously until it reaches the goal flag.

**I got Reeborg through hurdles.**

---

## What Was Accomplished

* Reeborg successfully clears every hurdle
* Movement logic is modularized into readable functions
* The robot adapts to obstacles instead of relying on fixed step counts
* Completion is detected dynamically using goal conditions

---

## Topics Practiced

### Functions

* Custom functions encapsulate repeated movement patterns
* Directional behavior is abstracted for clarity and reuse

### Code Blocks

* Logical sections separate climbing, crossing, and descending actions
* Indentation defines behavior boundaries clearly

### While Loops

* Loops allow Reeborg to react to walls and open paths
* Movement continues until conditions change or the goal is reached

---

## How the Solution Works

* The robot moves forward until a wall is detected
* When blocked, a hurdle-clearing routine is triggered
* Vertical movement continues while walls or paths exist
* The process repeats until Reeborg reaches the flag

---

## Environment

This project runs inside the **Reeborg World** Python environment:

🔗 Reeborg Hurdle World:
[https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json)

---

## Final Note

This challenge demonstrates how functions and while loops turn repetitive motion into intelligent behavior. Instead of counting steps, Reeborg observes, decides, and moves — one hurdle at a time. 🏁

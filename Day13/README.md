# Day 13 – Debugging: Finding and Fixing Bugs

## Overview

Day 13 focused on the art of debugging — understanding why code doesn’t behave the way we expect and learning how to methodically correct it. This lesson emphasized that bugs are not failures, but clues. One of the highlights was the historical story of **Grace Hopper**, whose team discovered an actual moth inside a computer, giving rise to the term *“debugging.”*.



Debugging is about observation, reasoning, and patience. And sometimes, a fresh set of eyes can discover bugs in your code that you never noticed earlier.

---

## Key Takeaways

### Thinking Like the Computer

Instead of assuming what the code *should* do, I learned to step through it line by line and follow exactly how Python interprets each instruction. This approach makes hidden logic errors visible.

### Tracing the Problem

Bugs often appear far from their cause. By checking inputs, outputs, and intermediate values, I practiced tracing issues back to their source rather than treating symptoms.

### Recreating Errors on Purpose

I learned that a bug you can’t reproduce is almost impossible to fix. Testing edge cases and repeating failing scenarios helps isolate the exact conditions that cause issues.

---

## Debugging Strategies Practiced

### Strategic Print Statements

* Printing variable values at critical points to observe unexpected changes
* Using temporary debug labels to distinguish test output from real output

### Controlled Error Handling

* Using `try` / `except` blocks to prevent crashes
* Creating clearer error messages to understand what went wrong and why

### Debugging Tools

* Learning when and why to use debuggers instead of relying only on prints
* Inspecting variables during runtime to understand program state

---

## Habits That Improve Debugging

* **Run code often**, not just at the end
* **Change one thing at a time** to avoid confusion
* **Take breaks** — fresh eyes catch mistakes faster
* **Look up known issues** when stuck (because chances are, someone else has hit the same wall)
* **Use tools like pythontutor.com** — to see your code execution visually, one line at a time.

---

## Why This Lesson Matters

Debugging is a core programming skill that applies everywhere — from simple scripts to large applications. Writing code is only half the job; understanding, correcting, and improving it is what makes a developer reliable.

Grace Hopper’s moth may have been physical, but most bugs today live quietly in logic — waiting to be found.

---

## Final Reflection

This lesson reinforced that bugs aren’t signs of failure — they’re part of the process. Debugging trains patience, sharpens reasoning, and builds confidence. Every fixed bug is a small win, and every confusing error is an opportunity to understand code more deeply.



# Object-Oriented Inheritance Demo  
A simple Python project demonstrating class inheritance

This project shows how **inheritance** works in Python using a base class `Animal` and a derived class `Fish`. It highlights how child classes can:

- Inherit attributes  
- Inherit methods  
- Override methods  
- Extend behavior using `super()`  

---

## Concept Overview

### **Animal (Parent Class)**  
Represents a generic animal with:

- `num_eyes` attribute  
- `breathe()` method  

### **Fish (Child Class)**  
Inherits from `Animal` and:

- Calls the parent constructor using `super()`  
- Overrides the `breathe()` method  
- Adds a new method `swim()`  

This demonstrates how subclasses can reuse and extend parent functionality.

---

## What the Code Does

1. Creates an `Animal` with 2 eyes  
2. Defines a `Fish` that:
   - Can swim  
   - Breathes both like an animal **and** underwater  
3. Instantiates a `Fish` named `nemo`  
4. Calls:
   - `nemo.swim()`  
   - `nemo.breathe()`  
   - `print(nemo.num_eyes)`  

---

## Expected Output

When you run the script, you’ll see:

```
********* moving in water ********
Inhale, exhale
~~~~~~~~~~~~~~~~~ Breathe Under Water ~~~~~~~~~~~~~~~~~
2
```

This shows:

- The fish can swim  
- The fish uses the parent’s breathing behavior  
- The fish adds its own underwater breathing behavior  
- The fish inherits the `num_eyes` attribute from `Animal`  

---

## How to Run

1. Save the script as `inheritance_demo.py`  
2. Run it with:

```bash
python inheritance_demo.py
```

3. Observe the output in your terminal.

---

## Requirements

- Python 3.x  
- No external libraries needed  

---

## Learning Highlights

This project teaches:

- How to define a parent class  
- How to create a child class  
- How to use `super()`  
- How to override methods  
- How attributes are inherited  

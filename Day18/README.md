# Spirograph Turtle Art  
A colorful Python Turtle Graphics project

This project uses Python’s built‑in `turtle` module to draw a vibrant, rotating **spirograph** pattern. Each circle in the spirograph is drawn in a randomly generated RGB color, creating a beautiful, hypnotic design.

---

## Features

- Uses Python’s `turtle` graphics module  
- Generates **random RGB colors** for each circle  
- Draws a full 360° spirograph using a customizable angle gap  
- Runs smoothly using `speed("fastest")`  
- Produces unique artwork every time  

---

## How It Works

1. The turtle is set to **RGB color mode** (`colormode(255)`).
2. A helper function `random_color()` generates a random `(r, g, b)` tuple.
3. The `draw_spirograph(size_gap)` function:
   - Repeats drawing circles until it completes 360 degrees  
   - After each circle, the turtle rotates by `size_gap` degrees  
   - Each circle uses a new random color  
4. The result is a full spirograph made of overlapping circles.

---

## Example Output

The program produces a colorful circular pattern similar to a geometric flower or mandala.  
Every run looks different because the colors are randomized.

---

## Code Structure

- `random_color()` → generates random RGB colors  
- `draw_spirograph(size_gap)` → draws the full spirograph  
- `nunu_the_wise` → the turtle drawing the pattern  
- `screen.exitonclick()` → keeps the window open until clicked  

---

## How to Run

1. Install Python (3.x recommended).  
2. Save the script as `spirograph.py`.  
3. Run it:

```bash
python spirograph.py
```

4. A Turtle Graphics window will open and draw the spirograph automatically.

---

## Customization

You can tweak:

### Circle size  
Change:

```python
nunu_the_wise.circle(100)
```

### Rotation gap  
Change the function call:

```python
draw_spirograph(5)
```

Smaller gap → more circles → denser pattern  
Larger gap → fewer circles → simpler pattern

### Turtle speed  
Try:

```python
nunu_the_wise.speed("fastest")
```

---

## Requirements

- Python 3.x  
- No external libraries needed (uses built‑in `turtle` and `random`)

---

## Ideas for Extensions

- Add keyboard controls  
- Save the drawing as an image  
- Animate color transitions  
- Let the user choose circle size or gap  


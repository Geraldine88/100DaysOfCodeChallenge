# Aga Snake Game

A classic Snake game built with Python's Turtle graphics library. Control the snake to eat food, grow longer, and avoid crashing into walls or yourself!

## Features

- **Smooth snake movement** with keyboard controls
- **Dynamic food spawning** at random locations
- **Score tracking** that increases with each food eaten
- **Difficulty levels** (Easy, Medium, Hard) that control game speed
- **Collision detection** for walls and self-collision
- **Growing snake** that extends with each food consumed
- **Game over screen** when you crash

## How to Play

1. Run the main game file
2. Choose your difficulty level when prompted:
   - **Easy**: Slower speed (0.2s delay)
   - **Medium**: Moderate speed (0.1s delay)
   - **Hard**: Fast speed (0.05s delay)
3. Use arrow keys to control the snake:
   - **Up Arrow**: Move up
   - **Down Arrow**: Move down
   - **Left Arrow**: Move left
   - **Right Arrow**: Move right
4. Eat the brown food circles to grow and increase your score
5. Avoid hitting the walls or your own tail!

## Installation & Running

### Prerequisites
- Python 3.x installed on your system
- Turtle graphics library (comes pre-installed with Python)

### Running the Game
```bash
python main.py
```

## Project Structure

```
snake-game/
│
├── main.py              # Main game loop and logic
├── aga_snake.py         # Snake class (movement, growth, direction)
├── food.py              # Food class (spawning, positioning)
├── score_board.py       # Scoreboard class (score tracking, game over)
└── README.md            # This file
```

## Game Rules

- The snake starts with 3 segments
- Each food eaten adds one segment to the snake's body
- The snake cannot reverse direction (e.g., can't go down if moving up)
- Game ends if:
  - Snake hits any of the four walls
  - Snake collides with its own body

## Technical Details

### Classes

**Snake Class** (`aga_snake.py`)
- Manages snake segments, movement, and direction
- Handles growth when food is eaten
- Prevents illegal moves (reversing direction)

**Food Class** (`food.py`)
- Creates food as a small brown circle
- Randomly spawns food within game boundaries
- Refreshes to new location when eaten

**Scoreboard Class** (`score_board.py`)
- Displays current score at top of screen
- Updates score when food is eaten
- Shows "GAME OVER" message when game ends

### Game Settings

- **Screen size**: 600x600 pixels
- **Snake segment size**: 20x20 pixels
- **Food size**: 10x10 pixels
- **Movement distance**: 20 pixels per step
- **Collision detection**: 15 pixels for food, 10 pixels for tail

## Customization

You can customize the game by modifying:

**Colors**:
```python
# In main.py
screen.bgcolor("green")  # Change background color

# In aga_snake.py
snake.color("gold")      # Change snake color

# In food.py
self.color("brown")      # Change food color
```

**Speed**:
```python
# In main.py - modify the difficulty speeds
if difficulty == "easy":
    speed = 0.2  # Adjust this value
```

**Screen Size**:
```python
# In main.py
screen.setup(width=600, height=600)  # Change dimensions
```



## Future Enhancements

Potential features to add:
- High score tracking
- Progressive difficulty (speed increases with score)
- Power-ups and special foods
- Obstacles in the playing field

## Author

Coded as guided as part of the 100 Days of Code challenge


## Acknowledgments

Built using Python's Turtle graphics library - a great tool for learning game development!

---

**Enjoy the game!**
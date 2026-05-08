# Turtle Crossing Game

A classic Frogger-style game built with Python's Turtle graphics library. Help the turtle cross the busy road while avoiding colorful cars! Each successful crossing increases the difficulty.

## Features

- **Progressive difficulty** - cars move faster with each level
- **Random car generation** - unpredictable traffic patterns
- **Level tracking** - displays current level on screen
- **Collision detection** - game ends if turtle hits a car
- **Colorful graphics** - multi-colored cars on a gray road
- **Smooth animations** - optimized screen updates
- **Simple controls** - easy-to-learn, hard-to-master gameplay

## How to Play

### Controls

- **Up Arrow**: Move turtle forward (toward finish line)
- **Down Arrow**: Move turtle backward (toward starting position)

### Objective

1. Guide the white turtle from the bottom of the screen to the top
2. Avoid getting hit by the moving cars
3. Successfully reach the finish line to advance to the next level
4. Each level increases the car speed - how many levels can you complete?

### Game Rules

- Turtle starts at the bottom center of the screen
- Cars spawn randomly on the right side and move left
- If the turtle collides with a car (within 20 pixels), game over!
- Successfully crossing resets turtle position and increases difficulty
- No time limit - take your time, but don't get hit!

## Installation & Running

### Prerequisites
- Python 3.x installed on your system
- Turtle graphics library (comes pre-installed with Python)

### Running the Game
```bash
python main.py
```
*(Replace `main.py` with your actual main file name)*

## Project Structure

```
turtle-crossing-game/
│
├── main.py              # Main game loop and collision logic
├── turtle_cross.py      # Player class (turtle movement and positioning)
├── cars.py              # Cars class (vehicle generation and movement)
├── points.py            # Points class (level tracking and game over)
└── README.md            # This file
```

##  Game Mechanics

### Turtle Movement
- Starts at position (0, -280) at the bottom of the screen
- Moves 10 pixels per keypress
- Resets to starting position after successful crossing
- Cannot move off the screen boundaries

### Car System
- Cars spawn randomly at x=300 (right edge)
- Random y-position between -280 and 280
- 1 in 6 chance of spawning each frame (approximately)
- Cars are 20px high and 40px wide
- Six different colors: red, orange, yellow, green, blue, purple
- Initial speed: 5 pixels per frame
- Speed increases by 10 pixels per level

### Collision Detection
- Collision occurs when turtle is within 20 pixels of car center
- Uses distance calculation for accurate detection
- Game ends immediately upon collision

### Level Progression
- Starts at Level 1
- Level increases each time turtle reaches finish line (y > 280)
- Car speed increases by 10 pixels per level
- Level displayed in top-left corner

## Technical Details

### Classes

**Player Class** (`turtle_cross.py`)
- Inherits from Turtle
- White turtle shape facing upward
- Movement methods: `go_up()`, `go_down()`
- Helper methods: `at_finish()`, `at_start()`
- Starting position: (0, -280)
- Movement distance: 10 pixels

**Cars Class** (`cars.py`)
- Manages list of all car objects
- Methods: `make_vehicle()`, `drive_vehicle()`, `increase_speed()`
- Cars stored in `self.vehicles` list
- Random color selection from COLORS list
- Dynamic speed adjustment

**Points Class** (`points.py`)
- Inherits from Turtle
- Displays current level at top-left
- Methods: `update_points()`, `increase_level()`, `game_over()`
- White text with Courier font

### Game Settings

- **Screen size**: 600x600 pixels
- **Background color**: Gray
- **Turtle size**: Default (20x20 pixels)
- **Car size**: 20x40 pixels (stretch_wid=1, stretch_len=2)
- **Frame rate**: 0.1 seconds per frame
- **Starting car speed**: 5 pixels/frame
- **Speed increase per level**: 10 pixels/frame
- **Finish line**: y-coordinate > 280
- **Starting line**: y-coordinate = -280
- **Collision threshold**: 20 pixels

## Customization

### Change Turtle Color
```python
# In turtle_cross.py Player.__init__
self.color("green")  # Change from white to green
```

### Adjust Difficulty
```python
# In cars.py
STARTING_MOVE_DISTANCE = 3  # Make easier (slower cars)
MOVE_INCREMENT = 15  # Make harder (bigger speed jumps)
```

### Modify Car Spawn Rate
```python
# In cars.py make_vehicle() method
rand = random.randint(1, 3)  # More cars (was 1, 6)
```

### Add More Colors
```python
# In cars.py
COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]
```

### Change Movement Speed
```python
# In turtle_cross.py
MOVE_DISTANCE = 15  # Turtle moves faster (was 10)
```

### Adjust Screen Size
```python
# In main file
screen.setup(width=800, height=800)  # Larger playing field
```

## Game Enhancements

### Add Score System
```python
# In points.py, add to __init__
self.score = 0

# Create method
def increase_score(self, points):
    self.score += points
    self.update_points()
```

### Add Sound Effects
```python
# Requires winsound (Windows) or playsound library
import winsound

# In collision detection
winsound.Beep(1000, 200)  # Crash sound
```

### Add High Score
```python
# In points.py
self.high_score = 0

# Update when level increases
if self.level > self.high_score:
    self.high_score = self.level
```

### Add Lives System
```python
# In main file
lives = 3

# In collision detection
lives -= 1
if lives == 0:
    cross_now = False
    score.game_over()
```

## Troubleshooting

### Cars Not Appearing
- Make sure `screen.tracer(0)` is set before creating objects
- Check that `screen.update()` is in the game loop
- Verify random spawn rate isn't too low

### Turtle Moves Too Fast/Slow
- Adjust `MOVE_DISTANCE` in `turtle_cross.py`
- Modify `time.sleep()` value in main loop

### Collision Detection Too Sensitive
- Increase collision threshold: `if v.distance(turtle_player) <= 25:`
- Adjust car size or turtle size


##  Learning Objectives

This project demonstrates:
- Object-oriented programming with multiple classes
- Game loop architecture and state management
- Collision detection algorithms
- Random generation and probability
- Event-driven programming with keyboard input
- Progressive difficulty scaling
- Screen refresh and animation optimization
- Modular code organization across multiple files


## Challenge Modes

Try these self-imposed challenges:
- **Speed Run**: Complete 10 levels as fast as possible
- **Minimalist**: Cross using the fewest moves
- **One Life**: No mistakes allowed - one hit and restart
- **Blindfolded** (audio cues only - requires modification)

##

Created as part of the 100 Days of Code challenge - Day 23

##

This project is open source and available for educational purposes.

## Acknowledgments

- Built using Python's Turtle graphics library
- Inspired by the classic Frogger arcade game (1981)
- Great project for learning game development and OOP concepts
- Creator of the 100DaysOfCode bootcamp

---

**Good luck crossing the road!**
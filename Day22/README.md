# Ping-Pong Game

A classic two-player Pong game built with Python's Turtle graphics library. Challenge your friend in this timeless arcade game where reflexes and precision are key!

## Features

- **Two-player gameplay** with independent paddle controls
- **Realistic ball physics** with bouncing mechanics
- **Dynamic speed increase** - ball gets faster after each paddle hit
- **Score tracking** for both players
- **Automatic ball reset** when a point is scored
- **Smooth animations** with optimized screen updates
- **Color-coded paddles** for easy player identification

## How to Play

### Controls

**Player 1 (Right Paddle - Red)**
- **Up Arrow**: Move paddle up
- **Down Arrow**: Move paddle down

**Player 2 (Left Paddle - Gold)**
- **W Key**: Move paddle up
- **S Key**: Move paddle down

### Game Rules

1. Each player controls a paddle on their side of the screen
2. The ball bounces between the paddles
3. If a player misses the ball, their opponent scores a point
4. The ball speeds up slightly after each successful paddle hit
5. First player to reach the target score wins!

### Running the Game
```bash
python Screen.py
```

## 📁 Project Structure

```
pong-game/
│
├── Screen.py            # Main game loop and collision detection
├── paddlers.py          # Paddle class (movement and positioning)
├── ball_pong.py         # Ball class (movement, bouncing, reset)
├── track_score.py       # Scoreboard class (score tracking and display)
└── README.md            # This file
```

## Game Mechanics

### Ball Movement
- Ball starts at the center of the screen (0, 0)
- Moves diagonally with initial speed of 10 pixels per frame
- Direction reverses when hitting walls or paddles
- Speed increases by 10% after each paddle collision

### Collision Detection
- **Wall collision**: Ball bounces when hitting top or bottom walls (y-coordinate > 280 or < -280)
- **Paddle collision**: Ball bounces when within 50 pixels of a paddle and at the paddle's x-position
- **Scoring**: Point awarded when ball goes past the paddle (x-coordinate > 380 or < -380)

### Scoring System
- Left player scores when ball passes right paddle
- Right player scores when ball passes left paddle
- Score displayed at the top of the screen
- Ball resets to center after each point


### Classes

**Paddle Class** (`paddlers.py`)
- Inherits from Turtle
- 20x100 pixel rectangular shape
- Positioned at screen edges (±350, 0)
- Moves 20 pixels per keypress

**Ball Class** (`ball_pong.py`)
- Inherits from Turtle
- Circular shape
- Independent x and y movement vectors
- Dynamic speed adjustment via `pace` attribute

**ScoreBoard Class** (`track_score.py`)
- Inherits from Turtle
- Displays scores at top of screen
- Auto-updates when points are scored
- White text with Courier font

### Game Settings

- **Screen size**: 800x600 pixels
- **Background color**: Black
- **Paddle size**: 20x100 pixels
- **Ball speed**: 10 pixels/frame (increases with each hit)
- **Frame rate**: Controlled by ball.pace (starts at 0.1 seconds)
- **Wall boundaries**: ±280 pixels (top/bottom)
- **Scoring boundaries**: ±380 pixels (left/right)


### Change Paddle Colors
```python
# In Screen.py
l_paddle.color("gold")  
r_paddle.color("red")  
```

### Adjust Ball Speed
```python
# In ball_pong.py __init__ method
self.x_move = 15 
self.y_move = 15  
self.pace = 0.05 
```

### Modify Paddle Size
```python
# In paddlers.py __init__ method
self.shapesize(stretch_len=1, stretch_wid=7) 
```

### Change Screen Dimensions
```python
# In Screen.py
screen.setup(width=1000, height=800)  # Larger playing field
```

### Adjust Speed Increase Rate
```python
# In ball_pong.py bounce_x method
self.pace *= 0.8  # Makes ball speed up faster (was 0.9)
```

## Game Variations

### Add Winning Condition
```python
# In Screen.py, inside the game loop
if scoreboard.l_score == 5:
    scoreboard.goto(0, 0)
    scoreboard.write("LEFT PLAYER WINS!", align="center", font=("Courier", 40, "bold"))
    start_game = False
```

### Add Center Line
```python
# In Screen.py, after creating screen
line = Turtle()
line.color("white")
line.penup()
line.goto(0, 300)
line.setheading(270)
for _ in range(30):
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(10)
line.hideturtle()
```

## Future Enhancements

Potential features to add:
- Single-player mode with AI opponent
- Difficulty levels (easy, medium, hard)
- Sound effects for paddle hits and scoring
- Power-ups (speed boost, paddle size change)
- Winning screen with replay option
- High score persistence
- Particle effects on ball collision
- Adjustable winning score
- Pause functionality

## Learning Objectives

This project demonstrates:
- Object-oriented programming (OOP) with classes and inheritance
- Game loop architecture
- Collision detection algorithms
- Event handling with keyboard input
- Screen refresh and animation techniques
- Modular code organization

## Author

This project was created as part of the 100 Days of Code challenge - Day 22


## Acknowledgments

- Guided by tutor of the 100 days of code 
- Inspired by the classic Atari Pong game (1972)
- Perfect project for learning game development fundamentals

---

**Enjoy the game! May the best player win! **
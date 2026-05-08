# Day 28: Pomodoro Timer

A Tkinter desktop Pomodoro timer app using Tkinter to help manage work sessions and breaks using the Pomodoro Technique.

## What I Learned

### Time Management with Tkinter
- I used `window.after()` to schedule function calls after delays
- I implemented `window.after_cancel()` to stop running timers
- I created recursive countdown functions
- I managed global state across multiple function calls

### Pomodoro Technique Implementation
- 25-minute work sessions
- 5-minute short breaks (after odd work sessions)
- 20-minute long breaks (after every 4 work sessions)
- Visual checkmarks to track completed work sessions

### UI Components Used
- Canvas widget to display images and text overlays
- Dynamic text updates with `canvas.itemconfig()`
- Color-coded labels to indicate different timer states
- Grid layout for button placement

### Programming Concepts Applied
- Global variables to track timer state and repetitions
- Mathematical operations with `math.floor()` for time formatting
- String formatting for zero-padded seconds display
- Modulo operator to determine work/break cycles


### Timer Cycle Logic
```
Work (25 min) → Short Break (5 min) → Work → Short Break → 
Work → Short Break → Work → Long Break (20 min) → Repeat
```

### Implemention
1. **START button** - Begins the timer cycle
2. **RESET button** - Stops the timer and resets to 00:00
3. **Color indicators**:
   - Green "Work" = Work session
   - Pink "Break" = Short break
   - Red "Break" = Long break
4. **Checkmarks** - One ✔ appears after each completed work session


### My Countdown Function
A recursive countdown that:
- Converts seconds to MM:SS format
- Updates the canvas text every second
- Automatically starts the next session when timer hits 0
- Adds checkmarks after work sessions


## Key Features Built

Automatic cycle between work and breaks  
Visual timer countdown  
Color-coded session types  
Progress tracking with checkmarks  
Reset functionality  
Clean, minimal UI  

## What I'd Improve Next

- Add sound notifications when sessions end
- Allow custom work/break durations
- Add pause functionality
- Save session history
- Display statistics (total work time, sessions completed)

---

**Pomodoro Technique**: Work for 25 minutes, break for 5. After 4 sessions, take a longer 20-minute break.
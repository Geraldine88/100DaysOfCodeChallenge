# Day 34: Quiz App with GUI
```

## Project Overview

**GUI-based Trivia Quiz Application**

This project builds upon Day 17's quiz app by adding a graphical user interface using Tkinter and fetching real quiz questions from the Open Trivia Database API.

## Features

- **Beautiful GUI** - Interactive Tkinter interface
- **API Integration** - Fetches random trivia questions from Open Trivia DB
- **Real-time Feedback** - Visual feedback for correct/incorrect answers
- **Score Tracking** - Live score display
- **Question Bank** - Multiple questions with True/False format
- **OOP Design** - Clean separation of concerns (Model, Logic, UI)

## Technologies Used

- **tkinter** - GUI interface
- **requests** - API calls to fetch quiz data
- **OOP** - Object-Oriented Programming principles
- **API** - Open Trivia Database

## Project Architecture

### Object-Oriented Design (MVC Pattern):

1. **Model** (`question_model.py`)
   - `Question` class - Stores question text and answer

2. **Controller** (`quiz_brain.py`)
   - `QuizBrain` class - Handles quiz logic, scoring, question flow

3. **View** (`ui.py`)
   - `QuizGUI` class - Manages user interface and interactions

4. **Data** (`data.py`)
   - Fetches questions from API
   - Formats data for the application

5. **Main** (`main.py`)
   - Coordinates all components
   - Creates question bank
   - Initializes quiz and GUI
```

## GUI Components

- **Canvas** - Question display area
- **Buttons** - True/False answer buttons
- **Score Label** - Current score tracker
- **Visual Feedback** - Green (correct) / Red (incorrect) background flash

## API Integration

**Open Trivia Database API:**
```python
# Example API endpoint
url = "https://opentdb.com/api.php?amount=10&type=boolean"
```

**Response format:**
```json
{
  "question": "Question text here",
  "correct_answer": "True"
}
```

## Key Concepts Practiced

### From Day 17 (Enhanced):
- Object-Oriented Programming
- Class design and methods
- Quiz logic implementation

### New in Day 34:
- **Tkinter GUI** - Building interactive interfaces
- **API Integration** - Fetching live data
- **Event Handling** - Button clicks and user input
- **Canvas Manipulation** - Dynamic text updates
- **Visual Feedback** - Color changes for user experience

## Configuration

**Customize quiz settings in `data.py`:**
- Number of questions
- Question difficulty
- Question category
- Question type (True/False, Multiple Choice)

## Code Evolution

**Day 17 (Console):**
```python
while quiz.still_has_questions():
    quiz.next_question()
```

**Day 34 (GUI):**
```python
quizGUI = QuizGUI(quiz)
# GUI handles question flow with button clicks
```

##  Learning Outcomes

- Transformed console application into GUI
- Integrated external APIs for dynamic content
- Applied OOP principles with multiple classes
- Created interactive user experience
- Practiced separation of concerns (MVC pattern)

---

**Day 34 Complete!** Quiz app upgraded with GUI and live API data.

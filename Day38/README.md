# Workout Tracker with API + Regex Fallback

A Python project that logs workouts to a Google Sheet using the 100 Days of Python Exercise API. The script accepts **any workout description** — cardio, generic exercises, or complex strength‑training commands — and automatically extracts the needed information using either the API or a custom regex parser.

## What This Project Does
- Sends natural‑language workout descriptions to the Exercise API  
- Accepts both API response formats (`workouts` and `exercises`)  
- Falls back to a regex parser when the API cannot understand the input  
- Logs each workout to Sheety (Google Sheets)  
- Supports API Key, Basic Auth, or Bearer Token authentication  
- Loads all sensitive values from a `.env` file  
- Prints a clean summary of each logged workout  

This makes the tracker flexible enough to handle inputs like:

- “Walking for 20 minutes”  
- “Riding for 15 minutes”  
- “Hamstring curl at 60kg for 20 minutes”  
- “Leg press 100kg 10 reps x 3 sets”  

## How It Works

### 1. API Parsing  
The script first sends the workout text to the Exercise API.  
Depending on the input, the API may return:

- `"workouts"` (cardio-style)  
- `"exercises"` (generic)  

Both formats are supported.

### 2. Regex Fallback  
If the API cannot parse the workout, the script uses a custom regex parser to extract:

- exercise name  
- weight  
- reps  
- sets  
- duration  

This ensures **every input** produces a valid workout entry.

### 3. Logging to Sheety  
Each workout is sent to a Google Sheet using Sheety.  
Authentication can be done using:

- API Key (default)  
- Basic Auth  
- Bearer Token  

Only one method is used at a time.

### 4. Final Output  
After logging, the script prints a clean summary:

```
Logged Workout:
- Exercise: Hamstring Curl
- Duration: 20 min
- Calories: 0
```

## Environment Variables

Create a `.env` file in the project folder

## Project Structure

```
project/
│
├── main.py
├── .env
├── README.md
└── requirements.txt
```

Enter your workout when prompted:

```
What exercises did you do?: Hamstring curl at 60kg for 20 minutes
```

The workout will be:

- parsed (API or regex)  
- logged to Sheety  
- printed to the console  

## Possible Improvements

- Add calorie estimation for strength training  
- Support multiple exercises in one input  
- Add a CLI menu for different logging modes  
- Store reps/sets/weight in the Google Sheet  
- Add error logging for debugging  

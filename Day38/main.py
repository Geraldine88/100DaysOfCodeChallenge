# ************************ IMPORTATIONS **************************** #
import requests
from dotenv import load_dotenv
import os
from datetime import datetime
import re

load_dotenv()

# ************************ CONSTANTS **************************** #
APP_ID = os.getenv("X_APP_ID")
API_KEY = os.getenv("X_APP_KEY")

GENDER = os.getenv("GENDER")
WEIGHT_KG = float(os.getenv("WEIGHT_KG"))
HEIGHT_CM = float(os.getenv("HEIGHT_CM"))
AGE = int(os.getenv("AGE"))

BASIC_USERNAME = os.getenv("BASIC_USERNAME")
BASIC_PASSWORD = os.getenv("BASIC_PASSWORD")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# ************************ REGEX PARSER **************************** #
def parse_strength_workout(text):
    workout = {}

    # Extract weight (e.g., 60kg, 120 lbs)
    weight_match = re.search(r'(\d+)\s*(kg|lbs?)', text, re.IGNORECASE)
    if weight_match:
        workout["weight"] = int(weight_match.group(1))
        workout["unit"] = weight_match.group(2).lower()
    else:
        workout["weight"] = None
        workout["unit"] = None

    # Extract duration (e.g., 20 minutes)
    duration_match = re.search(r'(\d+)\s*(minutes?|mins?)', text, re.IGNORECASE)
    if duration_match:
        workout["duration_min"] = int(duration_match.group(1))
    else:
        workout["duration_min"] = None

    # Extract reps and sets (e.g., 10 reps x 3 sets)
    reps_match = re.search(r'(\d+)\s*reps?', text, re.IGNORECASE)
    sets_match = re.search(r'(\d+)\s*sets?', text, re.IGNORECASE)

    workout["reps"] = int(reps_match.group(1)) if reps_match else None
    workout["sets"] = int(sets_match.group(1)) if sets_match else None

    # Extract exercise name (everything before weight or duration)
    name_match = re.split(r'at|\d+|\bfor\b', text, maxsplit=1, flags=re.IGNORECASE)
    workout["name"] = name_match[0].strip().title()

    return workout

# ************************ API CALLS AND ENDPOINTS **************************** #
base_url = "https://app.100daysofpython.dev"
exercise_endpoint = f"{base_url}/v1/nutrition/natural/exercise"
sheety_url = os.getenv("SHEETY_URL")
sheety_endpoint_end = os.getenv("SHEETY_ENDPOINT_END")
sheet_endpoint = f"{sheety_url}/{sheety_endpoint_end}"
# POST /v1/nutrition/natural/exercise

# GETTING USER'S INPUT WORKOUT
workout_input = input("What exercises 🏋️ did you do?: ")

# DEFINING HEADERS
headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

# PARAMETERS FOR THE API CALL
params = {
    'query': workout_input,
    'gender': GENDER,
    'weight': WEIGHT_KG,
    'height': HEIGHT_CM,
    'age': AGE,
}

response = requests.post(exercise_endpoint, json=params, headers=headers)
result = response.json()
# print(result)

# -------------------------------
# Accept "workouts", "exercises", or fallback to regex parser
# -------------------------------
if "workouts" in result:
    workout_list = result["workouts"]

elif "exercises" in result:
    workout_list = result["exercises"]

else:
    print("API could not parse this. Falling back to strength parser.")
    parsed = parse_strength_workout(workout_input)

    # Convert parsed strength workout into API-like structure
    workout_list = [{
        "name": parsed["name"],
        "duration_min": parsed["duration_min"] if parsed["duration_min"] else 0,
        "nf_calories": 0  # No calorie data for strength training
    }]

today = datetime.now().strftime("%d/%m/%Y")
now = datetime.now().strftime("%X")

for workout in workout_list:
    sheet_inputs = {
        "workout": {
            'date': today,
            'time': now,
            'exercise': workout['name'].title(),
            'duration': workout['duration_min'],
            'calories': workout['nf_calories'],
        }
    }

    sheet_res = requests.post(sheet_endpoint, json=sheet_inputs, headers=headers)
    print(sheet_res.text)

    # ************* FINAL PRINTED RESULT *************
    print(
        f"\nLogged Workout:\n"
        f"- Exercise: {workout['name'].title()}\n"
        f"- Duration: {workout['duration_min']} min\n"
        f"- Calories: {workout['nf_calories']}\n"
    )

#Basic Authentication
sheet_response = requests.post(
  sheet_endpoint,
  json=sheet_inputs,
  auth=(
      BASIC_USERNAME,
      BASIC_PASSWORD,
  )
)

#Bearer Token Authentication
bearer_headers = {
"Authorization": f"Bearer {BEARER_TOKEN}"
}
sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    headers=bearer_headers
)
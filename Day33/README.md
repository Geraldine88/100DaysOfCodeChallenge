# Day 33: API Requests & ISS Tracker

## Project Structure

```
Day33/
├── kanye-quotes/
│   ├── background.png        # Kanye quote background image
│   ├── kanye.png             # Kanye button image
│   └── main.py               # Kanye Quotes GUI app
│
└── issoverhead-start/
    └── main.py               # ISS Overhead Tracker with email alerts
```

## Projects Overview

### 1. Kanye Quotes App
**GUI application that displays random Kanye West quotes**

**Features:**
- Tkinter GUI with background image
- Fetches quotes from Kanye REST API
- Click Kanye button to get new quotes
- Quotes displayed on canvas overlay

**API Used:** `https://api.kanye.rest/`

---

### 2. ISS Overhead Tracker
**Automated email notifier when ISS passes overhead at night**

**Features:**
- Checks ISS position every 60 seconds
- Determines if it's nighttime using sunrise/sunset API
- Sends email alert when ISS is overhead AND it's dark
- Location-based tracking (latitude/longitude)

**APIs Used:**
- ISS Position: `http://api.open-notify.org/iss-now.json`
- Sunrise/Sunset: `https://api.sunrise-sunset.org/json`

**Email:** Uses Gmail SMTP with app password

---

## Technologies Used

- **requests** - HTTP requests to APIs
- **tkinter** - GUI for Kanye quotes
- **smtplib** - Email notifications
- **datetime** - Time checking and formatting
- **pandas** - CSV handling (if used)

## Key Concepts Learned

### API Requests
```python
response = requests.get(url="https://api.example.com", params=parameters)
response.raise_for_status()  # Raise exception for bad status codes
data = response.json()        # Parse JSON response
```

### HTTP Status Codes
- **1XX** - Hold on (informational)
- **2XX** - Success (here you go)
- **3XX** - Redirect (go away, no permission)
- **4XX** - Client error (you screwed up - 404)
- **5XX** - Server error (server screwed up)

### API Parameters
```python
parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0
}
response = requests.get(url, params=parameters)
```

### Error Handling
```python
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
except Exception as e:
    print(f"Error: {e}")
```

##  How to Run

### Kanye Quotes:
```bash
cd kanye-quotes
python main.py
```

### ISS Tracker:
```bash
cd issoverhead-start
python main.py
```

**Note:** Update `my_gmail`, `my_yahoomail`, and `gmail_password` with your credentials.

## Gmail Setup

1. Enable 2-Factor Authentication
2. Go to Google Account → Security → App Passwords
3. Generate app password for "Mail"
4. Use 16-character password in code

## Configuration

**ISS Tracker:** Update your location coordinates:
```python
MY_LAT = 51.507351   # Your latitude
MY_LONG = -0.127758  # Your longitude
```

---

**Day 33 Complete! 🎉 Learned API requests, error handling, and email automation.

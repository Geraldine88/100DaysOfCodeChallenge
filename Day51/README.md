# Internet Speed Complaint Bot  
Automated Speed Test + Complaint Poster (Day 51 – 100 Days of Python)

This project automates two tasks:

1. **Runs an internet speed test** using Selenium and extracts your download/upload speeds.  
2. **Logs into the Y‑app (100 Days of Python service)** and automatically posts a complaint message based on your results.

It’s a practical automation project that combines web scraping, browser automation, environment variables, and form submission.

---

## Features

- Opens **Speedtest.net** and runs a full speed test  
- Automatically extracts:
  - Download speed  
  - Upload speed  
- Logs into the **Y‑app** using credentials stored in a `.env` file  
- Auto‑fills and posts a complaint message  
- Uses Selenium waits for more stable automation  
- Closes the browser when finished  

---

## Technologies Used

- **Python 3**
- **Selenium WebDriver**
- **ChromeDriver**
- **dotenv** for environment variables
- **WebDriverWait** for stable element detection

---

## Project Structure

```
project-folder/
│
├── X_complaintBot.py      # Main automation script
├── .env                   # Stores login credentials (not committed)
└── README.md              # Project documentation
```

---

## Environment Variables

Create a `.env` file in the same folder as your script:

```
Y_EMAIL=your_email_here
Y_PASSWORD=your_password_here
```

These values are loaded using:

```python
from dotenv import load_dotenv
load_dotenv()
```

---

## How to Run

1. Install dependencies:

```bash
pip install selenium python-dotenv
```

2. Download ChromeDriver that matches your Chrome version.

3. Run the script:

```bash
python X_complaintBot.py
```

The bot will:

- Open Speedtest  
- Run the test  
- Log into the Y‑app  
- Post your complaint  
- Quit the browser  

---

## What I Learned

- How to target `<div>` and `<span>` elements using CSS selectors  
- How to wait for dynamic elements using `WebDriverWait`  
- How to automate login forms  
- How to safely store credentials using `.env`  
- How to simulate typing and clicking with Selenium  

---

## Notes

- Speedtest.net can be slow or unstable; using explicit waits is essential.  
- The Y‑app login button does not have an ID, so the form is submitted using `ENTER`.  
- This project is for educational purposes only — do not automate real social media logins without permission.

---

## Future Improvements

- Add error handling for network drops  
- Replace `time.sleep()` with full WebDriverWait logic  
- Add logging  
- Add retry logic for Speedtest failures  


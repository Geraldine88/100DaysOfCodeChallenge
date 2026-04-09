# Amazon Price Tracker Bot

## Overview  
This project is a **Python-based Amazon Price Tracker** built as part of **Day 47** of the *100 Days of Code – The Complete Python Pro Bootcamp*.  
The script checks the current price of a chosen Amazon product and sends an **email alert** when the price drops below a target threshold.

It uses:

- `requests` for fetching the product page  
- `BeautifulSoup` for parsing HTML  
- `smtplib` for sending email notifications  
- `.env` variables for secure credential storage  

This project demonstrates **web scraping**, **HTML parsing**, **environment variable management**, and **automated email alerts**.

---

## Project Structure

```
Day47/
│
├── amz_price_track_bot.py     # Main script that scrapes Amazon and sends alerts
├── .env                       # Environment variables (email + app password)
└── README.md                  # Project documentation
```

---

## Requirements

### **Python Libraries**
Install dependencies:

```bash
pip install requests beautifulsoup4 python-dotenv
```

### **Environment Variables (.env)**  
Your `.env` file should contain:

```
EMAIL_ADDRESS=your_email_here
APP_PASSWORD_PASSWORD=your_app_password_here
SMTP_ADDRESS=smtp.gmail.com
```

> ⚠️ *Never commit your `.env` file to GitHub.*

---

## How It Works

1. The script sends a GET request to the Amazon product page using realistic browser headers.  
2. BeautifulSoup parses the HTML and extracts:
   - Product title  
   - Current price  
3. If the price is **below your target threshold**, the script sends an email alert to your inbox.  
4. The script can be scheduled to run automatically (e.g., via Task Scheduler or cron).

---

## Email Alert Example

The email you receive includes:

- Product title  
- Current price  
- Direct link to the Amazon product page  

This allows you to quickly decide whether to buy the item.

---

## ⚠️ Notes on Amazon Scraping (Safe Use)

Amazon uses strong anti‑bot protections.  
To avoid being blocked:

- Use **minimal, realistic headers**  
- Scrape **infrequently** (e.g., once per day)  
- Track **only a few products**  
- Do **not** bypass CAPTCHAs or use proxies  
- Keep usage **personal and educational**  

This project is safe for learning and personal automation.

---

## Suggestions for Improvement

Here are some enhancements you can add as you grow the project:

### **1. Track Multiple Products**
Store product URLs in a list or JSON file and loop through them.

### **2. Log Price History**
Save timestamps + prices to a CSV for trend analysis.

### **3. HTML Email Formatting**
Send beautiful HTML emails with product images and styling.

### **4. Error Handling & Logging**
Gracefully handle:
- CAPTCHAs  
- Missing selectors  
- Network errors  

### **5. Scheduler Automation**
Run the script automatically using:
- Windows Task Scheduler  
- macOS launchd  
- Linux cron jobs  

### **6. GUI or Dashboard**
Build a small interface using:
- Tkinter  
- Flask  
- Streamlit  

### **7. Use Amazon’s Official API**
For long‑term, stable usage, migrate to the **Amazon Product Advertising API**.

---

## What I Learned

- How to send HTTP requests safely  
- How to parse dynamic HTML structures  
- How to extract specific elements from Amazon pages  
- How to send automated emails with Python  
- How to secure credentials using environment variables  
- How to structure a real-world automation script  


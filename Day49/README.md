# 🏋️‍♀️ **Snack & Lift Gym Automation Bot**  
### *Day 49 – Selenium Automation with Chaos Mode, Retry Logic & Resilient Booking System*

This project automates class booking on the **App Brewery Gym** website using **Selenium WebDriver**.  
It simulates a real‑world QA automation scenario where the system is unreliable, network failures occur, and the bot must retry actions intelligently.

This version includes:

- Automated login  
- Automated booking of **Tuesday & Thursday 6pm** classes  
- Automatic detection of booked / waitlisted / available classes  
- Verification on the **My Bookings** page  
- A **retry wrapper** that makes the bot resilient to failures  
- Compatibility with **Chaos Mode** (50% failure rate)  
- Compatibility with **Time Travel Testing** (admin date shifting)  

---

# 🚀 **Features**

### ✅ Automated Login  
The bot logs into the gym website using stored credentials and verifies successful login by detecting the **Class Schedule** page.

### ✅ Dynamic Class Booking  
The bot:

- Filters the schedule to “Next 7 Days”
- Scans all class cards dynamically
- Identifies **Tuesday** and **Thursday** classes
- Filters for **6:00 PM** sessions
- Books available classes
- Joins waitlists when booking is unavailable
- Tracks:
  - New bookings  
  - Waitlist joins  
  - Already booked classes  

### ✅ Resilient Retry Logic  
A custom `retry()` wrapper retries any function up to 7 times.

This protects against:

- Network failures  
- Random Selenium errors  
- Chaos Mode failures  
- Slow page loads  
- Element click failures  

### Retry logic example:

```
retry(login, description="Logging in")
retry(book_tue_thu_6pm_classes, description="Booking Tue/Thu 6pm classes")
retry(get_my_bookings, description="Verifying bookings")
```

### ✅ Verification System  
After booking, the bot navigates to **My Bookings** and verifies:

- Each Tue/Thu 6pm class appears  
- The number of verified bookings matches the expected count  

If not, it prints a mismatch summary.

### 🧪 Chaos Mode Support  
Using the **Admin Panel**, you can enable:

- Network Simulation  
- 50% failure rate  
- Time travel (advance days)  
- Clear all bookings  

The bot is designed to survive these conditions.

---

# 🧠 **How It Works (High-Level Architecture)**

### **1. retry(func)**  
A wrapper that retries any function multiple times until it succeeds or exhausts attempts.

### **2. login()**  
Navigates to the site, clicks Login, enters credentials, and waits for the schedule page.

### **3. book_tue_thu_6pm_classes()**  
Parses the DOM dynamically:

- Finds all class cards  
- Extracts day + time  
- Filters Tue/Thu 6pm  
- Books or waitlists  
- Tracks results  

### **4. get_my_bookings()**  
Navigates to My Bookings:

- Extracts all booking cards  
- Filters Tue/Thu 6pm  
- Counts verified bookings  

### **5. Final Comparison**  
Prints:

```
Expected: X
Verified: Y
```

And reports success or mismatch.

---

# 🛠️ **Technologies Used**

- Python  
- Selenium WebDriver  
- ChromeDriver  
- WebDriverWait & Expected Conditions  
- CSS Selectors & XPath  
- dotenv for credential management  
- Retry logic for resilience  
- Custom Chrome profile for persistent sessions  

---

# 📦 **Setup Instructions**

### 1. Install dependencies  
```
pip install selenium python-dotenv
```

### 2. Create a `.env` file  
```
ACCOUNT_EMAIL=your_email
ACCOUNT_PASSWORD=your_password
```

### 3. Run the script  
```
python snack_and_lift_gym.py
```

### Optional (for Chaos Mode Testing):

1. Log in as **Admin** manually  
2. Click **Clear All Bookings**  
3. Enable **Network Simulation**  
4. Set failure rate to **50%**  
5. Reset to **Real Time**  
6. Log out  
7. Run your bot again  

---

# 📊 **Example Output**

```
🔄 Attempt 1/7: Logging in
✅ Login successful!

📅 Booking Tue/Thu 6pm classes...
✓ Successfully booked: Spin Class on Tue, Apr 28
✓ Successfully booked: Spin Class on Thu, Apr 30

--- BOOKING SUMMARY ---
New bookings: 2
Waitlists: 0
Already booked: 0

📖 Retrieving My Bookings...
✓ Verified: Spin Class (Waitlist)

--- FINAL RESULT ---
Expected: 2
Verified: 1
❌ MISMATCH: Some bookings missing.
```

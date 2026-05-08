# **Day 48 – Cookie Clicker Automation Bot (Selenium + Python)**

This project is part of my **100 Days of Code – Python Pro Bootcamp**.  
The goal for Day 48 was to build a fully automated bot that plays the online game **Cookie Clicker** using **Selenium WebDriver**.

The bot must:

- Load the game  
- Automatically dismiss the language selection popup  
- Click the cookie as fast as possible  
- Every 5 seconds, check available upgrades  
- Buy the **most expensive affordable upgrade**  
- Run for **5 minutes**  
- Print the final **cookies per second (CPS)** score  

This project combines **web automation**, **DOM inspection**, **timing logic**, and **dynamic element handling**.

---

## ** Technologies Used**
- Python 3  
- Selenium WebDriver  
- ChromeDriver  
- WebDriverWait + Expected Conditions  
- Regular expressions for text parsing  

---

## ** Project Overview**

Cookie Clicker is a browser-based incremental game where clicking a giant cookie earns currency (“cookies”).  
You can spend cookies on upgrades that increase your production rate.

The challenge was to automate this gameplay loop.

### **Key Features of the Bot**
- Automatically dismisses the language popup using WebDriverWait  
- Clicks the cookie thousands of times per second  
- Parses cookie count safely using regex  
- Reads upgrade prices dynamically from the DOM  
- Buys the **most expensive** upgrade the bot can afford  
- Runs for exactly **5 minutes**  
- Prints the final **cookies per second**  

---

## ** Core Logic**

### **1. Clicking the Cookie**
The bot clicks the cookie continuously inside a loop.  
To simulate extremely fast clicking, multiple `.click()` calls are executed per iteration.

### **2. Checking Upgrades Every 5 Seconds**
A timer controls when the bot checks the store:

- Extract current cookies  
- Extract all upgrade prices  
- Clean and convert prices to integers  
- Build a dictionary of affordable upgrades  
- Buy the most expensive one  

### **3. Ending the Game**
After 5 minutes, the bot stops and prints the CPS value from the game interface.

---

## ** Final Code**
The full, optimized, and error‑handled script is included in `CookieClicker.py`.

It uses:

- `WebDriverWait` to handle slow-loading elements  
- `re.sub()` to safely extract numeric values  
- A high-speed clicking loop  
- A 5-minute timer  
- A 5-second upgrade check cycle  

---

## ** What I Learned**
- How to automate browser interactions with Selenium  
- How to inspect and extract dynamic values from a webpage  
- How to handle slow-loading elements using explicit waits  
- How to parse messy text using regex  
- How to design timed loops and automation strategies  
- How to optimize performance for high-frequency actions  

---

## ** Possible Improvements**
- Auto-click golden cookies  
- Buy upgrades (not just products)  
- Smarter strategy (e.g., prioritize certain items early game)  
- Logging CPS over time  
- GUI to start/stop the bot  

---

## **Final Output Example**
At the end of the 5-minute run, the bot prints something like:

```
Cookies per second: 12,345
```

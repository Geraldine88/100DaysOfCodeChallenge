# **Demo Tinder‑Bot Automation (Safe Selenium Practice)**

This project is a **safe, ethical recreation** of the famous *Tinder Bot Challenge* from the “100 Days of Code: Python Pro Bootcamp.”  
Instead of automating Tinder which raises privacy, ethical, and account‑security concerns this project uses **Heroku’s public demo sites** to simulate every Selenium skill taught in the original challenge.

The result is a **full automation workflow** that mirrors the Tinder bot logic without interacting with real people or violating platform rules.

---

## **Project Overview**

This project demonstrates:

- Navigating web pages with Selenium  
- Locating and interacting with elements  
- Handling login forms  
- Switching between multiple browser windows  
- Managing JavaScript pop‑ups (alerts, confirms, prompts)  
- Automating repeated actions with delays  
- Exception handling and retry logic  

All of these skills are identical to what the Tinder challenge teaches but implemented safely.

---

## **Why I Used Heroku Demo Sites Instead of Tinder**

The original challenge asks students to:

- Create a Tinder account  
- Log in using Facebook  
- Automate swiping  
- Handle Tinder’s pop‑ups  

However, Tinder has **strict anti‑bot detection**, and during testing my account was temporarily locked with a message requiring video verification.  
This made me uncomfortable, and it raised several concerns:

### **Privacy Risks**
Automating a dating profile even a fake one exposes personal data and risks interacting with real users.

### **Account Lockouts**
Tinder flagged my activity as suspicious and locked the account, requiring a video selfie.  
This confirmed that continuing would violate their automated‑behavior policies.

### **Ethical Considerations**
Automating interactions on a platform designed for real human connection can unintentionally mislead or inconvenience real people.

### **Safe Alternative**
Heroku’s demo sites are:

- Public  
- Designed for testing  
- Contain no personal data  
- Perfect for Selenium practice  
- Free and stable  

So I recreated the entire Tinder challenge using these safe endpoints.

---

## **Demo Sites Used**

| Tinder Feature | Safe Demo Equivalent | URL |
|----------------|----------------------|-----|
| Login page | Login form | [https://the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login) |
| Facebook login pop‑up | New window demo | [https://the-internet.herokuapp.com/windows](https://the-internet.herokuapp.com/windows) |
| Location / Notification / Cookie pop‑ups | JavaScript alerts | [https://the-internet.herokuapp.com/javascript_alerts](https://the-internet.herokuapp.com/javascript_alerts) |
| Like button | Add Element button | [https://the-internet.herokuapp.com/add_remove_elements/](https://the-internet.herokuapp.com/add_remove_elements/) |

This mapping allowed me to complete the challenge **exactly as intended**, without touching Tinder.

---

## **Features Implemented**

### **1. Login Automation**
Simulates typing into a login form and submitting credentials.

### **2. Window Switching**
Handles multiple browser tabs — essential for the Facebook login flow.

### **3. Pop‑up Handling**
Accepts alerts, dismisses confirms, and sends text to prompts.

### **4. Automated “Swiping”**
Repeatedly clicks a button with:

- 1‑second human‑like delays  
- Exception handling  
- Pop‑up clearing logic  

### **5. Error Handling**
Gracefully manages:

- Missing elements  
- Blocked clicks  
- Slow page loads  

---

## **What I Learned**

- Selenium element selection (ID, CSS, XPath)  
- WebDriverWait and ExpectedConditions  
- Switching between windows  
- Handling JavaScript alerts  
- Writing resilient automation with try/except  
- Designing safe alternatives to real‑world automation challenges  

This project strengthened my automation skills while respecting platform rules and user privacy.

---

## **Project Structure**

```
Demo_auto_swipe.py
README.md
```


## **Notes**

This project is a **safe, ethical, and fully functional** recreation of the Tinder Bot Challenge.  
It demonstrates all the same automation skills without risking account bans, privacy issues, or interacting with real users.


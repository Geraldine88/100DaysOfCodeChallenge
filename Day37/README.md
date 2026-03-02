# Pixela Coding Tracker

A small Python project that recreates the feel of GitHub’s contribution graph on a personal scale using the Pixela API. 
Each pixel represents your daily coding activity, i.e, number of commits done per day, giving you a simple visual record of consistency and growth.

### What the Project Does
- Creates a Pixela user and a coding‑activity graph  
- Records today’s total coding work as a single pixel  
- Updates or deletes previous entries when needed  
- Formats dates automatically in `yyyyMMdd`  
- Loads your Pixela username and token from a `.env` file instead of hard‑coding them  

### Why This Exists
GitHub’s commit graph is motivating, but it only tracks activity inside GitHub. 
This project recreates that same visual habit‑tracking idea using Pixela, letting me log coding sessions manually or through automation. 
It’s a lightweight, customizable version of the GitHub graph, perfect for personal tracking, small projects, or daily practice.

---

## How It Works
The script uses:
- **Python**
- **requests** for API communication  
- **datetime** and **timedelta** for date handling  
- **python-dotenv** to load environment variables  
- **Pixela’s REST API** for creating, updating, and deleting pixels  

Each action (post, update, delete) is a simple HTTP request. 
The `.env` file keeps your username and token private and out of your codebase.

---

## Project Setup

### 1. Create a `.env` file in the project folder
```
PIXEL_USERNAME=your_username
PIXEL_TOKEN=your_token
```

### 2. Run the script
The script will:
- Read your username and token from `.env`
- Post, update, or delete a pixel depending on the section you run
- Display Pixela’s response in the console

---

## Viewing Your Graph
Open your graph in the browser:

```
https://pixe.la/v1/users/<your-username>/graphs/<graph-id>.html
```

This shows your personal “commit graph” growing day by day.
The more 'commits' done, the greater the color intensity of the pixel.

---

## Possible Improvements
- Add a command‑line menu for posting, updating, or deleting pixels  
- Automate daily posting with Task Scheduler or cron  
- Track multiple habits with multiple graphs  
- Add logging for clearer feedback  
- Store graph IDs in `.env` as well  
- Wrap API calls into reusable functions or a small class  


# **Web Scraping with BeautifulSoup — README**

## **Overview**
This project introduced me to the fundamentals of web scraping using Python, the `requests` library, and BeautifulSoup. I learned how to retrieve webpage content, parse HTML, and extract specific information from structured and unstructured pages. As a final exercise, I built a script that scrapes the top 100 movies from an archived website and writes them into a text file in a clean, numbered format.

---

## **What I Learned**

### ** What Web Scraping Is**
I learned that web scraping is the process of programmatically retrieving and extracting data from websites. BeautifulSoup helps transform raw HTML into a structured format that is easier to navigate and search.

### ** What Types of Files BeautifulSoup Can Parse**
BeautifulSoup is designed to parse:
- HTML  
- XML  
- Any markup‑based text  

It cannot parse PDFs, images, or JavaScript-rendered content without additional tools.

### ** Core BeautifulSoup Features**
I practiced using the most common and powerful methods, including:

- **`.get()`** — retrieving webpage content using the `requests` library  
- **`.getText()`** — extracting only the text inside an element  
- **`.find()`** — locating the first matching tag  
- **`.find_all()`** — locating all matching tags  
- **`.select_one()`** — selecting a single element using a CSS selector  
- **`.select()`** — selecting multiple elements using CSS selectors  

These tools allowed me to target specific HTML elements and extract exactly the data I needed.

### ** How to Locate and Select Elements**
I learned how to inspect a webpage’s structure and identify:
- Tags (`h1`, `p`, `a`, etc.)  
- Classes  
- IDs  
- Attributes  
- Nested elements  

Using CSS selectors made it easy to target elements precisely, especially when pages had complex or deeply nested HTML.

---

## ** ⚖️ Legal Considerations of Web Scraping**
I also learned that scraping is not always allowed. The legality depends on:

### **1. The Website’s Terms of Service**
Some sites explicitly forbid scraping.  
To check this, look for:
- A **Terms of Service** link  
- A **robots.txt** file (e.g., `example.com/robots.txt`)  

If the site blocks bots or automated access, scraping may violate their rules.

### **2. Whether the Data Is Public**
Publicly accessible data is generally safer to scrape, but still subject to the site’s policies.

### **3. The Purpose of Scraping**
Scraping for:
- personal learning  
- research  
- non‑commercial use  

is usually safer than scraping for commercial or competitive purposes.

### **4. Server Load and Ethical Use**
Even when scraping is allowed, it’s important to:
- avoid sending too many requests  
- respect rate limits  
- avoid harming the website’s performance  

In this project, we used the **Internet Archive’s Wayback Machine**, which is specifically provided for public access and educational use — making it a safe and appropriate source.

---

## ** Final Project: Top 100 Movies Scraper**
To apply everything I learned, I built a script that:

- Loads a URL from a `.env` file  
- Fetches the archived webpage using `requests`  
- Parses the HTML with BeautifulSoup  
- Locates the movie titles using tag searches or CSS selectors  
- Reverses the list (because the site lists movies from 100 → 1)  
- Writes the final ordered list into a `movies.txt` file  

This project helped me combine environment variables, HTTP requests, HTML parsing, and file handling into one complete workflow.

---

## **Skills Practiced**
- Web scraping fundamentals  
- HTML structure analysis  
- CSS selector targeting  
- Data extraction and cleaning  
- Environment variable usage  
- Writing data to external files  
- Understanding ethical and legal scraping practices  


import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
load_dotenv()

url = os.getenv("URL")

# Write your code below this line 👇

# TODO: 1 - Create a text file with the top 100 movies starting from 1
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

movies = soup.find_all("h3", class_="title")

titles = [tag.getText() for tag in movies]
titles = titles[::-1]

with open('movies.txt', 'w', encoding="utf-8") as f:
    for i, title in enumerate(titles, start=1):
        f.write(f"{title}\n")



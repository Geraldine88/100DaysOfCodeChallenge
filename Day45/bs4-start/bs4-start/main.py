# from bs4 import BeautifulSoup
# import lxml
#
# with open("website.html") as f:
#     contents = f.read()
#
#
# # Make soup
# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title.string)

"""
    USING BEAUTIFUL SOUP TO GET HOLD OF A LIVE WEBSITE AND GRAB DATA FROM IT
"""
from bs4 import BeautifulSoup
import requests

url = "https://appbrewery.github.io/news.ycombinator.com/"
response = requests.get(url)

#print(response.text)

# TODO: Getting the article from the url with the highest point
# NB: Don't manually check all post

yc_webPage = response.text

# Creating Beautiful soup object
soup = BeautifulSoup(yc_webPage, "html.parser")

# Now, dig in the soup and find the parts we want
print(soup.title)

# Printing out the title of first article
# Hint: name of attribute, class name of the attribute
# article_text = soup.find(selectors = "a", name = "title")

"""
<a class="storylink" href="https://www.aps.org/archives/publications/apsnews/202008/feynman.cfm">
    Joan Feynman 1927-2020   
</a>
"""

article_tag = soup.find(name="a", class_="storylink")
print(f'\n--> Article Tag:\n{article_tag}')

article_text = article_tag.getText()
print(f'\n--> Article Text:\n{article_text}')

# TODO: Get the article link
article_link = article_tag.get("href")
print(f'\n--> Article Link:\n{article_link}')


# TODO: Get the article's score (upvote)
article_upvote = soup.find(name="span", class_="score").getText()
print(f'\n--> Article Upvote:\n{article_upvote}')

# TODO: Get all the articles' properties

print(f"\n #----------------------------------------------------- Doing same for all the posts available --------------------------------------------------------------------------------------#\n"
      f"::::::::::::::")
article_tags = soup.find_all(name="a", class_="storylink")
print(f'\n--> Article Tags:\n{article_tags}')

article_texts = []
article_links = []
for article_tag in article_tags:
    texts = article_tag.getText()
    links = article_tag.get("href")

    article_texts.append(texts)
    article_links.append(links)

# TODO: Get the article's score (upvote)
article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]

print(f'\n--> Article Texts:\n{article_texts}')
print(f'\n--> Article Links:\n{article_links}')
print(f'\n--> Article Upvotes:\n{article_upvotes}')

# TODO: Getting the article votes into a number format (Get rid of 'points' string)
import re

votes = []
for v in article_upvotes:
    matches = re.match(r'(\d+)', v)
    if matches:
        votes.append(int(matches.group(1)))

print(f"\n--> Votes:\n{votes}")

"""
Alternatively, 

article_upvotes_ = [
        int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")
]

print(f'\n--> Article Upvotes:\n{article_upvotes_}')
"""

# TODO: From the article with the highest vote, pick out the title and link
# Hint: Use index of largest number

max_upvote = [(i, v) for i, v in enumerate(votes) if v == max(votes)]
print(f'\n --> Index and Value of largest upvote: {max_upvote}')

# Index of max votes
idx_max_upvote = [i for i, v in enumerate(votes) if v == max(votes)]
print(f'\n --> Index of largest upvote: {idx_max_upvote}')

top_idx = idx_max_upvote[0]

# Access specific tag using the index
max_tag_text = article_tags[top_idx].getText()
max_tag_link = article_tags[top_idx].get("href")

print(f'\n--> Article Text from Most Popular Post:\n{max_tag_text}')
print(f'\n --> Article Link from Most Popular Post:\n{max_tag_link}')

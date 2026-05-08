##############################################################################################
#                                          IMPORTS & SETUP
##############################################################################################
import requests
import os
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()


##############################################################################################
#                                       CONSTANTS & ENV VARS
##############################################################################################
instant_pot_url = "https://appbrewery.github.io/instant_pot/"
real_tablet_url = "https://www.amazon.com/dp/B0FJ1XKNHV"

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("APP_PASSWORD_PASSWORD")
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")


##############################################################################################
#                                       REQUEST HEADERS
##############################################################################################
# 3. TODO: Adding this header to request to make is less-bot in its response
"""
    {
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
    "Accept-Encoding": "gzip, deflate, br, zstd", 
    "Accept-Language": "en-US,en;q=0.9", 
    "Host": "httpbin.org", 
    "Priority": "u=0, i", 
    "Sec-Fetch-Dest": "document", 
    "Sec-Fetch-Mode": "navigate", 
    "Sec-Fetch-Site": "cross-site", 
    "Sec-Fetch-User": "?1", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:149.0) Gecko/20100101 Firefox/149.0"
  }
}
"""

# Minimal realistic headers for Amazon
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}


##############################################################################################
#                                   FETCH & PARSE HTML
##############################################################################################
response = requests.get(real_tablet_url, headers=headers)

# Beautiful soup object with new header
soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify()[:2000])  # Debug


##############################################################################################
#                                       PRICE EXTRACTION
##############################################################################################
"""
    It's under an HTML tag <span class="a-price aok-align-center" data-a-color="base" data-a-size="xl">
                           <span class="a-offscreen">
                            $99.99
                           </span>'<span aria-hidden="true"></span>'
"""

# Amazon changes structure often, so try multiple selectors
price_selectors = [
    "span.a-offscreen",
    "span.a-price-whole",
    "span.apexPriceToPay span.a-offscreen",
    "span.a-price > span.a-offscreen",
]

price_tag = None
for selector in price_selectors:
    price_tag = soup.select_one(selector)
    if price_tag:
        break

if price_tag is None:
    print("Price element not found. Check headers or page structure.")
    print(soup.prettify()[:5000])
    exit()

price_text = price_tag.get_text().strip()
price = float(price_text.replace("$", "").replace(",", ""))


##############################################################################################
#                                       TITLE EXTRACTION
##############################################################################################
"""
     In the email, include the title of the product, the current price and a link to buy the product.
"""
title_tag = soup.find(id='productTitle')

if title_tag is None:
    print("Title element not found.")
    print(soup.prettify()[:5000])
    exit()

title = title_tag.get_text().strip()


##############################################################################################
#                                       PRICE CHECK & EMAIL ALERT
##############################################################################################
# I'm gonna set target price to 100 for testing
target_price = 200

if price < target_price:
    # Send an email alerting the user
    msg = f"{title} is on sale at ${price}\n\nBuy here:\n{real_tablet_url}"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject: Amazon Price Alert!\n\n{msg}".encode("utf-8")
        )

    print("Email sent!")
else:
    print(f"No alert. Current price is ${price}.")
# ####################################################################################################
# #                                       IMPORTS
# ####################################################################################################
"""
    Win the Cookie Cliker Game.
    Run program for 5 minutes  then check how many cookies per second you have.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait

from Day48.CookieClicker import five_sec_timer

options = Options()
options.add_argument("--log-level=3")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Inputting the cookieclicker link
driver.get("https://ozh.github.io/cookieclicker/")

# TODO: 2. Create a bot using Selenium and Python to click on the cookie as fast as possible.
"""
    TODO: 2. Create a bot using Selenium and Python to click on the cookie as fast as possible.
    Note that you will need to find a way to automatically dismiss the language selection
    before you can get started.
"""

# DISMISS LANGUAGE SELECTION
# eng_selection = driver.find_element(By.CSS_SELECTOR, value="div#langSelect-EN.langSelectButton.title")
# eng_selection.click()

wait = WebDriverWait(driver, 10)
eng_selection = wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
eng_selection.click()


"""
   TODO: 3. Every 5 seconds, check the right-hand pane to see which upgrades are affordable and
   purchase the most expensive one. You'll need to check how much money (cookies) you have against
   the price of each upgrade.

    e.g. both Grandma and Cursor are affordable as we have 105 cookies, but Grandma is the more
    expensive one, so we'll purchase that instead of the cursor.
"""

# timeout = time.time() + (60*5)
# while True:

#prod_to_buy = int(driver.find_elements(By.CSS_SELECTOR, value="span.price"))
prices = driver.find_elements(By.CSS_SELECTOR, "span.price")
products = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")

current_cookies = driver.find_elements(By.ID, value="cookies").text.split("\n")[0]
cookies = int(current_cookies.replace(",", ""))

affordables = {}

# Every 5 seconds, check upgrades
if time.time() > five_sec_timer:

    # Get cookies safely
    cookies_text = driver.find_element(By.ID, "cookies").text
    cookies = int(re.sub(r"\D", "", cookies_text))

    # Get store items
    prices = driver.find_elements(By.CSS_SELECTOR, "span.price")
    products = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")

    affordables = {}

    # Loop through all store items
    for i in range(len(prices)):
        price_text = re.sub(r"\D", "", prices[i].text)
        if price_text.isdigit():
            price = int(price_text)
            if cookies >= price:
                affordables[price] = products[i]

    # Buy the most expensive affordable item
    if affordables:
        max_price = max(affordables.keys())
        affordables[max_price].click()

    # Reset timer
    five_sec_timer = time.time() + 5


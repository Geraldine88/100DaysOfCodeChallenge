####################################################################################################
#                                       IMPORTS
####################################################################################################
"""
    Interact with the wikipedia webpage.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--log-level=3")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Inputting the wikipedia link
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# ####################################################################################################
# #                                       CHALLENGE
# ####################################################################################################
# # 1. TODO: Get a hold of "Number of articles in English" and print it out INSIDE interaction.py
# # num_english_articles = driver.find_element(By.CSS_SELECTOR, value='a[href="/wiki/Special:Statistics"]')
# # print(num_english_articles.text)
#
# num_eng_articles = driver.find_elements(By.CSS_SELECTOR, value="#articlecount a")[1]
# print(num_eng_articles.text.strip())
#
# ####################################################################################################
# #                                       INTERACTING WITH ELEMENTS WITH SELENIUN
# ####################################################################################################
#
# """ Clicking on the element """
# # num_eng_articles.click()
#
# """ Using Link Text """
# teaHouse = driver.find_element(By. LINK_TEXT, value="Teahouse")
# print(teaHouse.text)
# teaHouse.click()

""" Typing """

# # Typing in the search bar
# search_box = driver.find_element(By.ID, "searchInput")
#
# search_box.send_keys("Python") # Sending whatever to the element we're targetting


####################### CHALLENGE
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")

last_name = driver.find_element(By.NAME, value="lName")

email = driver.find_element(By. NAME, value="email")

# Fill in the form
first_name.send_keys("Ginger")
last_name.send_keys("The Coder")
email.send_keys("gingerme26coder@gmail.com")

#submit_button = driver.find_element(By.CSS_SELECTOR, value="btn btn-lg btn-primary btn-block")
submit_button = driver.find_element(By.CSS_SELECTOR, value="form button")
submit_button.click()
# submit_button.send_keys(Keys.ENTER)

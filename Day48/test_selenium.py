# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# # Getting the driver to open up a web page
# driver.get("https://www.amazon.com")
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#Specifying HTML class name we're interested in finding
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--log-level=3")  # suppress warnings and info logs

"""
    To keep the Chrome browser open after the program runs, use chrome options
"""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/dp/B0FJ1XKNHV")
#
#
# # PRICE hold on to the price element on the amazon page
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#
# print(f"The price is {price_dollar.text}.{price_cents.text}")
#
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
#
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
#
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)


####################################################################################################
#                                       CHALLENGE
####################################################################################################

driver.get("https://www.python.org/events/")

upcoming_events = {}

event_title = driver.find_elements(By.CLASS_NAME, value="event-title")
time = driver.find_elements(By.TAG_NAME, value="time")

num_events = len(event_title)
# for i in range(num_events):
#     upcoming_events[event_title[i].text] = time[i].text
for events in range(num_events):
    upcoming_events[events] = {
        "Event" : event_title[events].text,
        "Time" : time[events].text,
    }

print(upcoming_events)



"""
    To close the tab and quit Chrome programmatically, user driver.close
"""

# driver.close() # Closes the single active tab, not the browser
#
driver.quit() # Stops the entire browser
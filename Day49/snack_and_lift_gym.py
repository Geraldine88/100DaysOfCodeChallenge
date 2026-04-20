"""
    STEP 1: 🚀 Let's Get Started! Initial Setup - Getting Your Gym Membership 💪
"""
from platformdirs import user_data_dir
####################################################################################################
#                                       IMPORTS
####################################################################################################
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os
load_dotenv()

####################################################################################################
#                                       CREDENTIALS
####################################################################################################
ACCOUNT_USER_NAME = os.getenv("ACCOUNT_USER_NAME")
ACCOUNT_EMAIL = os.getenv('ACCOUNT_EMAIL')
ACCOUNT_PASSWORD = os.getenv('ACCOUNT_PASSWORD')
# 4. TODO: Run Selenium and have it navigate to the gym website:
GYM_URL = "https://appbrewery.github.io/gym/"
####################################################################################################
#                                           TASKS
####################################################################################################

# 1. TODO: Configure Selenium to stay open using the Chrome option:
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# 2. TODO: Give Selenium it's own user profile.
"""
Have your script create a directory in your project folder to store your 
Chrome Profile information with:
"""
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

# 3. TODO: Tell your Chrome Driver to use the directory you specified to store a "profile".
"""
That way every time you quit Chrome and re-run your Selenium script, it keeps all the preferences
 and settings from your profile.
"""
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)

# 5. TODO: Create your account manually in the browser that Selenium opens
driver.get(GYM_URL)

# The site needs to wait before clicking the submit button
wait = WebDriverWait(driver, 10)
# ****************************************************************************************************

"""
    STEP 2: 🔐 Automated Login - No More Manual Sign-ins!
"""

# Write code to:

# 1. TODO: Click the login button
login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#login-button.Navigation_button__uyKX2")))
login.click()

# 2. TODO: Fill in your email and password
"""Pro tip 2: Use presence_of_element_located to verify that an element is present on the page."""
email = wait.until(EC.presence_of_element_located((By.ID, "email-input")))
password = driver.find_element(By.ID, "password-input")

login_submit = wait.until(EC.element_to_be_clickable((By.ID,"submit-button")))

# Filling in the form with credentials
email.send_keys(ACCOUNT_EMAIL)
password.send_keys(ACCOUNT_PASSWORD)

# 3. TODO: Submit the form

login_submit.click()
print("After submit, current URL:", driver.current_url)


# 4. TODO: Verify you're logged in by checking for the "Class Schedule" page
# print(GYM_URL)
# driver.get(GYM_URL)
wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Class Schedule')]")))
print("Login successful!")
# ****************************************************************************************************

"""
    Book Your First Class - Tuesday at 6pm 📅
"""

"""
Hints:

The default filter shows "Next 7 Days" - perfect!

Parse the day and time from each class card

Look for patterns in the HTML structure

Right click to inspect various elements in the class table. 
Do you see a pattern in the naming of IDs?
"""

# 1. TODO: Find the next Tuesday 6pm class (any type - Yoga, Spin, or HIIT)

def book_next_tuesday_6pm(driver):
    wait = WebDriverWait(driver, 10)

    # Make sure the filter is set to "Next 7 Days"
    select = Select(driver.find_element(By.ID, "day-filter"))
    select.select_by_value("week")

    # Get all class cards
    class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

    for card in class_cards:

        # Go up to the parent day group
        day_group = card.find_element(
            By.XPATH,
            "./ancestor::div[contains(@id, 'day-group-')]"
        )
        day_title = day_group.find_element(By.TAG_NAME, "h2").text

        # Check if this is a Tuesday
        if "Tue" not in day_title:
            continue

        # Check if this is a 6:00 PM class
        time_text = card.find_element(
            By.CSS_SELECTOR,
            "p[id^='class-time-']"
        ).text

        if "6:00 PM" not in time_text:
            continue

        # Get the class name
        class_name = card.find_element(
            By.CSS_SELECTOR,
            "h3[id^='class-name-']"
        ).text

        # Book the class
        button = card.find_element(
            By.CSS_SELECTOR,
            "button[id^='book-button-']"
        )
        button.click()

        print(f"✓ Booked: {class_name} on {day_title} at {time_text} 🎉")
        return

    print("No Tuesday 6pm class found.")

#print("Login successful!")

# Call your booking function
book_next_tuesday_6pm(driver)

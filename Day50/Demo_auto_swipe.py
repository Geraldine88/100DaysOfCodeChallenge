################################################################################################
# IMPORTS
################################################################################################
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Keep chrome browser open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

################################################################################################
# STEP 1 — LOGIN PAGE PRACTICE
################################################################################################
driver.get("https://the-internet.herokuapp.com/login")

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
login_btn = driver.find_element(By.CSS_SELECTOR, "button.radius")

username.send_keys("Ginger")
password.send_keys("The swagger")
# login_btn.click()   # optional

################################################################################################
# STEP 2 — WINDOW SWITCHING DEMO
################################################################################################
driver.get("https://the-internet.herokuapp.com/windows")

click_here = driver.find_element(By.LINK_TEXT, "Click Here")
click_here.click()

base_window = driver.window_handles[0]
new_window = driver.window_handles[1]

driver.switch_to.window(new_window)
print("New window title:", driver.title)

driver.switch_to.window(base_window)
print("Back to base window:", driver.title)

################################################################################################
# STEP 3 — SIMULATE FACEBOOK LOGIN FLOW
################################################################################################
# Open window-switching page again
driver.get("https://the-internet.herokuapp.com/windows")

click_here = driver.find_element(By.LINK_TEXT, "Click Here")
click_here.click()

base_window = driver.window_handles[0]
new_window = driver.window_handles[1]

driver.switch_to.window(new_window)
print("New window title:", driver.title)

# Load login form inside the new window
driver.get("https://the-internet.herokuapp.com/login")

email = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

email.send_keys("fake_email@example.com")
password.send_keys("fake_password")

login_btn = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_btn.click()

driver.switch_to.window(base_window)
print("Back to base window:", driver.title)

################################################################################################
# STEP 4 — INSTRUCTIONS
################################################################################################

# Navigate to the pop up demo account
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

#2 Handle location permission popup alerts
alert_btn = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
alert_btn.click()

alert = driver.switch_to.alert
alert.accept()
print("Location pop-up accepted")

# Handle notification popup
confirm_btn = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
confirm_btn.click()

confirm = driver.switch_to.alert
confirm.dismiss()
print("Notification pop-up dismissed")

# Handle cookies popup
prompt_btn = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
prompt_btn.click()

prompt = driver.switch_to.alert
prompt.send_keys("Accept Cookies")
prompt.accept()
print("Cookies pop-up handled")

################################################################################################
# STEP 5 — HIT LIKE - DEMO SWIPE SIMULATION
################################################################################################

# 1. Navigate to the demo “swipe” page
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")


# 3. Create a loop to click it repeatedly
for n in range(10):
    try:
        # 2. Locate the “Like” button
        like_btn = driver.find_element(By.XPATH, "//button[text()='Add Element']")
        like_btn.click()
        print(f"Liked {n+1}")

        # 4. Add a 1‑second delay between likes
        time.sleep(1)
        # simulate a pop-up by clicking the delete button
        try:
            delete_btn = driver.find_element(By.CLASS_NAME, "added-manually")
            delete_btn.click()
            print("Pop-up cleared")
        except:
            pass

    except Exception as e:
        print(f"Error during like #{n + 1}: {e}")
        print("Waiting 2 seconds before retrying...")
        time.sleep(2)
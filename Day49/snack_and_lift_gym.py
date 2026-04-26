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
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import time
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

# The site needs to wait before clicking the submit button
wait = WebDriverWait(driver, 10)
# ****************************************************************************************************

####################################################################################################
#                                       RETRY WRAPPER
####################################################################################################
def retry(func, retries=7, description=""):
    for attempt in range(1, retries+1):
        try:
            print(f"\n🔄 Attempt {attempt}/{retries}: {description}")
            return func()
        except Exception as e:
            print(f"⚠️ Failed attempt {attempt}: {e}")
            if attempt == retries:
                print("❌ All retries failed.")
                raise
            time.sleep(1)

####################################################################################################
#                                       LOGIN FUNCTION
####################################################################################################
"""
    STEP 2: 🔐 Automated Login - No More Manual Sign-ins!
"""
def login():
    driver.get(GYM_URL)

    # 1. TODO: Click the login button
    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#login-button.Navigation_button__uyKX2")))
    login_btn.click()

    # 2. TODO: Fill in your email and password
    email_input = wait.until(EC.presence_of_element_located((By.ID, "email-input")))
    password_input = driver.find_element(By.ID, "password-input")

    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)

    # 3. TODO: Submit the form
    submit_btn = wait.until(EC.element_to_be_clickable((By.ID, "submit-button")))
    submit_btn.click()

    # 4. TODO: Verify you're logged in by checking for the "Class Schedule" page
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Class Schedule')]")))
    print("✅ Login successful!")

####################################################################################################
#                                       BOOKING FUNCTION
####################################################################################################
"""
    Book Your First Class - Tuesday at 6pm 📅
"""
def book_tue_thu_6pm_classes():
    wait = WebDriverWait(driver, 10)

    # Counters
    new_bookings = 0
    waitlists_joined = 0
    already_booked = 0
    total_target_classes = 0

    # Detailed list for summary
    details = []

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

        # Only Tuesday or Thursday
        if not ("Tue" in day_title or "Thu" in day_title):
            continue

        # Only 6:00 PM classes
        time_text = card.find_element(
            By.CSS_SELECTOR,
            "p[id^='class-time-']"
        ).text

        if "6:00 PM" not in time_text:
            continue

        total_target_classes += 1

        # Class name
        class_name = card.find_element(
            By.CSS_SELECTOR,
            "h3[id^='class-name-']"
        ).text

        # Check if already booked/waitlisted
        try:
            card.find_element(By.CSS_SELECTOR, "button[disabled]")
            already_booked += 1
            details.append(f"[Already Booked] {class_name} on {day_title}")
            print(f"Already booked/waitlisted: {class_name} on {day_title}")
            continue
        except:
            pass

        # Try booking
        try:
            book_button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            book_button.click()
            new_bookings += 1
            details.append(f"[New Booking] {class_name} on {day_title}")
            print(f"✓ Successfully booked: {class_name} on {day_title}")
            continue

        except:
            # Try waitlist
            try:
                waitlist_button = card.find_element(By.CSS_SELECTOR, "button[id^='waitlist-button-']")
                waitlist_button.click()
                waitlists_joined += 1
                details.append(f"[New Waitlist] {class_name} on {day_title}")
                print(f"✓ Joined waitlist for: {class_name} on {day_title}")
                continue
            except:
                print(f"Unexpected: No valid button found for {class_name} on {day_title}")
                continue

    # Summary
    print("\n--- BOOKING SUMMARY ---")
    print(f"New bookings: {new_bookings}")
    print(f"New waitlist entries: {waitlists_joined}")
    print(f"Already booked/waitlisted: {already_booked}")
    print(f"Total Tuesday & Thursday 6pm classes: {total_target_classes}")

    print("\n--- DETAILED CLASS LIST ---")
    for item in details:
        print(f"  • {item}")

    return new_bookings + waitlists_joined + already_booked, details

####################################################################################################
#                                       GET BOOKINGS FUNCTION
####################################################################################################
"""
    Step 7: Verify Class bookings on the "My Bookings" Page
"""
def get_my_bookings():
    print("\n ----- VERIFYING MY BOOKINGS PAGE ----")

    my_bookings_link = driver.find_element(By.ID, "my-bookings-link")
    my_bookings_link.click()

    wait.until(EC.presence_of_element_located((By.ID, "my-bookings-page")))

    verified = 0

    all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

    for c in all_cards:
        try:
            when_parag = c.find_element(By.XPATH, ".//p[strong[text()='When:']]")
            when_text = when_parag.text

            if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
                class_name = c.find_element(By.TAG_NAME, "h3").text
                print(f" ✓ Verified: {class_name}")
                verified += 1

        except:
            pass

    return verified

####################################################################################################
#                                       RUN SCRIPT WITH RETRIES
####################################################################################################
retry(login, description="Logging in")

expected_total, details = retry(book_tue_thu_6pm_classes, description="Booking Tue/Thu 6pm classes")

verified_total = retry(get_my_bookings, description="Verifying bookings")

print("\n--- FINAL RESULT ---")
print(f"Expected: {expected_total}")
print(f"Verified: {verified_total}")

if expected_total == verified_total:
    print("🎉 SUCCESS: All bookings verified!")
else:
    print("❌ MISMATCH: Some bookings missing.")

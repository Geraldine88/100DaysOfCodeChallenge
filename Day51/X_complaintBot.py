from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv
load_dotenv()

# print("EMAIL:", os.getenv("Y_EMAIL"))
# print("PASSWORD:", os.getenv("Y_PASSWORD"))


options = Options()
options.add_argument('--log-level=3')


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        # Getting the current internet speeds for uploads and downloads @ UWT
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)

        # Close cookie popup
        try:
            consent = self.driver.find_element(By.ID, 'onetrust-accept-btn-handler')
            consent.click()
            time.sleep(1)
        except:
            pass

        go_btn = self.driver.find_element(By.CSS_SELECTOR, '.start-button a')
        go_btn.click()

        wait = WebDriverWait(self.driver, 120)

        download = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.result-item-download span.result-data-value")
            )
        )

        upload = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.result-item-upload span.result-data-value")
            )
        )
        self.down = download.text
        """
            Download Speed at UWT: 198.59
            Upload Speed at UWT: 72.79
        """
        print(f"Download Speed: {self.down}")
        self.up = upload.text
        print(f"Upload Speed at UWT: {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://app.100daysofpython.dev/services/y/login")
        time.sleep(2)

        email = os.getenv("Y_EMAIL")
        password = os.getenv("Y_PASSWORD")

        # Fill email
        email_el = self.driver.find_element(By.ID, "email")
        email_el.send_keys(email)

        # Fill password
        password_el = self.driver.find_element(By.ID, "password")
        password_el.send_keys(password)
        password_el.send_keys(Keys.ENTER)
        time.sleep(3)

        # # Wait for login button to be clickable
        # wait = WebDriverWait(self.driver, 10)
        # login_btn = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        # login_btn.click()

        # Type complaint
        complaint_box = self.driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Post text"]')
        complain_txt = (
            f"I'd like to place a complaint, please. "
            f"My current download speed is {self.down} and upload speed is {self.up} "
            f"when I pay for 300 download and 5 upload."
        )
        complaint_box.send_keys(complain_txt)

        time.sleep(2)

        y_btn = self.driver.find_element(By.CSS_SELECTOR, value='.x-compose-form button')
        y_btn.click()

        time.sleep(3)
        self.driver.quit()




bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

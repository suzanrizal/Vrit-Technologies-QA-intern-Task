import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Yopmail:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def open_inbox(self, email):
        # Open YOPmail in a new browser tab
        self.driver.switch_to.new_window("tab")
        self.driver.get("https://yopmail.com/en/")

        # Enter the mailbox name (without @yopmail.com)
        inbox_name = email.split("@")[0]

        email_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, "login"))
        )
        email_input.clear()
        email_input.send_keys(inbox_name)

        # Open the inbox
        self.driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        ).click()

    def get_otp(self):
        # Switch into the inbox iframe
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.ID, "ifinbox")
            )
        )

        # Wait for at least one email to appear
        email = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.lm")
            )
        )
        email.click()

        # Return to the main document to inspect message frames
        self.driver.switch_to.default_content()

        # Wait for the email content frame and read its text
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.ID, "ifmail")
            )
        )

        message_text = self.wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, "body"))
        ).text

        # Extract a 4–8 digit OTP
        match = re.search(r"\b(\d{4,8})\b", message_text)

        if not match:
            raise AssertionError("OTP was not found in the email")

        return match.group(1)

from selenium import webdriver 
import time
import pytest
from PageObjects.SignupAutomation import Signup

class TestSignUp():
    @pytest.fixture(autouse=True)
    def setup(self, driver: webdriver.Chrome):
        self.driver = driver
        driver.get("https://authorized-partner.vercel.app/")
        time.sleep(2)

    def test_signup_Automation(self, driver):
        self.signupobj= Signup(self.driver)
        self.signupobj.click_login()
        time.sleep(2)
        self.signupobj.click_signup()
        time.sleep(2)
        self.signupobj.click_checkbox()
        time.sleep(2)
        self.signupobj.click_continue_button()
        time.sleep(2)

        # Actions on 1. setup your account
        self.signupobj.set_first_name("Sujan")
        self.signupobj.set_last_name("Rial")
        self.signupobj.set_email_address("tester@yopmail.com")
        self.signupobj.set_phone_number("9840308352")
        self.signupobj.set_password("Tester@123")
        self.signupobj.set_confirm_password("Tester@123")
        time.sleep(2)




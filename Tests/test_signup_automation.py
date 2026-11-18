from selenium import webdriver 
import time
import pytest
from PageObjects.SignupAutomation import Signup

# For Keyboard Actions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

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
        time.sleep(2)
        self.signupobj.set_last_name("Rijal")
        self.signupobj.set_email_address("interntask108@yopmail.com")
        self.signupobj.set_phone_number("9840308709")
        self.signupobj.set_password("Tester@123")
        self.signupobj.set_confirm_password("Tester@123")
        time.sleep(2)
        self.signupobj.scroll_page()
        self.signupobj.click_next()
        time.sleep(20)

        # Action on 2. Agency Detail
        self.signupobj.set_agency_name("Vrit Technologies")
        time.sleep(1)
        self.signupobj.set_role_in_agency("Quality Assurance")
        time.sleep(1)
        self.signupobj.set_agency_email("rizalsuzan3@gmail.com")
        time.sleep(1)
        self.signupobj.set_agency_website("www.vrittechnologies.com")
        time.sleep(1)
        self.signupobj.set_agency_address("Sankhamul")
        time.sleep(1)
        self.signupobj.click_region_of_operation()
        time.sleep(1)
        self.signupobj.scroll_page()
        time.sleep(1)
        self.signupobj.search_region("nepal")
        time.sleep(1)
        self.signupobj.click_search_result()
        time.sleep(1)
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(1)
        self.signupobj.click_next2()
        time.sleep(5)

        # Actions on 3. Professional Experience
        # ActionChains(self.driver).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()  # Keyboarrd actions with actionchain
        # time.sleep(2)
        self.signupobj.click_experience_menu()
        time.sleep(2)
        self.signupobj.choose_years_of_exp()
        time.sleep(2)
        self.signupobj.set_number_of_students_recruited("20")
        time.sleep(2)
        self.signupobj.set_focus_area("Selenium Webdriver")
        time.sleep(2)
        self.signupobj.set_sucess_matrix("99")
        self.signupobj.click_Service_provided()
        time.sleep(2)

        










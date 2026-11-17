from selenium import webdriver
from selenium.webdriver.common.by import By


class Signup(): 
    def __init__(self, driver: webdriver.chrome):  # Initializing driver
        self.driver = driver

        # Saving Locator
        self.login_button_XPATH = (By.XPATH, "//a[@class='px-4 flex items-center gap-2']")
        self.signup_button_XPATH = (By.XPATH, "/html/body/div[4]/div[1]/div[2]/form/div[3]/div/a")
        self.terms_policy_checkbox = (By.ID, "remember")
        self.continue_button_XPATH = (By.XPATH, "/html/body/div[4]/div[4]/div[3]/a/button")

        #Setup Your Accouut Locators
        self.first_name_ID = (By.ID, "_r_21_-form-item")
        self.last_name_ID = (By.ID, "_r_22_-form-item")
        self.email_address_ID = (By.ID, "_r_23_-form-item")
        self.phone_number_ID = (By.ID, "_r_25_-form-item")
        self.password_XPATH = (By.XPATH, '//*[@id="_r_27_-form-item"]/input')
        self.confirm_password_XPATH = (By.XPATH, '//*[@id="_r_27_-form-item"]/input')



    def click_login(self):
        self.driver.find_element(*self.login_button_XPATH).click()

    def click_signup(self):
        self.driver.find_element(*self.signup_button_XPATH).click()

    def click_checkbox(self):
        self.driver.find_element(*self.terms_policy_checkbox).click()

    def click_continue_button(self):
        self.driver.find_element(*self.continue_button_XPATH).click()

    def set_first_name(self, firstname):
        self.driver.find_element(*self.first_name_ID).click
        self.driver.find_element(*self.first_name_ID).send_keys(firstname)

    def set_last_name(self, lastname):
        self.driver.find_element(*self.last_name_ID).click
        self.driver.find_element(*self.last_name_ID).send_keys(lastname)

    def set_email_address(self, email):
        self.driver.find_element(*self.email_address_ID).click()
        self.driver.find_element(*self.email_address_ID).send_keys(email)

    def set_phone_number(self, phoneno):
        self.driver.find_element(*self.phone_number_ID).click()
        self.driver.find_element(*self.phone_number_ID).send_keys(phoneno)

    def set_password(self, password):
        self.driver.find_element(*self.password_XPATH).click()
        self.driver.find_element(*self.password_XPATH).send_keys(password)

    def set_confirm_password(self, Confirmpassword):
        self.driver.find_element(*self.confirm_password_XPATH).click()
        self.driver.find_element(*self.confirm_password_XPATH).send_keys(Confirmpassword)










        






        
        

    

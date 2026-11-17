from selenium import webdriver
from selenium.webdriver.common.by import By
# For Keyboard Actions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Signup(): 
    def __init__(self, driver: webdriver.chrome):  # Initializing driver
        self.driver = driver

        # Saving Locator
        self.login_button_XPATH = (By.XPATH, "//a[@class='px-4 flex items-center gap-2']")
        self.signup_button_XPATH = (By.XPATH, "/html/body/div[4]/div[1]/div[2]/form/div[3]/div/a")
        self.terms_policy_checkbox = (By.ID, "remember")
        self.continue_button_XPATH = (By.XPATH, "/html/body/div[4]/div[4]/div[3]/a/button")

        # 1. Setup Your Accouut Locators
        self.first_name_NAME = (By.NAME, "firstName")
        self.last_name_NAME = (By.NAME, "lastName")
        self.email_address_NAME = (By.NAME, "email")
        self.phone_number_NAME = (By.NAME, "phoneNumber")
        self.password_NAME = (By.NAME, "password")
        self.confirm_password_NAME = (By.NAME, "confirmPassword")
        self.next_button_XPAH = (By.XPATH, "//button[@type='submit']")

        # 2. Agency Details Locators

        self.name_NAME = (By.NAME, "agency_name")
        self.agency_role_NAME = (By.NAME, "role_in_agency")
        self.agency_email_NAME = (By.NAME, "agency_email")
        self.agency_website_NAME = (By.NAME, "agency_website")
        self.agency_Address_NAME = (By.NAME, "agency_address")
        self.agency_operator_region_XPATH = (By.XPATH, "//span[@class='font-satoshi-regular text-translucent']")
        self.region_search_CSSselector = (By.CSS_SELECTOR, "input[placeholder='Search...']")
        self.search_result_XPATH = (By.XPATH, "//span[normalize-space()='Nepal']")
        self.next2_button_CSSselector = (By.CSS_SELECTOR, "button[type='submit']")

        # 3. Professional experience Locators

        self.years_of_experience_button_CSSselector = (By.CSS_SELECTOR, "#_r_37e_-form-item")
        self.experience_options_XPATH = (By.XPATH, "//div[@role='presentation']//div[1]")
        self.no_of_students_CSSselector = (By.CSS_SELECTOR, "#_r_2v5_-form-item")
        self.focus_area_CSSselector = (By.CSS_SELECTOR, "#_r_2v6_-form-item")
        self.sucess_metricsCSS_selector = (By.CSS_SELECTOR, "#_r_2v7_-form-item")
        self.services_checkbox_CSSselector = (By.CSS_SELECTOR, "#_r_2vc_-form-item")
        self.next3_CSSselector = (By.CSS_SELECTOR, "button[type='submit']")

        # 4. Verification and Preferences
        self.Business_reg_number_NAME = (By.NAME, "business_registration_number")
        self.preffered_countries_CSSselector = (By.CSS_SELECTOR,".font-satoshi-regular.text-translucent")



    def click_login(self):
        self.driver.find_element(*self.login_button_XPATH).click()

    def click_signup(self):
        self.driver.find_element(*self.signup_button_XPATH).click()

    def click_checkbox(self):
        self.driver.find_element(*self.terms_policy_checkbox).click()

    def click_continue_button(self):
        self.driver.find_element(*self.continue_button_XPATH).click()

    def set_first_name(self, firstname):
        self.driver.find_element(*self.first_name_NAME).click()
        self.driver.find_element(*self.first_name_NAME).send_keys(firstname)

    def set_last_name(self, lastname):
        self.driver.find_element(*self.last_name_NAME).click()
        self.driver.find_element(*self.last_name_NAME).send_keys(lastname)

    def set_email_address(self, email):
        self.driver.find_element(*self.email_address_NAME).click()
        self.driver.find_element(*self.email_address_NAME).send_keys(email)

    def set_phone_number(self, phoneno):
        self.driver.find_element(*self.phone_number_NAME).click()
        self.driver.find_element(*self.phone_number_NAME).send_keys(phoneno)

    def set_password(self, password):
        self.driver.find_element(*self.password_NAME).click()
        self.driver.find_element(*self.password_NAME).send_keys(password)

    def set_confirm_password(self, Confirmpassword):
        self.driver.find_element(*self.confirm_password_NAME).click()
        self.driver.find_element(*self.confirm_password_NAME).send_keys(Confirmpassword)

    def click_next(self):
        self.driver.find_element(*self.next_button_XPAH).click()

    # Scrollpage

    def scroll_page(self, x=0, y=500):
        self.driver.execute_script("window.scrollBy(arguments[0], arguments[1]);", x, y)

    # Methods for agency details

    def set_agency_name(self, AgencyName):
        self.driver.find_element(*self.name_NAME).click() 
        self.driver.find_element(*self.name_NAME).send_keys(AgencyName)

    def set_role_in_agency(self, Agencyrole):
        self.driver.find_element(*self.agency_role_NAME).click() 
        self.driver.find_element(*self.agency_role_NAME).send_keys(Agencyrole)

    def set_agency_email(self, AgencyEmail):
        self.driver.find_element(*self.agency_email_NAME).click() 
        self.driver.find_element(*self.agency_email_NAME).send_keys(AgencyEmail)

    def set_agency_website(self, AgencyWebsite):
        self.driver.find_element(*self.agency_website_NAME).click()
        self.driver.find_element(*self.agency_website_NAME).send_keys(AgencyWebsite)

    def set_agency_address(self, AgencyAddress):
        self.driver.find_element(*self.agency_Address_NAME).click()
        self.driver.find_element(*self.agency_Address_NAME).send_keys(AgencyAddress)

    def click_region_of_operation(self):
        self.driver.find_element(*self.agency_operator_region_XPATH).click()

    def search_region(self, Search):
        self.driver.find_element(*self.region_search_CSSselector).click()
        self.driver.find_element(*self.region_search_CSSselector).send_keys(Search)

    def click_search_result(self):
        self.driver.find_element(*self.search_result_XPATH).click()
        
    def click_next2(self):
        self.driver.find_element(*self.next2_button_CSSselector).click()

    # Methods for Professional Experience

    def click_experience_menu(self):
        self.driver.find_element(*self.years_of_experience_button_CSSselector).click()

    def click_experience_option(self):
        self.driver.find_element(*self.experience_options_XPATH).click()

    def set_number_of_students_recruited(self, studentnumber):
        self.driver.find_element(*self.no_of_students_CSSselector).send_keys(studentnumber)

    def set_focus_area(self, focusarea):
        self.driver.find_element(*self.focus_area_CSSselector).send_keys(focusarea)

    def set_sucess_matrix(self, sucessmatrix_percentage):
        self.driver.find_element(*self.sucess_metricsCSS_selector).send_keys(sucessmatrix_percentage)

    def click_Service_provided(self):
        self.driver.find_element(*self.services_checkbox_CSSselector).click()

    def click_next3(self):
        self.driver.find_element(*self.next3_CSSselector).click()



    

    

        

    

    

    










        






        
        

    

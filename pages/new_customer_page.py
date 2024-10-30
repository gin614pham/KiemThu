from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys


class NewCustomerPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "http://www.demo.guru99.com/V4/manager/addcustomerpage.php"

    def open(self):
        self.driver.get(self.url)

    CUSTOMER_NAME = (By.NAME, "name")
    MESSAGE_NAME = (By.ID, "message")
    GENDER_MALE = (By.XPATH, "//input[@name='rad1' and @value='m']")
    DOB = (By.ID, "dob")
    MESSAGE_DOB = (By.ID, "message24")
    ADDRESS = (By.NAME, "addr")
    MESSAGE_ADDRESS = (By.ID, "message3")
    CITY = (By.NAME, "city")
    MESSAGE_CITY = (By.ID, "message4")
    STATE = (By.NAME, "state")
    MESSAGE_STATE = (By.ID, "message5")
    PIN = (By.NAME, "pinno")
    MESSAGE_PIN = (By.ID, "message6")
    MOBILE_NUMBER = (By.NAME, "telephoneno")
    MESSAGE_MOBILE = (By.ID, "message7")
    EMAIL = (By.NAME, "emailid")
    MESSAGE_EMAIL = (By.ID, "message9")
    PASSWORD = (By.NAME, "password")
    MESSAGE_PASSWORD = (By.ID, "message18")
    SUBMIT_BUTTON = (By.NAME, "sub")

    def create_new_customer_with_no_data(self):
        self.driver.find_element(*self.CUSTOMER_NAME).send_keys(Keys.TAB)
        self.driver.find_element(*self.DOB).send_keys(Keys.TAB)
        self.driver.find_element(*self.ADDRESS).send_keys(Keys.TAB)
        self.driver.find_element(*self.CITY).send_keys(Keys.TAB)
        self.driver.find_element(*self.STATE).send_keys(Keys.TAB)
        self.driver.find_element(*self.PIN).send_keys(Keys.TAB)
        self.driver.find_element(*self.MOBILE_NUMBER).send_keys(Keys.TAB)
        self.driver.find_element(*self.EMAIL).send_keys(Keys.TAB)
        self.driver.find_element(*self.PASSWORD).send_keys(Keys.TAB)

    def create_new_customer(self, name, dob, address, city, state, pin, mobile, email, password):
        self.driver.find_element(*self.CUSTOMER_NAME).send_keys(name)
        self.driver.find_element(*self.DOB).send_keys(dob)
        self.driver.find_element(*self.ADDRESS).send_keys(address)
        self.driver.find_element(*self.CITY).send_keys(city)
        self.driver.find_element(*self.STATE).send_keys(state)
        self.driver.find_element(*self.PIN).send_keys(pin)
        self.driver.find_element(*self.MOBILE_NUMBER).send_keys(mobile)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
     
    def get_error_message(self) -> str:
        name_error = self.driver.find_element(*self.MESSAGE_NAME).text
        dob_error = self.driver.find_element(*self.MESSAGE_DOB).text
        address_error = self.driver.find_element(*self.MESSAGE_ADDRESS).text
        city_error = self.driver.find_element(*self.MESSAGE_CITY).text
        state_error = self.driver.find_element(*self.MESSAGE_STATE).text
        pin_error = self.driver.find_element(*self.MESSAGE_PIN).text
        mobile_error = self.driver.find_element(*self.MESSAGE_MOBILE).text
        email_error = self.driver.find_element(*self.MESSAGE_EMAIL).text
        password_error = self.driver.find_element(*self.MESSAGE_PASSWORD).text
        return {
            "name_error": name_error,
            "dob_error": dob_error,
            "address_error": address_error,
            "city_error": city_error,
            "state_error": state_error,
            "pin_error": pin_error,
            "mobile_error": mobile_error,
            "email_error": email_error,
            "password_error": password_error
        }

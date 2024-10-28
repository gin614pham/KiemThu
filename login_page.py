# login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Adjust according to your HTML
        self.username_field = (By.ID, "username")
        # Adjust according to your HTML
        self.password_field = (By.ID, "password")
        # Adjust according to your HTML
        self.inpatient_ward_option = (By.ID, "Inpatient Ward")
        # Adjust according to your HTML
        self.login_button = (By.ID, "loginButton")
        # Adjust based on actual error message locator
        self.error_message_locator = (By.CSS_SELECTOR, ".alert.alert-danger")

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_field)
        ).send_keys(username)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_field)
        ).send_keys(password)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.inpatient_ward_option)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def get_error_message(self):
        # Wait for the error message element to be present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.error_message_locator)
        )
        # Find the error message element and return its text
        error_element = self.driver.find_element(*self.error_message_locator)
        return error_element.text if error_element else ""

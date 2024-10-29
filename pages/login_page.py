import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Các locator cho các phần tử
    USERNAME_INPUT = (By.NAME, "uid")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.NAME, "btnLogin")
    ERROR_MESSAGE = (By.CLASS_NAME, "heading3")
    ERROR_MESSAGE_USERNAME = (By.ID, "message23")
    ERROR_MESSAGE_PASSWORD = (By.ID, "message18")

    # Hàm đăng nhập
    def login(self, username: str, password: str):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login_with_no_username_and_password(self):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(Keys.TAB)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(Keys.TAB)

        # Hàm lấy thông báo lỗi
    def get_error_message(self) -> str:
        username_error = self.driver.find_element(
            *self.ERROR_MESSAGE_USERNAME).text
        password_error = self.driver.find_element(
            *self.ERROR_MESSAGE_PASSWORD).text
        return {
            "username_error": username_error,
            "password_error": password_error,
        }

    def get_alert_text(self) -> str:
        try:
            alert = self.driver.switch_to.alert
            error_message = alert.text
            alert.accept()
            return error_message
        except NoAlertPresentException:
            return "No alert present"

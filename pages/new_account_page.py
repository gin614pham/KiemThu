from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class NewAccountPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://www.demo.guru99.com/V4/manager/addAccount.php"

    def open(self):
        self.driver.get(self.url)

    CUSTOMER_ID = (By.NAME, "cusid")
    ACCOUNT_TYPE = (By.NAME, "selaccount")
    INITIAL_DEPOSIT = (By.NAME, "inideposit")
    SUBMIT_BUTTON = (By.NAME, "button2")
    MESSAGE_CUST_ID = (By.ID, "message14")
    MESSAGE_INIT_DEPOSIT = (By.ID, "message19")

    def create_new_account(self, customer_id, initial_deposit):
        self.driver.find_element(*self.CUSTOMER_ID).send_keys(customer_id)
        self.driver.find_element(*self.ACCOUNT_TYPE).send_keys(Keys.TAB)
        self.driver.find_element(
            *self.INITIAL_DEPOSIT).send_keys(initial_deposit)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def get_error_message(self):
        cust_id_error = self.driver.find_element(*self.MESSAGE_CUST_ID).text
        init_deposit_error = self.driver.find_element(
            *self.MESSAGE_INIT_DEPOSIT).text
        return {
            "cust_id_error": cust_id_error,
            "init_deposit_error": init_deposit_error
        }

    def create_new_account_with_no_data(self):
        self.driver.find_element(*self.CUSTOMER_ID).send_keys(Keys.TAB)
        self.driver.find_element(*self.INITIAL_DEPOSIT).send_keys(Keys.TAB)

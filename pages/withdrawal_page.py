from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys


class WithdrawalPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://www.demo.guru99.com/V4/manager/WithdrawalInput.php"

    def open(self):
        self.driver.get(self.url)

    ACCOUNT_NO = (By.NAME, "accountno")
    DEPOSIT_AMOUNT = (By.NAME, "ammount")
    DESCRIPTION = (By.NAME, "desc")
    SUBMIT_BUTTON = (By.NAME, "AccSubmit")
    MESSAGE_ACCOUNT_NO = (By.ID, "message2")
    MESSAGE_AMOUNT = (By.ID, "message1")
    MESSAGE_DESC = (By.ID, "message17")

    def make_withdrawal(self, account_no, deposit_amount, description):
        self.driver.find_element(*self.ACCOUNT_NO).send_keys(account_no)
        self.driver.find_element(
            *self.DEPOSIT_AMOUNT).send_keys(deposit_amount)
        self.driver.find_element(*self.DESCRIPTION).send_keys(description)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
    def get_error_message(self):
        account_no_error = self.driver.find_element(
            *self.MESSAGE_ACCOUNT_NO).text
        deposit_amount_error = self.driver.find_element(
            *self.MESSAGE_AMOUNT).text
        description_error = self.driver.find_element(
            *self.MESSAGE_DESC).text
        
        return {
            "account_no_error": account_no_error,
            "deposit_amount_error": deposit_amount_error,
            "description_error": description_error
        }


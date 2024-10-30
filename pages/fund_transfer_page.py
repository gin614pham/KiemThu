from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoAlertPresentException


class FundTransferPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = 'https://www.demo.guru99.com/V4/manager/FundTransInput.php'

    def open(self):
        self.driver.get(self.url)

    PAYERS_ACCOUNT_NO = (By.NAME, 'payersaccount')
    MESSAGE_PAYERS_ACCOUNT_NO = (By.ID, 'message10')
    PAYEES_ACCOUNT_NO = (By.NAME, 'payeeaccount')
    MESSAGE_PAYEES_ACCOUNT_NO = (By.ID, 'message11')
    AMMOUNT = (By.NAME, 'ammount')
    MESSAGE_AMMOUNT = (By.ID, 'message1')
    DESCRIPTION = (By.NAME, 'desc')
    MESSAGE_DESCRIPTION = (By.ID, 'message17')
    SUBMIT_BUTTON = (By.NAME, 'AccSubmit')

    def input_fund_transfer(self, payers_account_no, payees_account_no, ammount, description):
        self.driver.find_element(
            *self.PAYERS_ACCOUNT_NO).send_keys(payers_account_no)
        self.driver.find_element(
            *self.PAYEES_ACCOUNT_NO).send_keys(payees_account_no)
        self.driver.find_element(
            *self.AMMOUNT).send_keys(ammount)
        self.driver.find_element(*self.DESCRIPTION).send_keys(description)

    def fund_transfer(self, payers_account_no, payees_account_no, ammount, description):
        self.input_fund_transfer(
            payers_account_no, payees_account_no, ammount, description)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def get_error_message(self):
        payers_account_no_error = self.driver.find_element(
            *self.MESSAGE_PAYERS_ACCOUNT_NO).text
        payees_account_no_error = self.driver.find_element(
            *self.MESSAGE_PAYEES_ACCOUNT_NO).text
        amount_error = self.driver.find_element(
            *self.MESSAGE_AMMOUNT).text
        description_error = self.driver.find_element(
            *self.MESSAGE_DESCRIPTION).text

        return {
            'payers_account_no_error': payers_account_no_error,
            'payees_account_no_error': payees_account_no_error,
            'amount_error': amount_error,
            'description_error': description_error
        }

    def get_alert_text(self) -> str:
        try:
            alert = self.driver.switch_to.alert
            error_message = alert.text
            alert.accept()
            return error_message
        except NoAlertPresentException:
            return "No alert present"

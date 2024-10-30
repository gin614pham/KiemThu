from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoAlertPresentException


class CustomizedStatementFormPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://www.demo.guru99.com/V4/manager/CustomisedStatementInput.php"

    def open(self):
        self.driver.get(self.url)

    ACCOUNT_NO = (By.NAME, "accountno")
    FROM_DATE = (By.NAME, "fdate")
    TO_DATE = (By.NAME, "tdate")
    MINIMUM_TRANSACTION_VALUE = (By.NAME, "amountlowerlimit")
    NUMBER_OF_TRANSACTION = (By.NAME, "numtransaction")
    MESSAGE_ACCOUNT_NO = (By.ID, "message2")
    MESSAGE_FROM_DATE = (By.ID, "message26")
    MESSAGE_TO_DATE = (By.ID, "message27")
    MESSAGE_MINIMUM_TRANSACTION_VALUE = (By.ID, "message12")
    MESSAGE_NUMBER_OF_TRANSACTION = (By.ID, "message13")
    SUBMIT_BUTTON = (By.NAME, "AccSubmit")

    def input_customized_statement(
        self,
        account_no,
        from_date,
        to_date,
        minimum_transaction_value,
        number_of_transaction,
    ):
        self.driver.find_element(*self.ACCOUNT_NO).send_keys(account_no)
        self.driver.find_element(*self.FROM_DATE).send_keys(from_date)
        self.driver.find_element(*self.TO_DATE).send_keys(to_date)
        self.driver.find_element(*self.MINIMUM_TRANSACTION_VALUE).send_keys(
            minimum_transaction_value
        )
        self.driver.find_element(*self.NUMBER_OF_TRANSACTION).send_keys(
            number_of_transaction
        )

    def submit_customized_statement(
        self,
        account_no,
        from_date,
        to_date,
        minimum_transaction_value,
        number_of_transaction,
    ):
        self.input_customized_statement(
            account_no,
            from_date,
            to_date,
            minimum_transaction_value,
            number_of_transaction,
        )
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def get_error_message(self):
        account_no_error = self.driver.find_element(*self.MESSAGE_ACCOUNT_NO).text
        from_date_error = self.driver.find_element(*self.MESSAGE_FROM_DATE).text
        to_date_error = self.driver.find_element(*self.MESSAGE_TO_DATE).text
        minimum_transaction_value_error = self.driver.find_element(
            *self.MESSAGE_MINIMUM_TRANSACTION_VALUE
        ).text
        message_number_of_transaction_error = self.driver.find_element(
            *self.MESSAGE_NUMBER_OF_TRANSACTION
        ).text

        return {
            "account_no_error": account_no_error,
            "from_date_error": from_date_error,
            "to_date_error": to_date_error,
            "minimum_transaction_value_error": minimum_transaction_value_error,
            "message_number_of_transaction_error": message_number_of_transaction_error,
        }

    def get_alert_text(self) -> str:
        try:
            alert = self.driver.switch_to.alert
            error_message = alert.text
            alert.accept()
            return error_message
        except NoAlertPresentException:
            return "No alert present"

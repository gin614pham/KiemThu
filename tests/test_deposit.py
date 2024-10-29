import pytest
from pages.login_page import LoginPage
from pages.deposit_page import DepositPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope="module")
def deposit_page(driver):
    return DepositPage(driver)


def test_deposit_with_no_data(deposit_page, login_page):
    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    deposit_page.open()
    deposit_page.make_deposit_with_no_data()
    error_message = deposit_page.get_error_message()
    assert error_message["account_no_error"] == "Account Number must not be blank"
    assert error_message["deposit_amount_error"] == "Amount field must not be blank"
    assert error_message["description_error"] == "Description can not be blank"


@pytest.mark.parametrize("account_no, deposit_amount, description", [
    ("2", "999999", "NO DESCRIPTION"),])
def test_deposit_with_account_not_exist(deposit_page, login_page, account_no, deposit_amount, description):
    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    deposit_page.open()
    deposit_page.make_deposit(account_no, deposit_amount, description)
    alert = WebDriverWait(deposit_page.driver, 10).until(EC.alert_is_present())
    error_message = alert.text
    assert "Account does not exist" in error_message
    alert.accept()


@pytest.mark.parametrize("account_no, deposit_amount, description", [
    ("310103", "500", "SENT TO PHUC"),])
def test_deposit_success(deposit_page, login_page, account_no, deposit_amount, description):
    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    deposit_page.open()
    deposit_page.make_deposit(account_no, deposit_amount, description)
    assert "Guru99 Bank Manager HomePage" in deposit_page.driver.title

import pytest
from pages.login_page import LoginPage
from pages.new_account_page import NewAccountPage


@pytest.fixture(scope="module")
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope="module")
def new_account_page(driver):
    return NewAccountPage(driver)


def test_create_new_account_with_no_data(login_page, new_account_page):
    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_account_page.open()
    new_account_page.create_new_account_with_no_data()
    error_message = new_account_page.get_error_message()
    assert error_message["cust_id_error"] == "Customer ID is required"
    assert error_message["init_deposit_error"] == "Initial Deposit must not be blank"


@pytest.mark.parametrize("customer_id, initial_deposit", [
    ("3123155", "5000"),])
def test_create_new_account(login_page, new_account_page, customer_id, initial_deposit):
    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_account_page.open()
    new_account_page.create_new_account(customer_id, initial_deposit)
    assert "Guru99 Bank Manager HomePage" in new_account_page.driver.title

import pytest 
from pages.login_page import LoginPage
from pages.new_account_page import NewAccountPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


# @pytest.mark.parametrize("customer_id, initial_deposit", [
#     ("3123155", "5000"),])
# def test_create_new_account(login_page, new_account_page, customer_id, initial_deposit):
#     login_page.open()
#     login_page.login("mngr599099", "zAqyhYr")
#     new_account_page.open()
#     new_account_page.create_new_account(customer_id, initial_deposit)
#     assert "Guru99 Bank Manager HomePage" in new_account_page.driver.title


@pytest.mark.parametrize("customer_id, initial_deposit", [
    ("987yt", "1000"),])
def test_create_new_account_TCNewAccount1(login_page, new_account_page, customer_id, initial_deposit):
    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_account_page.open()
    new_account_page.create_new_account(customer_id, initial_deposit)
    alert = WebDriverWait(new_account_page.driver,
                        10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "Please fill all fields"    
    alert.accept()

    error_message = new_account_page.get_error_message()
    assert error_message["cust_id_error"] == "Characters are not allowed"


@pytest.mark.parametrize("customer_id, initial_deposit", [
    ("956*0", "1000y"),])
def test_create_new_account_TCNewAccount2(login_page, new_account_page, customer_id, initial_deposit):
    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_account_page.open()
    new_account_page.create_new_account(customer_id, initial_deposit)
    alert = WebDriverWait(new_account_page.driver,
                        10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "Please fill all fields"    
    alert.accept()

    error_message = new_account_page.get_error_message()
    assert error_message["cust_id_error"] == "Special characters are not allowed"
    assert error_message["init_deposit_error"] == "Characters are not allowed"


@pytest.mark.parametrize("customer_id, initial_deposit", [
    ("95690", "1000"),])
def test_create_new_account_TCNewAccount3(login_page, new_account_page, customer_id, initial_deposit):
    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_account_page.open()
    new_account_page.create_new_account(customer_id, initial_deposit)
    assert "Gtpl Bank Customer Registration Page" in new_account_page.driver.title

@pytest.mark.parametrize("customer_id, initial_deposit", [
    ("95690", "300"),])
def test_create_new_account_TCNewAccount4(login_page, new_account_page, customer_id, initial_deposit):
    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_account_page.open()
    new_account_page.create_new_account(customer_id, initial_deposit)
    alert = WebDriverWait(new_account_page.driver,
                        10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "Intial deposite must be Rs. 500 or more"    
    alert.accept()

@pytest.mark.parametrize("customer_id, initial_deposit", [
    ("9590", "1000"),])
def test_create_new_account_TCNewAccount5(login_page, new_account_page, customer_id, initial_deposit):
    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_account_page.open()
    new_account_page.create_new_account(customer_id, initial_deposit)
    alert = WebDriverWait(new_account_page.driver,
                        10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "Customer does not exist!!"    
    alert.accept()


@pytest.mark.parametrize("customer_id, initial_deposit", [
    ("956&0", " 3500"),])
def test_create_new_account_TCNewAccount6(login_page, new_account_page, customer_id, initial_deposit):
    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_account_page.open()
    new_account_page.create_new_account(customer_id, initial_deposit)
    alert = WebDriverWait(new_account_page.driver,
                        10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "Please fill all fields"    
    alert.accept()

    error_message = new_account_page.get_error_message()
    assert error_message["cust_id_error"] == "Special characters are not allowed"
    assert error_message["init_deposit_error"] == "First character can not have space"


@pytest.mark.parametrize("customer_id, initial_deposit", [
    ("95690", "34y4"),])
def test_create_new_account_TCNewAccount7(login_page, new_account_page, customer_id, initial_deposit):
    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_account_page.open()
    new_account_page.create_new_account(customer_id, initial_deposit)
    alert = WebDriverWait(new_account_page.driver,
                        10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "Please fill all fields"    
    alert.accept()

    error_message = new_account_page.get_error_message()
    assert error_message["init_deposit_error"] == "Characters are not allowed"


@pytest.mark.parametrize("customer_id, initial_deposit", [
    (" 95690", "34&4"),])
def test_create_new_account_TCNewAccount8(login_page, new_account_page, customer_id, initial_deposit):
    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_account_page.open()
    new_account_page.create_new_account(customer_id, initial_deposit)
    alert = WebDriverWait(new_account_page.driver,
                        10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "Please fill all fields"    
    alert.accept()

    error_message = new_account_page.get_error_message()
    assert error_message["cust_id_error"] == "First character can not have space"
    assert error_message["init_deposit_error"] == "Special characters are not allowed"


@pytest.mark.parametrize("customer_id, initial_deposit", [
    ("50705", "1000"),])
def test_create_new_account_TCNewAccount9(login_page, new_account_page, customer_id, initial_deposit):
    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_account_page.open()
    new_account_page.create_new_account(customer_id, initial_deposit)
    alert = WebDriverWait(new_account_page.driver,
                        10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "You are not authorize to Add Account for this Customer"    
    alert.accept()

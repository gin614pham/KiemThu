from typing import KeysView
import pytest
from pages.login_page import LoginPage
from pages.withdrawal_page import WithdrawalPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="module")
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope="module")
def withdrawal_page(driver):
    return WithdrawalPage(driver)

@pytest.mark.parametrize("account_no, deposit_amount, description", [
    ("34840", "abc", {Keys.TAB}),])
def test_TCWD1(withdrawal_page, login_page, account_no, deposit_amount, description):
    login_page.open()
    login_page.login("mngr599498", "mEdAmeg")
    withdrawal_page.open()
    withdrawal_page.make_withdrawal(account_no, deposit_amount, description)
    alert = WebDriverWait(withdrawal_page.driver, 10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "Please fill all fields"
    alert.accept()
    error_message = withdrawal_page.get_error_message()
    assert error_message["deposit_amount_error"] == "Characters are not allowed"
    assert error_message["description_error"] == "Description can not be blank"
@pytest.mark.parametrize("account_no, deposit_amount, description", [
    ("abcd", "12@", "valid"),])
def test_TCWD2(withdrawal_page, login_page, account_no, deposit_amount, description):
    login_page.open()
    login_page.login("mngr599498", "mEdAmeg")
    withdrawal_page.open()
    withdrawal_page.make_withdrawal(account_no, deposit_amount, description)
    alert = WebDriverWait(withdrawal_page.driver, 10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "Please fill all fields"
    alert.accept()
    error_message = withdrawal_page.get_error_message()
    assert error_message["account_no_error"] == "Characters are not allowed"
    assert error_message["deposit_amount_error"] == "Special characters are not allowed"
@pytest.mark.parametrize("account_no, deposit_amount, description", [
    ("310103", "130000", "SENT TO PHUC"),])
def test_TCWD3(withdrawal_page, login_page, account_no, deposit_amount, description):
    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    withdrawal_page.open()
    withdrawal_page.make_withdrawal(account_no, deposit_amount, description)
    assert "Guru99 Bank Manager HomePage" in withdrawal_page.driver.title
@pytest.mark.parametrize("account_no, deposit_amount, description", [
    ("abcd", {Keys.TAB}, {Keys.TAB}),])
def test_TCWD4(withdrawal_page, login_page, account_no, deposit_amount, description):
    login_page.open()
    login_page.login("mngr599498", "mEdAmeg")
    withdrawal_page.open()
    withdrawal_page.make_withdrawal(account_no, deposit_amount, description)
    alert = WebDriverWait(withdrawal_page.driver, 10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "Please fill all fields"
    alert.accept()
    error_message = withdrawal_page.get_error_message()
    assert error_message["account_no_error"] == "Characters are not allowed"
    assert error_message["deposit_amount_error"] == "Amount field must not be blank"
    assert error_message["description_error"] == "Description can not be blank"
@pytest.mark.parametrize("account_no, deposit_amount, description", [
    ({Keys.TAB}, {Keys.TAB}, "valid"),])
def test_TCWD5(withdrawal_page, login_page, account_no, deposit_amount, description):
    login_page.open()
    login_page.login("mngr599498", "mEdAmeg")
    withdrawal_page.open()
    withdrawal_page.make_withdrawal(account_no, deposit_amount, description)
    alert = WebDriverWait(withdrawal_page.driver, 10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "Please fill all fields"
    alert.accept()
    error_message = withdrawal_page.get_error_message()
    assert error_message["account_no_error"] == "Account Number must not be blank"
    assert error_message["deposit_amount_error"] == "Amount field must not be blank"
@pytest.mark.parametrize("account_no, deposit_amount, description", [
    ("34840", {Keys.TAB}, "valid"),])
def test_TCWD6(withdrawal_page, login_page, account_no, deposit_amount, description):
    login_page.open()
    login_page.login("mngr599498", "mEdAmeg")
    withdrawal_page.open()
    withdrawal_page.make_withdrawal(account_no, deposit_amount, description)
    alert = WebDriverWait(withdrawal_page.driver, 10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "Please fill all fields"
    alert.accept()
    error_message = withdrawal_page.get_error_message()
    assert error_message["deposit_amount_error"] == "Amount field must not be blank"
@pytest.mark.parametrize("account_no, deposit_amount, description", [
    ({Keys.TAB}, "abc", {Keys.TAB}),])
def test_TCWD7(withdrawal_page, login_page, account_no, deposit_amount, description):
    login_page.open()
    login_page.login("mngr599498", "mEdAmeg")
    withdrawal_page.open()
    withdrawal_page.make_withdrawal(account_no, deposit_amount, description)
    alert = WebDriverWait(withdrawal_page.driver, 10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "Please fill all fields"
    alert.accept()
    error_message = withdrawal_page.get_error_message()
    assert error_message["account_no_error"] == "Account Number must not be blank"
    assert error_message["deposit_amount_error"] == "Characters are not allowed"
    assert error_message["description_error"] == "Description can not be blank"
@pytest.mark.parametrize("account_no, deposit_amount, description", [
    ("123@", "130000", {Keys.TAB}),])
def test_TCWD8(withdrawal_page, login_page, account_no, deposit_amount, description):
    login_page.open()
    login_page.login("mngr599498", "mEdAmeg")
    withdrawal_page.open()
    withdrawal_page.make_withdrawal(account_no, deposit_amount, description)
    alert = WebDriverWait(withdrawal_page.driver, 10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "Please fill all fields"
    alert.accept()
    error_message = withdrawal_page.get_error_message()
    assert error_message["account_no_error"] == "Special characters are not allowed"
    assert error_message["description_error"] == "Description can not be blank"
@pytest.mark.parametrize("account_no, deposit_amount, description", [
    ({Keys.TAB}, "130000", {Keys.TAB}),])
def test_TCWD9(withdrawal_page, login_page, account_no, deposit_amount, description):
    login_page.open()
    login_page.login("mngr599498", "mEdAmeg")
    withdrawal_page.open()
    withdrawal_page.make_withdrawal(account_no, deposit_amount, description)
    alert = WebDriverWait(withdrawal_page.driver, 10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "Please fill all fields"
    alert.accept()
    error_message = withdrawal_page.get_error_message()
    assert error_message["account_no_error"] == "Account Number must not be blank"
    assert error_message["description_error"] == "Description can not be blank"





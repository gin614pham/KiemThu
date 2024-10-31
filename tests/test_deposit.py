from typing import KeysView
import pytest
from pages.login_page import LoginPage
from pages.deposit_page import DepositPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="module")
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope="module")
def deposit_page(driver):
    return DepositPage(driver)


@pytest.mark.parametrize("account_no, deposit_amount, description", [
    ("34840", "abc", {Keys.TAB}),])
def test_TCDP1(deposit_page, login_page, account_no, deposit_amount, description):
    login_page.open()
    login_page.login("mngr599498", "mEdAmeg")
    deposit_page.open()
    deposit_page.make_deposit(account_no, deposit_amount, description)
    alert = WebDriverWait(deposit_page.driver, 10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "Please fill all fields"
    alert.accept()
    error_message = deposit_page.get_error_message()
    assert error_message["deposit_amount_error"] == "Characters are not allowed"
    assert error_message["description_error"] == "Description can not be blank"


@pytest.mark.parametrize("account_no, deposit_amount, description", [
    ("abcd", "12@", "valid"),])
def test_TCDP2(deposit_page, login_page, account_no, deposit_amount, description):
    login_page.open()
    login_page.login("mngr599498", "mEdAmeg")
    deposit_page.open()
    deposit_page.make_deposit(account_no, deposit_amount, description)
    alert = WebDriverWait(deposit_page.driver, 10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "Please fill all fields"
    alert.accept()
    error_message = deposit_page.get_error_message()
    assert error_message["account_no_error"] == "Characters are not allowed"
    assert error_message["deposit_amount_error"] == "Special characters are not allowed"


@pytest.mark.parametrize("account_no, deposit_amount, description", [
    ("139416", "30", "SENT TO PHUC"),])
def test_TCDP3(deposit_page, login_page, account_no, deposit_amount, description):
    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    deposit_page.open()
    deposit_page.make_deposit(account_no, deposit_amount, description)
    assert "Guru99 Bank Manager HomePage" in deposit_page.driver.title


@pytest.mark.parametrize("account_no, deposit_amount, description", [
    ("abcd", {Keys.TAB}, {Keys.TAB}),])
def test_TCDP4(deposit_page, login_page, account_no, deposit_amount, description):
    login_page.open()
    login_page.login("mngr599498", "mEdAmeg")
    deposit_page.open()
    deposit_page.make_deposit(account_no, deposit_amount, description)
    alert = WebDriverWait(deposit_page.driver, 10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "Please fill all fields"
    alert.accept()
    error_message = deposit_page.get_error_message()
    assert error_message["account_no_error"] == "Characters are not allowed"
    assert error_message["deposit_amount_error"] == "Amount field must not be blank"
    assert error_message["description_error"] == "Description can not be blank"


@pytest.mark.parametrize("account_no, deposit_amount, description", [
    ({Keys.TAB}, {Keys.TAB}, "valid"),])
def test_TCDP5(deposit_page, login_page, account_no, deposit_amount, description):
    login_page.open()
    login_page.login("mngr599498", "mEdAmeg")
    deposit_page.open()
    deposit_page.make_deposit(account_no, deposit_amount, description)
    alert = WebDriverWait(deposit_page.driver, 10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "Please fill all fields"
    alert.accept()
    error_message = deposit_page.get_error_message()
    assert error_message["account_no_error"] == "Account Number must not be blank"
    assert error_message["deposit_amount_error"] == "Amount field must not be blank"


@pytest.mark.parametrize("account_no, deposit_amount, description", [
    ("34840", {Keys.TAB}, "valid"),])
def test_TCDP6(deposit_page, login_page, account_no, deposit_amount, description):
    login_page.open()
    login_page.login("mngr599498", "mEdAmeg")
    deposit_page.open()
    deposit_page.make_deposit(account_no, deposit_amount, description)
    alert = WebDriverWait(deposit_page.driver, 10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "Please fill all fields"
    alert.accept()
    error_message = deposit_page.get_error_message()
    assert error_message["deposit_amount_error"] == "Amount field must not be blank"


@pytest.mark.parametrize("account_no, deposit_amount, description", [
    ({Keys.TAB}, "abc", {Keys.TAB}),])
def test_TCDP7(deposit_page, login_page, account_no, deposit_amount, description):
    login_page.open()
    login_page.login("mngr599498", "mEdAmeg")
    deposit_page.open()
    deposit_page.make_deposit(account_no, deposit_amount, description)
    alert = WebDriverWait(deposit_page.driver, 10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "Please fill all fields"
    alert.accept()
    error_message = deposit_page.get_error_message()
    assert error_message["account_no_error"] == "Account Number must not be blank"
    assert error_message["deposit_amount_error"] == "Characters are not allowed"
    assert error_message["description_error"] == "Description can not be blank"


@pytest.mark.parametrize("account_no, deposit_amount, description", [
    ("123@", "12", {Keys.TAB}),])
def test_TCDP8(deposit_page, login_page, account_no, deposit_amount, description):
    login_page.open()
    login_page.login("mngr599498", "mEdAmeg")
    deposit_page.open()
    deposit_page.make_deposit(account_no, deposit_amount, description)
    alert = WebDriverWait(deposit_page.driver, 10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "Please fill all fields"
    alert.accept()
    error_message = deposit_page.get_error_message()
    assert error_message["account_no_error"] == "Special characters are not allowed"
    assert error_message["description_error"] == "Description can not be blank"


@pytest.mark.parametrize("account_no, deposit_amount, description", [
    ({Keys.TAB}, "12", {Keys.TAB}),])
def test_TCDP9(deposit_page, login_page, account_no, deposit_amount, description):
    login_page.open()
    login_page.login("mngr599498", "mEdAmeg")
    deposit_page.open()
    deposit_page.make_deposit(account_no, deposit_amount, description)
    alert = WebDriverWait(deposit_page.driver, 10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "Please fill all fields"
    alert.accept()
    error_message = deposit_page.get_error_message()
    assert error_message["account_no_error"] == "Account Number must not be blank"
    assert error_message["description_error"] == "Description can not be blank"

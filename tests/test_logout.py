import pytest
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope="module")
def logout_page(driver):
    return LogoutPage(driver)


def test_logout(logout_page, login_page):
    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    logout_page.logout()
    alert = WebDriverWait(logout_page.driver, 10).until(EC.alert_is_present())
    error_message = alert.text
    assert "You Have Succesfully Logged Out" in error_message
    alert.accept()

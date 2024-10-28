import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from login_page import LoginPage


@pytest.fixture(scope="module")
def driver():
    service = Service(r"D:\Code\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://demo.openmrs.org/openmrs/login.htm")
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login_page(driver):
    return LoginPage(driver)


def test_login_incorrect_password(login_page):
    login_page.login("Admin", "wrongpassword")
    assert "Invalid username/password. Please try again." in login_page.get_error_message(
    ), "Error message not displayed for wrong password."


def test_login_invalid_username(login_page):
    login_page.login("InvalidUser", "Admin123")
    assert "Invalid username/password. Please try again." in login_page.get_error_message(
    ), "Error message not displayed for invalid username."


def test_login_empty_username_password(login_page):
    login_page.login("", "")
    assert "Invalid username/password. Please try again." in login_page.get_error_message(
    ), "Error message not displayed for empty fields."


def test_login_empty_password(login_page):
    login_page.login("Admin", "")
    assert "Invalid username/password. Please try again." in login_page.get_error_message(
    ), "Error message not displayed for empty password."


def test_successful_login(login_page):
    login_page.login("Admin", "Admin123")
    assert "home.page" in login_page.driver.current_url, "Login failed or incorrect page."

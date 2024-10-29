import pytest
from pages.login_page import LoginPage
from pages.new_customer_page import NewCustomerPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope="module")
def new_customer_page(driver):
    return NewCustomerPage(driver)


def test_create_new_customer_with_no_data(new_customer_page, login_page):
    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_customer_page.open()
    new_customer_page.create_new_customer_with_no_data()
    error_message = new_customer_page.get_error_message()
    assert error_message["name_error"] == "Customer name must not be blank"
    assert error_message["dob_error"] == "Date Field must not be blank"
    assert error_message["address_error"] == "Address Field must not be blank"
    assert error_message["city_error"] == "City Field must not be blank"
    assert error_message["state_error"] == "State must not be blank"
    assert error_message["pin_error"] == "PIN Code must not be blank"
    assert error_message["mobile_error"] == "Mobile no must not be blank"
    assert error_message["email_error"] == "Email-ID must not be blank"
    assert error_message["password_error"] == "Password must not be blank"


# note: Thay doi email de khong bi trung
@pytest.mark.parametrize("name, dob, address, city, state, pin, mobile, email, password", [
    ("PhamHoangPhucAA", "01-31-2003", "Tran Dai Nghia Street", "Da Nang", "DN",
     "550000", "0123456789", "Q0bP2@example.com", "password123"),])
def test_create_new_customer(login_page, new_customer_page, name, dob, address, city,
                             state, pin, mobile, email, password):

    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_customer_page.open()

    new_customer_page.create_new_customer(name, dob, address, city, state,
                                          pin, mobile, email, password)
    assert "Guru99 Bank Customer Registration Page" in new_customer_page.driver.title


# Note: De email trung voi email cho test truoc
@pytest.mark.parametrize("name, dob, address, city, state, pin, mobile, email, password", [
    ("PhamHoangPhucAA", "01-31-2003", "Tran Dai Nghia Street", "Da Nang", "DN",
     "550000", "0123456789", "Q0bP2@example.com", "password123"),])
def test_create_new_customer_with_existing_email(login_page, new_customer_page, name, dob, address, city,
                                                 state, pin, mobile, email, password):

    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_customer_page.open()

    new_customer_page.create_new_customer(name, dob, address, city, state,
                                          pin, mobile, email, password)
    alert = WebDriverWait(new_customer_page.driver,
                          10).until(EC.alert_is_present())
    error_message = alert.text
    assert "Email Address Already Exist !!" in error_message
    alert.accept()

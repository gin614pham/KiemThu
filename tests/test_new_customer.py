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
     "550000", "0123456789", "Q0bP231@example.com", "password123"),])
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
     "550000", "0123456789", "Q0bP231@example.com", "password123"),])
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


@pytest.mark.parametrize("name, dob, address, city, state, pin, mobile, email, password", [
    ("", "01-31-2003", "", "HaTinh@", "Son Tra",
     "", "12345678", "lenhatlinh", "password123"),])
def test_create_new_customer_TC01(login_page, new_customer_page, name, dob, address, city,
                             state, pin, mobile, email, password):

    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_customer_page.open()

    new_customer_page.create_new_customer(name, dob, address, city, state,
                                          pin, mobile, email, password)
    alert = WebDriverWait(new_customer_page.driver,
                          10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "please fill all fields"    
    alert.accept()
    error_message = new_customer_page.get_error_message()
    assert error_message["name_error"] == "Customer name must not be blank"
    assert error_message["address_error"] == "Address Field must not be blank"
    assert error_message["pin_error"] == "PIN Code must not be blank"
    assert error_message["email_error"] == "Email-ID is not valid"


@pytest.mark.parametrize("name, dob, address, city, state, pin, mobile, email, password", [
    ("Link14", "02/02/2000", "470 Tran Dai Nghia", "Ha Tinh", "",
     "abc12322", "abc123456", "lenhatlinh@gmail.com", ""),])
def test_create_new_customer_TC02(login_page, new_customer_page, name, dob, address, city,
                             state, pin, mobile, email, password):

    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_customer_page.open()

    new_customer_page.create_new_customer(name, dob, address, city, state,
                                          pin, mobile, email, password)
    alert = WebDriverWait(new_customer_page.driver,
                          10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "please fill all fields"    
    alert.accept()
    error_message = new_customer_page.get_error_message()
    assert error_message["name_error"] == "Numbers are not allowed"
    assert error_message["state_error"] == "State must not be blank"
    assert error_message["pin_error"] == "Characters are not allowed"
    assert error_message["mobile_error"] == "Characters are not allowed"


@pytest.mark.parametrize("name, dob, address, city, state, pin, mobile, email, password", [
    ("SunLink", "02/02/2000", "2/9 Tran Dai Nghia", "", "Vippro99",
     "1", " 012345678", "lenhatlinh1@gmail.com", "password123"),])
def test_create_new_customer_TC03(login_page, new_customer_page, name, dob, address, city,
                             state, pin, mobile, email, password):

    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_customer_page.open()

    new_customer_page.create_new_customer(name, dob, address, city, state,
                                          pin, mobile, email, password)
    alert = WebDriverWait(new_customer_page.driver,
                          10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "please fill all fields"    
    alert.accept()
    error_message = new_customer_page.get_error_message()
    assert error_message["city_error"] == "City Field must not be blank"
    assert error_message["state_error"] == "Numbers are not allowed"
    assert error_message["pin_error"] == "PIN Code must have 6 Digits"
    assert error_message["mobile_error"] == "First character can not have space"


@pytest.mark.parametrize("name, dob, address, city, state, pin, mobile, email, password", [
    ("Link@gma", "", "Tran@Nghia", "HaTinh12", " Nhaem",
     "888888", "", "nhatlinh@", ""),])
def test_create_new_customer_TC04(login_page, new_customer_page, name, dob, address, city,
                             state, pin, mobile, email, password):

    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_customer_page.open()

    new_customer_page.create_new_customer(name, dob, address, city, state,
                                          pin, mobile, email, password)
    alert = WebDriverWait(new_customer_page.driver,
                          10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "please fill all fields"    
    alert.accept()
    error_message = new_customer_page.get_error_message()
    assert error_message["name_error"] == "Special characters are not allowed"
    assert error_message["dob_error"] == "Date Field must not be blank"
    assert error_message["address_error"] == "Special characters are not allowed"
    assert error_message["city_error"] == "Numbers are not allowed"
    assert error_message["state_error"] == "First character can not have space"
    assert error_message["mobile_error"] == "Mobile no must not be blank"
    assert error_message["email_error"] == "Email-ID is not valid"



@pytest.mark.parametrize("name, dob, address, city, state, pin, mobile, email, password", [
    ("NhatLink", "", "470 Tran Dai Nghia", " Ha Tinh", "ZzLinhzZ@123",
     "@12345", "@12345", "quocphu", ""),])
def test_create_new_customer_TC05(login_page, new_customer_page, name, dob, address, city,
                             state, pin, mobile, email, password):

    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_customer_page.open()

    new_customer_page.create_new_customer(name, dob, address, city, state,
                                          pin, mobile, email, password)
    alert = WebDriverWait(new_customer_page.driver,
                          10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "please fill all fields"    
    alert.accept()
    error_message = new_customer_page.get_error_message()
    assert error_message["dob_error"] == "Date Field must not be blank"
    assert error_message["city_error"] == "First character can not have space"
    assert error_message["state_error"] == "Special characters are not allowed"
    assert error_message["pin_error"] == "Special characters are not allowed"
    assert error_message["email_error"] == "Email-ID is not valid"


@pytest.mark.parametrize("name, dob, address, city, state, pin, mobile, email, password", [
    (" Sunlink", "", " 24haibatrung", "Ha Tinh", "123anhem",
     "888888", "@123456", "phamquocphu@gmail.com", "password123"),])
def test_create_new_customer_TC06(login_page, new_customer_page, name, dob, address, city,
                             state, pin, mobile, email, password):

    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_customer_page.open()

    new_customer_page.create_new_customer(name, dob, address, city, state,
                                          pin, mobile, email, password)
    alert = WebDriverWait(new_customer_page.driver,
                          10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "please fill all fields"    
    alert.accept()
    error_message = new_customer_page.get_error_message()
    assert error_message["name_error"] == "First character can not have space"
    assert error_message["dob_error"] == "Date Field must not be blank"
    assert error_message["address_error"] == "First character can not have space"
    assert error_message["state_error"] == "Numbers are not allowed"
    assert error_message["mobile_error"] == "Special characters are not allowed"


@pytest.mark.parametrize("name, dob, address, city, state, pin, mobile, email, password", [
    ("", "02/02/2000", "", "", "",
     "$a1234", " O12345", "linh321@@@", "password123"),])
def test_create_new_customer_TC07(login_page, new_customer_page, name, dob, address, city,
                             state, pin, mobile, email, password):

    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_customer_page.open()

    new_customer_page.create_new_customer(name, dob, address, city, state,
                                          pin, mobile, email, password)
    alert = WebDriverWait(new_customer_page.driver,
                          10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "please fill all fields"    
    alert.accept()
    error_message = new_customer_page.get_error_message()
    assert error_message["name_error"] == "Customer name must not be blank"
    assert error_message["address_error"] == "Address Field must not be blank"
    assert error_message["city_error"] == "City Field must not be blank"
    assert error_message["state_error"] == "State must not be blank"
    assert error_message["pin_error"] == "Special characters are not allowed"
    assert error_message["mobile_error"] == "First character can not have space"
    assert error_message["email_error"] == "Email-ID is not valid"


@pytest.mark.parametrize("name, dob, address, city, state, pin, mobile, email, password", [
    ("12SunLink", "02/02/2000", " 63 nguyen chi thanh", "Ha Tinh", "SonTra",
     " O22222", "1234567", "linh123@gmail.com", ""),])
def test_create_new_customer_TC08(login_page, new_customer_page, name, dob, address, city,
                             state, pin, mobile, email, password):

    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_customer_page.open()

    new_customer_page.create_new_customer(name, dob, address, city, state,
                                          pin, mobile, email, password)
    alert = WebDriverWait(new_customer_page.driver,
                          10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "please fill all fields"    
    alert.accept()
    error_message = new_customer_page.get_error_message()
    assert error_message["name_error"] == "Numbers are not allowed"
    assert error_message["address_error"] == "First character can not have space"
    assert error_message["pin_error"] == "First character can not have space"


@pytest.mark.parametrize("name, dob, address, city, state, pin, mobile, email, password", [
    ("@Link", "02/02/2000", "470 Tran Dai Nghia", " HaTinh", "SonTra",
     "888888", "@abc456", " linh@gmail.com", "password123"),])
def test_create_new_customer_TC09(login_page, new_customer_page, name, dob, address, city,
                             state, pin, mobile, email, password):

    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_customer_page.open()

    new_customer_page.create_new_customer(name, dob, address, city, state,
                                          pin, mobile, email, password)
    alert = WebDriverWait(new_customer_page.driver,
                          10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "please fill all fields"    
    alert.accept()
    error_message = new_customer_page.get_error_message()
    assert error_message["name_error"] == "Special characters are not allowed"
    assert error_message["mobile_error"] == "Special characters are not allowed"
    assert error_message["email_error"] == "First character can not have space"


@pytest.mark.parametrize("name, dob, address, city, state, pin, mobile, email, password", [
    ("Sun Link", "02/02/2000", "Tran-Dai-Nghia", "Ha-Tinh", "Son Tra",
     "abcd@@", "12345678", " linhtm@gmail.com", ""),])
def test_create_new_customer_TC10(login_page, new_customer_page, name, dob, address, city,
                             state, pin, mobile, email, password):

    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_customer_page.open()

    new_customer_page.create_new_customer(name, dob, address, city, state,
                                          pin, mobile, email, password)
    alert = WebDriverWait(new_customer_page.driver,
                          10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "please fill all fields"    
    alert.accept()
    error_message = new_customer_page.get_error_message()
    assert error_message["address_error"] == "Special characters are not allowed"
    assert error_message["city_error"] == "Special characters are not allowed"
    assert error_message["pin_error"] == "Special characters are not allowed"


@pytest.mark.parametrize("name, dob, address, city, state, pin, mobile, email, password", [
    ("", "", "470 Tran Dai Nghia", "Ha Tinh", "SonTra",
     "0", "", " quocphu", ""),])
def test_create_new_customer_TC11(login_page, new_customer_page, name, dob, address, city,
                             state, pin, mobile, email, password):

    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_customer_page.open()

    new_customer_page.create_new_customer(name, dob, address, city, state,
                                          pin, mobile, email, password)
    alert = WebDriverWait(new_customer_page.driver,
                          10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "please fill all fields"    
    alert.accept()
    error_message = new_customer_page.get_error_message()
    assert error_message["name_error"] == "Customer name must not be blank"
    assert error_message["dob_error"] == "Date Field must not be blank"
    assert error_message["pin_error"] == "PIN Code must have 6 Digits"
    assert error_message["mobile_error"] == "Mobile no must not be blank"
    assert error_message["email_error"] == "First character can not have space"


@pytest.mark.parametrize("name, dob, address, city, state, pin, mobile, email, password", [
    ("SunLink", "02/02/2000", "Tran-Dai-Nghia", "12HaTinh", "",
     "", "#$abcd", "", "password123"),])
def test_create_new_customer_TC12(login_page, new_customer_page, name, dob, address, city,
                             state, pin, mobile, email, password):

    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_customer_page.open()

    new_customer_page.create_new_customer(name, dob, address, city, state,
                                          pin, mobile, email, password)
    alert = WebDriverWait(new_customer_page.driver,
                          10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "please fill all fields"    
    alert.accept()
    error_message = new_customer_page.get_error_message()
    assert error_message["address_error"] == "Special characters are not allowed"
    assert error_message["city_error"] == "Numbers are not allowed"
    assert error_message["state_error"] == "State must not be blank"
    assert error_message["pin_error"] == "PIN Code must not be blank"
    assert error_message["mobile_error"] == "Special characters are not allowed"
    assert error_message["email_error"] == "Email-ID must not be blank"


@pytest.mark.parametrize("name, dob, address, city, state, pin, mobile, email, password", [
    ("SunLink", "", "", "Ha Tinh", " Nhaem",
     "888888", "12345678", "phamquocphu1@gmail.com", ""),])
def test_create_new_customer_TC13(login_page, new_customer_page, name, dob, address, city,
                             state, pin, mobile, email, password):

    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_customer_page.open()

    new_customer_page.create_new_customer(name, dob, address, city, state,
                                          pin, mobile, email, password)
    alert = WebDriverWait(new_customer_page.driver,
                          10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "please fill all fields"    
    alert.accept()
    error_message = new_customer_page.get_error_message()
    assert error_message["dob_error"] == "Date Field must not be blank"
    assert error_message["address_error"] == "Address Field must not be blank"
    assert error_message["state_error"] == "First character can not have space"


@pytest.mark.parametrize("name, dob, address, city, state, pin, mobile, email, password", [
    ("12SunLink", "02/02/2000", "Tran-Dai-Nghia", "Ha Tinh", "1234444",
     "abcdef", "12345678", "plenhatlinh@gmail.com", "password123"),])
def test_create_new_customer_TC14(login_page, new_customer_page, name, dob, address, city,
                             state, pin, mobile, email, password):

    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_customer_page.open()

    new_customer_page.create_new_customer(name, dob, address, city, state,
                                          pin, mobile, email, password)
    alert = WebDriverWait(new_customer_page.driver,
                          10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "please fill all fields"    
    alert.accept()
    error_message = new_customer_page.get_error_message()
    assert error_message["name_error"] == "Numbers are not allowed"
    assert error_message["address_error"] == "Special characters are not allowed"
    assert error_message["state_error"] == "Numbers are not allowed"
    assert error_message["pin_error"] == "Characters are not allowed"


@pytest.mark.parametrize("name, dob, address, city, state, pin, mobile, email, password", [
    (" SunLink", "", "470 Tran Dai Nghia", "12Ha@Tinh", "@@@@@@",
     "@@@@@@", "", "lin htm@gmail.com", ""),])
def test_create_new_customer_TC15(login_page, new_customer_page, name, dob, address, city,
                             state, pin, mobile, email, password):

    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_customer_page.open()

    new_customer_page.create_new_customer(name, dob, address, city, state,
                                          pin, mobile, email, password)
    alert = WebDriverWait(new_customer_page.driver,
                          10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "please fill all fields"    
    alert.accept()
    error_message = new_customer_page.get_error_message()
    assert error_message["name_error"] == "First character can not have space"
    assert error_message["dob_error"] == "Date Field must not be blank"
    assert error_message["city_error"] == "Special characters are not allowed"
    assert error_message["state_error"] == "Special characters are not allowed"
    assert error_message["pin_error"] == "Special characters are not allowed"
    assert error_message["mobile_error"] == "Mobile no must not be blank"
    assert error_message["email_error"] == "Email-ID is not valid"


@pytest.mark.parametrize("name, dob, address, city, state, pin, mobile, email, password", [
    ("", "", "Tran-Dai-Nghia", "", "SonTra",
     "888888", " O222222", "", ""),])
def test_create_new_customer_TC16(login_page, new_customer_page, name, dob, address, city,
                             state, pin, mobile, email, password):

    login_page.open()
    login_page.login("mngr599099", "zAqyhYr")
    new_customer_page.open()

    new_customer_page.create_new_customer(name, dob, address, city, state,
                                          pin, mobile, email, password)
    alert = WebDriverWait(new_customer_page.driver,
                          10).until(EC.alert_is_present())
    error_message_alert = alert.text
    assert error_message_alert == "please fill all fields"    
    alert.accept()
    error_message = new_customer_page.get_error_message()
    assert error_message["name_error"] == "Customer name must not be blank"
    assert error_message["dob_error"] == "Date Field must not be blank"
    assert error_message["address_error"] == "Special characters are not allowed"
    assert error_message["city_error"] == "City Field must not be blank"
    assert error_message["mobile_error"] == "First character can not have space"
    assert error_message["email_error"] == "Email-ID must not be blank"
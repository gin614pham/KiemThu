import pytest
from pages.login_page import LoginPage


@pytest.fixture(scope="module")
def login_page(driver):
    return LoginPage(driver)


def test_login_empty_fields(login_page):
    login_page.login_with_no_username_and_password()

    # Kiểm tra thông báo lỗi xuất hiện
    error_message = login_page.get_error_message()
    assert error_message["username_error"] == "User-ID must not be blank"
    assert error_message["password_error"] == "Password must not be blank"


@pytest.mark.parametrize("username, password", [
    ("invalidUser", "invalidPass"),  # Dữ liệu không hợp lệ
])
def test_login_failure(login_page, username, password):
    login_page.login(username, password)
    # Kiểm tra thông báo lỗi xuất hiện
    error_message = login_page.get_alert_text()
    assert "User or Password is not valid" in error_message


@pytest.mark.parametrize("username, password", [
    ("mngr599099", "zAqyhYr"),
])
def test_login_success(login_page, username, password):
    login_page.login(username, password)
    # Kiểm tra tiêu đề sau khi đăng nhập thành công
    assert "Guru99 Bank Manager HomePage" in login_page.driver.title

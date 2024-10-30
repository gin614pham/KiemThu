import pytest
from pages.login_page import LoginPage
from pages.customized_statement_form_page import CustomizedStatementFormPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@pytest.fixture(scope="module")
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope="module")
def customized_statement_form_page(driver):
    return CustomizedStatementFormPage(driver)


# Các cặp kiểm thử dựa trên bảng
@pytest.mark.parametrize(
    "account_no, from_date, to_date, minimum_transaction_value, number_of_transaction, expected_errors",
    [
        # TCSF1
        (
            {Keys.TAB},
            {Keys.TAB},
            "10/23/2024",
            "50",
            "5",
            {
                "account_no_error": "Account Number must not be blank",
                "from_date_error": "From Date Field must not be blank",
            },
        ),
        # TCSF2
        (
            "asd",
            {Keys.TAB},
            "10/23/2024",
            "50",
            "5",
            {
                "account_no_error": "Characters are not allowed",
                "from_date_error": "From Date Field must not be blank",
            },
        ),
        # TCSF3
        (
            "'`~!@#$%^&*()-_=+{}[]|;:,<.>/?",
            {Keys.TAB},
            "10/23/2024",
            "50",
            "5",
            {
                "account_no_error": "Special characters are not allowed",
                "from_date_error": "From Date Field must not be blank",
            },
        ),
        # TCSF4
        (
            "139454",
            {Keys.TAB},
            {Keys.TAB},
            "50",
            "5",
            {
                "from_date_error": "From Date Field must not be blank",
                "to_date_error": "To Date Field must not be blank",
            },
        ),
        # TCSF5
        (
            {Keys.TAB},
            "10/23/2024",
            "10/30/2024",
            {Keys.TAB},
            "5",
            {
                "account_no_error": "Account Number must not be blank",
                "minimum_transaction_value_error": "Minimum transaction value must not be blank",
            },
        ),
        # TCSF6
        (
            "asd",
            "10/23/2024",
            "10/30/2024",
            {Keys.TAB},
            "5",
            {
                "account_no_error": "Characters are not allowed",
                "minimum_transaction_value_error": "Minimum transaction value must not be blank",
            },
        ),
        # TCSF7
        (
            "'`~!@#$%^&*()-_=+{}[]|;:,<.>/?",
            "10/23/2024",
            "10/30/2024",
            {Keys.TAB},
            "5",
            {
                "account_no_error": "Special characters are not allowed",
                "minimum_transaction_value_error": "Minimum transaction value must not be blank",
            },
        ),
        # TCSF8
        (
            {Keys.TAB},
            "10/23/2024",
            "10/30/2024",
            "asd",
            "5",
            {
                "account_no_error": "Account Number must not be blank",
                "minimum_transaction_value_error": "Characters are not allowed",
            },
        ),
        # TCSF9
        (
            "asd",
            "10/23/2024",
            "10/30/2024",
            "asd",
            "5",
            {
                "account_no_error": "Characters are not allowed",
                "minimum_transaction_value_error": "Characters are not allowed",
            },
        ),
        # TCSF10
        (
            "'`~!@#$%^&*()-_=+{}[]|;:,<.>/?",
            "10/23/2024",
            "10/30/2024",
            "asd",
            "5",
            {
                "account_no_error": "Special characters are not allowed",
                "minimum_transaction_value_error": "Characters are not allowed",
            },
        ),
        # TCSF11
        (
            {Keys.TAB},
            "10/23/2024",
            "10/30/2024",
            "'`~!@#$%^&*()-_=+{}[]|;:,<.>/?",
            "5",
            {
                "account_no_error": "Account Number must not be blank",
                "minimum_transaction_value_error": "Special characters are not allowed",
            },
        ),
        # TCSF12
        (
            "asd",
            "10/23/2024",
            "10/30/2024",
            "'`~!@#$%^&*()-_=+{}[]|;:,<.>/?",
            "5",
            {
                "account_no_error": "Characters are not allowed",
                "minimum_transaction_value_error": "Special characters are not allowed",
            },
        ),
        # TCSF13
        (
            "'`~!@#$%^&*()-_=+{}[]|;:,<.>/?",
            "10/23/2024",
            "10/30/2024",
            "'`~!@#$%^&*()-_=+{}[]|;:,<.>/?",
            "5",
            {
                "account_no_error": "Special characters are not allowed",
                "minimum_transaction_value_error": "Special characters are not allowed",
            },
        ),
        # TCSF14
        (
            "139454",
            "10/23/2024",
            "10/30/2024",
            {Keys.TAB},
            {Keys.TAB},
            {
                "minimum_transaction_value_error": "Minimum transaction value must not be blank",
                "number_of_transaction_error": "Number of transaction must not be blank",
            },
        ),
    ],
)
def test_customized_statement_form(
    customized_statement_form_page,
    login_page,
    account_no,
    from_date,
    to_date,
    minimum_transaction_value,
    number_of_transaction,
    expected_errors,
):
    # Đăng nhập và mở trang Customized Statement
    login_page.open()
    login_page.login("mngr599535", "AsebUnU")
    customized_statement_form_page.open()

    # Điền form với các giá trị từ cặp kiểm thử
    customized_statement_form_page.input_customized_statement(
        account_no, from_date, to_date, minimum_transaction_value, number_of_transaction
    )

    # Kiểm tra thông báo lỗi xuất hiện như mong đợi cho từng cặp
    error_message = customized_statement_form_page.get_error_message()
    for field, expected_text in expected_errors.items():
        assert (
            error_message[field] == expected_text
        ), f"Expected {field} to have error '{expected_text}', got '{error_message[field]}'"


# TCSF15
@pytest.mark.parametrize(
    "account_no, from_date, to_date, minimum_transaction_value, number_of_transaction",
    [("139454a", {Keys.TAB}, {Keys.TAB}, "asd", "asd")],
)
def test_invalid_account(
    customized_statement_form_page,
    login_page,
    account_no,
    from_date,
    to_date,
    minimum_transaction_value,
    number_of_transaction,
):
    # Đăng nhập và mở trang Customized Statement
    login_page.open()
    login_page.login("mngr599535", "AsebUnU")
    customized_statement_form_page.open()

    # Điền form với các giá trị từ cặp kiểm thử
    customized_statement_form_page.submit_customized_statement(
        account_no, from_date, to_date, minimum_transaction_value, number_of_transaction
    )

    # Chờ và kiểm tra thông báo lỗi xuất hiện
    alert = WebDriverWait(customized_statement_form_page.driver, 5).until(
        EC.alert_is_present()
    )
    assert (
        alert.text == "Please fill all fields"
    ), f"Expected alert message to be Please fill all fields, but got '{alert.text}'"

    # Đóng thông báo cảnh báo nếu có
    if alert is not None:
        alert.accept()


# TCSF16
@pytest.mark.parametrize(
    "account_no, from_date, to_date, minimum_transaction_value, number_of_transaction",
    [("139454", "10/23/2024", "10/30/2024", "asd", "asd")],
)
def test_invalid_account(
    customized_statement_form_page,
    login_page,
    account_no,
    from_date,
    to_date,
    minimum_transaction_value,
    number_of_transaction,
):
    # Đăng nhập và mở trang Customized Statement
    login_page.open()
    login_page.login("mngr599535", "AsebUnU")
    customized_statement_form_page.open()

    # Điền form với các giá trị từ cặp kiểm thử
    customized_statement_form_page.submit_customized_statement(
        account_no, from_date, to_date, minimum_transaction_value, number_of_transaction
    )

    try:
        # Chờ và kiểm tra thông báo lỗi xuất hiện
        alert = WebDriverWait(customized_statement_form_page.driver, 2).until(
            EC.alert_is_present()
        )

        assert (
            alert.text == "Please fill all fields"
        ), f"Expected alert message to be Please fill all fields, but got '{alert.text}'"

        # Đóng thông báo cảnh báo nếu có
        if alert is not None:
            alert.accept()
            
    except TimeoutException:
        assert False, "Expected alert message, but none appeared."

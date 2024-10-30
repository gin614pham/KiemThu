import pytest
from pages.login_page import LoginPage
from pages.fund_transfer_page import FundTransferPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='module')
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope='module')
def fund_transfer_page(driver):
    return FundTransferPage(driver)

# TFT1: Test empty Payers Account Number
@pytest.mark.parametrize('payers_account_no, payees_account_no, ammount, description', [
    ({Keys.TAB}, '70234345103', '100000', 'transfer'),
])
def test_empty_payers_account_no_payers(fund_transfer_page, login_page, payers_account_no, payees_account_no, ammount, description):
    login_page.open()
    login_page.login('mngr599535', 'AsebUnU')
    fund_transfer_page.open()
    fund_transfer_page.input_fund_transfer(payers_account_no, payees_account_no, ammount, description)

    error_message = fund_transfer_page.get_error_message()
    assert error_message['payers_account_no_error'] == 'Payers Account Number must not be blank'

# TFT2: Test Characters are not allowed in Payers Account Number
@pytest.mark.parametrize('payers_account_no, payees_account_no, ammount, description', [
    ('abc', '70234345103', '100000', 'transfer'),
])
def test_characters_are_not_allowed_payers(fund_transfer_page, login_page, payers_account_no, payees_account_no, ammount, description):
    login_page.open()
    login_page.login('mngr599535', 'AsebUnU')
    fund_transfer_page.open()
    fund_transfer_page.input_fund_transfer(payers_account_no, payees_account_no, ammount, description)

    error_message = fund_transfer_page.get_error_message()
    assert error_message['payers_account_no_error'] == 'Characters are not allowed'

# TFT3: Test Special characters are not allowed in Payers Account Number
@pytest.mark.parametrize('payers_account_no, payees_account_no, ammount, description', [
    ('`~!@#$%^&*()-_=+{}[]|;:,<.>/?', '70234345103', '100000', 'transfer'),
])
def test_special_characters_are_not_allowed_payers(fund_transfer_page, login_page, payers_account_no, payees_account_no, ammount, description):
    login_page.open()
    login_page.login('mngr599535', 'AsebUnU')
    fund_transfer_page.open()
    fund_transfer_page.input_fund_transfer(payers_account_no, payees_account_no, ammount, description)

    error_message = fund_transfer_page.get_error_message()
    assert error_message['payers_account_no_error'] == 'Special characters are not allowed'

# TFT4: Test empty Payees Account Number
@pytest.mark.parametrize('payers_account_no, payees_account_no, ammount, description', [
    ('69234785103', {Keys.TAB}, '100000', 'transfer'),
])
def test_empty_payees_account_no(fund_transfer_page, login_page, payers_account_no, payees_account_no, ammount, description):
    login_page.open()
    login_page.login('mngr599535', 'AsebUnU')
    fund_transfer_page.open()
    fund_transfer_page.input_fund_transfer(payers_account_no, payees_account_no, ammount, description)

    error_message = fund_transfer_page.get_error_message()
    assert error_message['payees_account_no_error'] == 'Payees Account Number must not be blank'

# TFT5: Test Characters are not allowed in Payees Account Number
@pytest.mark.parametrize('payers_account_no, payees_account_no, ammount, description', [
    ('69234785103', 'zxc', '100000', 'transfer'),
])
def test_characters_are_not_allowed_payees(fund_transfer_page, login_page, payers_account_no, payees_account_no, ammount, description):
    login_page.open()
    login_page.login('mngr599535', 'AsebUnU')
    fund_transfer_page.open()
    fund_transfer_page.input_fund_transfer(payers_account_no, payees_account_no, ammount, description)

    error_message = fund_transfer_page.get_error_message()
    assert error_message['payees_account_no_error'] == 'Characters are not allowed'

# TFT6: Test Special characters are not allowed in Payees Account Number
@pytest.mark.parametrize('payers_account_no, payees_account_no, ammount, description', [
    ('69234785103', '`~!@#$%^&*()-_=+{}[]|;:,<.>/?', '100000', 'transfer'),
])
def test_special_characters_are_not_allowed_payees(fund_transfer_page, login_page, payers_account_no, payees_account_no, ammount, description):
    login_page.open()
    login_page.login('mngr599535', 'AsebUnU')
    fund_transfer_page.open()
    fund_transfer_page.input_fund_transfer(payers_account_no, payees_account_no, ammount, description)

    error_message = fund_transfer_page.get_error_message()
    assert error_message['payees_account_no_error'] == 'Special characters are not allowed'

# TFT7: Test empty Amount
@pytest.mark.parametrize('payers_account_no, payees_account_no, ammount, description', [
    ('69234785103', '70234345103', {Keys.TAB}, 'transfer'),
])
def test_empty_amount(fund_transfer_page, login_page, payers_account_no, payees_account_no, ammount, description):
    login_page.open()
    login_page.login('mngr599535', 'AsebUnU')
    fund_transfer_page.open()
    fund_transfer_page.input_fund_transfer(payers_account_no, payees_account_no, ammount, description)

    error_message = fund_transfer_page.get_error_message()
    assert error_message['amount_error'] == 'Amount Field must not be blank'

# TFT8: Test Characters are not allowed in Amount
@pytest.mark.parametrize('payers_account_no, payees_account_no, ammount, description', [
    ('69234785103', '70234345103', 'abc', 'transfer'),
])
def test_characters_are_not_allowed_amount(fund_transfer_page, login_page, payers_account_no, payees_account_no, ammount, description):
    login_page.open()
    login_page.login('mngr599535', 'AsebUnU')
    fund_transfer_page.open()
    fund_transfer_page.input_fund_transfer(payers_account_no, payees_account_no, ammount, description)

    error_message = fund_transfer_page.get_error_message()
    assert error_message['amount_error'] == 'Characters are not allowed'

# TFT9: Test Special characters are not allowed in Amount
@pytest.mark.parametrize('payers_account_no, payees_account_no, ammount, description', [
    ('69234785103', '70234345103', '~!@#$%^&*()-_=+{}[]|;:,<.>/?', 'transfer'),
])
def test_special_characters_are_not_allowed_amount(fund_transfer_page, login_page, payers_account_no, payees_account_no, ammount, description):
    login_page.open()
    login_page.login('mngr599535', 'AsebUnU')
    fund_transfer_page.open()
    fund_transfer_page.input_fund_transfer(payers_account_no, payees_account_no, ammount, description)

    error_message = fund_transfer_page.get_error_message()
    assert error_message['amount_error'] == 'Special characters are not allowed'

# TFT10: Test empty Description
@pytest.mark.parametrize('payers_account_no, payees_account_no, ammount, description', [
    ('69234785103', '70234345103', '100000', ''),
])
def test_empty_description(fund_transfer_page, login_page, payers_account_no, payees_account_no, ammount, description):
    login_page.open()
    login_page.login('mngr599535', 'AsebUnU')
    fund_transfer_page.open()
    fund_transfer_page.input_fund_transfer(payers_account_no, payees_account_no, ammount, description)

    error_message = fund_transfer_page.get_error_message()
    assert error_message['description_error'] == 'Description cannot be blank'

# TFT11: Check if these source and destination account numbers are invalid, system displays an error
@pytest.mark.parametrize('payers_account_no, payees_account_no, ammount, description', [
    ('139454a', '13945b', '50', 'transfer'),
])
def test_invalid_account(fund_transfer_page, login_page, payers_account_no, payees_account_no, ammount, description):
    login_page.open()
    login_page.login('mngr599535', 'AsebUnU')
    fund_transfer_page.open()
    fund_transfer_page.fund_transfer(payers_account_no, payees_account_no, ammount, description)

    alert = WebDriverWait(fund_transfer_page.driver,5).until(EC.alert_is_present())
    assert alert.text == 'Please fill all fields'
    if(alert is not None):
        alert.accept()

# TFT12: Check if these source and destination account numbers are same, system displays an error
@pytest.mark.parametrize('payers_account_no, payees_account_no, ammount, description', [
    ('69234785103', '69234785103', '100000', 'transfer'),
])
def test_same_account(fund_transfer_page, login_page, payers_account_no, payees_account_no, ammount, description):
    login_page.open()
    login_page.login('mngr599535', 'AsebUnU')
    fund_transfer_page.open()
    fund_transfer_page.fund_transfer(payers_account_no, payees_account_no, ammount, description)

    alert = WebDriverWait(fund_transfer_page.driver, 5).until(EC.alert_is_present())
    assert alert.text == 'Payers account No and Payees account No Must Not be Same!!!'
    if(alert is not None):
        alert.accept()

# TFT13: Check if the source account does not have the necessary balance, system displays an error
@pytest.mark.parametrize('payers_account_no, payees_account_no, ammount, description', [
    ('139454', '139455', '999999', 'transfer'),
])
def test_insufficient_balance(fund_transfer_page, login_page, payers_account_no, payees_account_no, ammount, description):
    login_page.open()
    login_page.login('mngr599535', 'AsebUnU')
    fund_transfer_page.open()
    fund_transfer_page.fund_transfer(payers_account_no, payees_account_no, ammount, description)

    alert = WebDriverWait(fund_transfer_page.driver, 5).until(EC.alert_is_present())
    assert alert.text == 'Transfer Failed. Account Balance low!!'
    if(alert is not None):
        alert.accept()

# TFT14: Check if the source account does not associated with manager, System displays an error
@pytest.mark.parametrize('payers_account_no, payees_account_no, ammount, description', [
    ('1', '139455', '100000', 'transfer'),
])
def test_not_associated_manager(fund_transfer_page, login_page, payers_account_no, payees_account_no, ammount, description):
    login_page.open()
    login_page.login('mngr599535', 'AsebUnU')
    fund_transfer_page.open()
    fund_transfer_page.fund_transfer(payers_account_no, payees_account_no, ammount, description)

    alert = WebDriverWait(fund_transfer_page.driver, 5).until(EC.alert_is_present())
    assert alert.text == 'You are not authorize to Transfer Funds from this account!!'
    if(alert is not None):
        alert.accept()

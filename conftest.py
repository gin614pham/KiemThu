import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    # Khởi tạo trình duyệt (ở đây dùng Chrome)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://www.demo.guru99.com/V4/")
    yield driver
    driver.quit()

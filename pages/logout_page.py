from selenium.webdriver.remote.webdriver import WebDriver


class LogoutPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://www.demo.guru99.com/V4/manager/Logout.php"

    def logout(self):
        self.driver.get(self.url)

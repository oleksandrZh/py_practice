from SeleniumPractice import AccountHelper
from SeleniumPractice import AssertHelper
from SeleniumPractice import get_webdriver
from SeleniumPractice import LoginHelper
from SeleniumPractice import NavigationHelper


class Application:

    def __init__(self):
        self.driver = get_webdriver()
        self.driver.maximize_window()
        self.login_helper = LoginHelper(self.driver)
        self.assertion_helper = AssertHelper(self.driver)
        self.navigation_helper = NavigationHelper(self.driver)
        self.account_helper = AccountHelper(self.driver)

    def complete(self):
        self.driver.close()

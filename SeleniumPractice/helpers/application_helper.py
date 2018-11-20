from SeleniumPractice.helpers.account_helper import AccountHelper
from SeleniumPractice.helpers.assertion_helper import AssertHelper
from SeleniumPractice.helpers.driver_helper import get_webdriver
from SeleniumPractice.helpers.login_helper import LoginHelper
from SeleniumPractice.helpers.navigation_helper import NavigationHelper


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

from SeleniumPractice import BalancePage
from SeleniumPractice import DepositPage
from SeleniumPractice import LoginPage
from SeleniumPractice import ManagerHomePage


class BaseHelper:

    def __init__(self, driver):
        self.balance_page = BalancePage(driver)
        self.deposit_page = DepositPage(driver)
        self.login_page = LoginPage(driver)
        self.manager_page = ManagerHomePage(driver)
        self.driver = driver

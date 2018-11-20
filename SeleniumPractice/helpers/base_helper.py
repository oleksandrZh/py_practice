from SeleniumPractice.pages.balance_page import BalancePage
from SeleniumPractice.pages.deposit_page import DepositPage
from SeleniumPractice.pages.login_page import LoginPage
from SeleniumPractice.pages.manager_page import ManagerHomePage


class BaseHelper:

    def __init__(self, driver):
        self.balance_page = BalancePage(driver)
        self.deposit_page = DepositPage(driver)
        self.login_page = LoginPage(driver)
        self.manager_page = ManagerHomePage(driver)
        self.driver = driver

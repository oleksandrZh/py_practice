from pages.balance_page import BalancePage
from pages.deposit_page import DepositPage
from pages.login_page import LoginPage
from pages.manager_page import ManagerHomePage


class BaseHelper:

    def __init__(self, driver):
        self.balance_page = BalancePage(driver)
        self.deposit_page = DepositPage(driver)
        self.login_page = LoginPage(driver)
        self.manager_page = ManagerHomePage(driver)
        self.driver = driver

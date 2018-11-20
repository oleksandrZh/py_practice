from SeleniumPractice.pages.login_page import LoginPage
from SeleniumPractice.pages.manager_page import ManagerHomePage


class AssertHelper:

    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        self.manager_page = ManagerHomePage(driver)
        self.driver = driver

    def get_product_name(self):
        return self.login_page.get_application_name()

    def get_manager_id(self):
        return self.manager_page.get_manager_id().split(' ')[-1]

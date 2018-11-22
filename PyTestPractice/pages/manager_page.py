from locators.locators import ManagerHomeLocators
from pages.base_page import BasePage


class ManagerHomePage(BasePage):

    def get_manager_id(self):
        element = self.driver.find_element(*ManagerHomeLocators.MANAGER_ID)
        return element.text



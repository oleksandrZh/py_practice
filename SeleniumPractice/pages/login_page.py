from SeleniumPractice.pages.base_page import *
from SeleniumPractice.locators.locators import *
from SeleniumPractice.locators.element import *


class LoginPage(BasePage):

    def click_sign_in_button(self):
        element = self.driver.find_element(*LoginPageLocators.SIGN_IN)
        element.click()

    def get_application_name(self):
        element = self.driver.find_element(*LoginPageLocators.APPLICATION_NAME)
        return element.text

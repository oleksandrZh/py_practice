from SeleniumPractice.pages.base_page import *
from SeleniumPractice.locators.locators import *
from SeleniumPractice.locators.element import *


class SigninPage(BasePage):
    def enter_user_name(self, str):
        element = self.driver.find_element(*SigninPageLocators.SIGN_IN_FIELD)
        element.send_keys(str)

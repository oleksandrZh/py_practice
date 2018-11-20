from SeleniumPractice.pages.base_page import *
from SeleniumPractice.locators.locators import *


class LoginPage(BasePage):

    def get_application_name(self):
        element = self.driver.find_element(*LoginPageLocators.APPLICATION_NAME)
        return element.text

    def enter_user_name(self, name):
        element = self.driver.find_element(*LoginPageLocators.USER_ID_FIELD)
        element.send_keys(name)

    def enter_user_pass(self, password):
        element = self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
        element.send_keys(password)

    def click_login_button(self):
        element = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        element.click()

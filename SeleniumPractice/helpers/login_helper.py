from SeleniumPractice.pages.login_page import *


class LoginHelper:

    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        self.driver = driver

    def login_to_site(self, user):
        self.login_page.enter_user_name(user.user_name)
        self.login_page.enter_user_pass(user.user_password)
        self.login_page.click_login_button()

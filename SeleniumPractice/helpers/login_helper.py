from SeleniumPractice.helpers.base_helper import BaseHelper


class LoginHelper(BaseHelper):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login_to_site(self, manager):
        self.login_page.enter_user_name(manager.user_name)
        self.login_page.enter_user_pass(manager.user_password)
        self.login_page.click_login_button()

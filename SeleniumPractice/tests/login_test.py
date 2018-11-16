import unittest
from SeleniumPractice.helpers.driver_helper import *
from SeleniumPractice.pages.login_page import *
from SeleniumPractice.pages.signin_page import *


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Projects/webdrivers/chromedriver.exe")
        self.driver.get("http://qa.jtalks.org/antarcticle/")
        self.login_page = LoginPage(self.driver)
        self.signin_page = SigninPage(self.driver)

    def test_login(self):
        self.assertEqual("Antarcticle QA instance", self.login_page.get_application_name())
        self.login_page.click_sign_in_button()
        self.signin_page.enter_user_name("Test")

    def tearDown(self):
        self.driver.close()

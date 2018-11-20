import unittest

from SeleniumPractice.helpers.assertion_helper import AssertHelper
from SeleniumPractice.helpers.driver_helper import *
from SeleniumPractice.helpers.login_helper import LoginHelper
from SeleniumPractice.helpers.navigation_helper import NavigationHelper
from SeleniumPractice.helpers.user_helper import *


class LoginTest(unittest.TestCase):
    app = None

    def setUp(self, url="http://demo.guru99.com/v4/index.php"):
        app = self.app = Application()
        app.navigation_helper.open_main_page(url)

    def test_login(self):
        self.user = get_valid_user()
        self.assertEqual("Guru99 Bank", self.app.assertion_helper.get_product_name())
        self.app.login_helper.login_to_site(self.user)
        self.assertEqual(self.user.user_name, self.app.assertion_helper.get_manager_id())
        

    def tearDown(self):
        self.app.complete()


# Test application that run test
class Application():

    def __init__(self):
        self.driver = get_webdriver()
        self.login_helper = LoginHelper(self.driver)
        self.assertion_helper = AssertHelper(self.driver)
        self.navigation_helper = NavigationHelper(self.driver)

    def complete(self):
        self.driver.close()

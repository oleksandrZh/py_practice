import unittest

from SeleniumPractice.helpers.application_helper import Application
from SeleniumPractice.helpers.manager_helper import *


class LoginTest(unittest.TestCase):
    app = None

    def setUp(self, url="http://demo.guru99.com/v4/index.php"):
        self.app = Application()
        self.app.navigation_helper.open_main_page(url)

    def test_login(self):
        self.manager = get_valid_manager()
        self.assertEqual("Guru99 Bank", self.app.assertion_helper.get_product_name())
        self.app.login_helper.login_to_site(self.manager)
        self.assertEqual(self.manager.user_name, self.app.assertion_helper.get_manager_id())

    def tearDown(self):
        self.app.complete()

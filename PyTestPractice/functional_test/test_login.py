import unittest
import pytest

from helpers.application_helper import Application
from helpers.manager_helper import get_valid_manager


class LoginTest(unittest.TestCase):
    app = None

    def setUp(self, url="http://demo.guru99.com/v4/index.php"):
        self.app = Application()
        self.app.navigation_helper.open_main_page(url)

    def test_login(self):
        """Test verify that user is able to login with valid credentials"""
        self.manager = get_valid_manager()
        self.assertEqual("Guru99 Bank", self.app.assertion_helper.get_product_name())
        self.app.login_helper.login_to_site(self.manager)
        self.assertEqual(self.manager.user_name, self.app.assertion_helper.get_manager_id())

    def tearDown(self):
        self.app.complete()

    if __name__ == 'main':
        import doctest
        doctest.testmod()
        unittest.main(verbosity=2)

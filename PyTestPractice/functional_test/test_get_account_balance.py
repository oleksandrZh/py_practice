import unittest

import pytest

from helpers.application_helper import Application
from helpers.manager_helper import get_valid_manager


class AccountTest(unittest.TestCase):
    app = None
    ACCOUNT_ID = 52025
    DEPOSIT_AMOUNT = 2000
    DESC = 'Test'

    def setUp(self, url="http://demo.guru99.com/v4/index.php"):
        self.app = Application()
        self.manager = get_valid_manager()
        self.app.navigation_helper.open_main_page(url)

    def test_manager_is_able_to_get_balance(self):
        self.app.login_helper.login_to_site(self.manager)
        self.app.navigation_helper.open_balance_page()
        self.app.account_helper.get_balance_by_account_id(self.ACCOUNT_ID)
        self.value = self.app.assertion_helper.get_balance_for_account()
        self.assertEqual('1000', self.value)

    def test_manager_is_able_to_add_to_existed_deposit(self):
        self.app.login_helper.login_to_site(self.manager)
        self.app.navigation_helper.open_balance_page()
        self.app.account_helper.get_balance_by_account_id(self.ACCOUNT_ID)
        self.initial_value = self.app.assertion_helper.get_balance_for_account()
        self.app.navigation_helper.open_deposit_page()
        self.app.account_helper.add_to_deposit_for_account(self.ACCOUNT_ID, self.DEPOSIT_AMOUNT, self.DESC)
        self.app.navigation_helper.open_balance_page()
        self.app.account_helper.get_balance_by_account_id(self.ACCOUNT_ID)
        self.value = self.app.assertion_helper.get_balance_for_account()
        expected_value = int(self.initial_value) + self.DEPOSIT_AMOUNT
        self.assertEqual(str(expected_value), self.value)

    def test_manager_is_able_to_withdraw_from_existed_deposit(self):
        self.app.login_helper.login_to_site(self.manager)
        self.app.navigation_helper.open_balance_page()
        self.app.account_helper.get_balance_by_account_id(self.ACCOUNT_ID)
        self.initial_value = self.app.assertion_helper.get_balance_for_account()
        self.app.navigation_helper.open_withdrawal_page()
        self.app.account_helper.add_to_deposit_for_account(self.ACCOUNT_ID, self.DEPOSIT_AMOUNT, self.DESC)
        self.app.navigation_helper.open_balance_page()
        self.app.account_helper.get_balance_by_account_id(self.ACCOUNT_ID)
        self.value = self.app.assertion_helper.get_balance_for_account()
        expected_value = int(self.initial_value) - self.DEPOSIT_AMOUNT
        self.assertEqual(str(expected_value), self.value)

    def tearDown(self):
        self.app.complete()

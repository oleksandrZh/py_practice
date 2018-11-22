from helpers.base_helper import BaseHelper


class AssertHelper(BaseHelper):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_product_name(self):
        """Method returns product name from header"""
        return self.login_page.get_application_name()

    def get_manager_id(self):
        return self.manager_page.get_manager_id().split(' ')[-1]

    def get_balance_for_account(self):
        return self.balance_page.get_balance_amount_value()

from helpers.base_helper import BaseHelper


class AccountHelper(BaseHelper):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_balance_by_account_id(self, account_id):
        self.balance_page.enter_account_id(account_id)
        self.balance_page.click_submit_button()

    def add_to_deposit_for_account(self, account_id, amount, description):
        self.deposit_page.enter_account_id(account_id)
        self.deposit_page.enter_amount(amount)
        self.deposit_page.enter_desc(description)
        self.deposit_page.click_submit_button()

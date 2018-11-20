from SeleniumPractice.pages.base_page import BasePage, BalancePageLocators


class BalancePage(BasePage):

    def enter_account_id(self, account_id):
        element = self.driver.find_element(*BalancePageLocators.ACCOUNT_FIELD)
        element.send_keys(account_id)

    def click_submit_button(self):
        element = self.driver.find_element(*BalancePageLocators.SUBMIT_BUTTON)
        element.click()

    def get_balance_amount_value(self):
        element = self.driver.find_element(*BalancePageLocators.BALANCE_AMOUNT)
        return element.text

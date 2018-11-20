from SeleniumPractice.pages.base_page import BasePage, DepositPageLocators


class DepositPage(BasePage):
    def enter_account_id(self, acc_id):
        element = self.driver.find_element(*DepositPageLocators.ACCOUNT_ID_FIELD)
        element.send_keys(acc_id)

    def enter_amount(self, amount):
        element = self.driver.find_element(*DepositPageLocators.AMOUNT_FIELD)
        element.send_keys(amount)

    def enter_desc(self, desc):
        element = self.driver.find_element(*DepositPageLocators.DESCRIPTION_FIELD)
        element.send_keys(desc)

    def click_submit_button(self):
        element = self.driver.find_element(*DepositPageLocators.SUBMIT_BUTTON)
        element.click()

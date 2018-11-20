from selenium.webdriver.common.by import *


class LoginPageLocators(object):
    APPLICATION_NAME = (By.XPATH, '//h2[@class="barone"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@value="LOGIN"]')
    RESET = (By.XPATH, '//input[@value="RESET"]')
    USER_ID_FIELD = (By.XPATH, '//input[@name="uid"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name="password"]')


class ManagerHomeLocators(object):
    MANAGER_ID = (By.XPATH, '//td[contains(text(),"Manger Id")]')


class BalancePageLocators(object):
    ACCOUNT_FIELD = (By.XPATH, '//input[@name="accountno"]')
    SUBMIT_BUTTON = (By.XPATH, '//input[@value="Submit"]')
    BALANCE_AMOUNT = (By.XPATH, './/td[contains(text(),"Balance")]/following-sibling::td')


class DepositPageLocators(object):
    ACCOUNT_ID_FIELD = (By.XPATH, '//input[@name="accountno"]')
    AMOUNT_FIELD = (By.XPATH, '//input[@name="ammount"]')
    DESCRIPTION_FIELD = (By.XPATH, '//input[@name="desc"]')
    SUBMIT_BUTTON = (By.XPATH, '//input[@value="Submit"]')

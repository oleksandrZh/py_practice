from selenium.webdriver.common.by import *


class LoginPageLocators(object):
    APPLICATION_NAME = (By.XPATH, '//h2[@class="barone"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@value="LOGIN"]')
    RESET = (By.XPATH, '//input[@value="RESET"]')
    USER_ID_FIELD = (By.XPATH, '//input[@name="uid"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name="password"]')


class ManagerHomeLocators(object):
    MANAGER_ID = (By.XPATH, '//td[contains(text(),"Manger Id")]')

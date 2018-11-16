from selenium.webdriver.common.by import *


class LoginPageLocators(object):
    SIGN_IN = (By.XPATH, '//a[@href="/antarcticle/signin"]')
    SIGN_UP = (By.XPATH, '//a[@href="/antarcticle/signup"]')
    APPLICATION_NAME = (By.XPATH, '//span[@id="application-name-container"]')


class SigninPageLocators(object):
    SIGN_IN_FIELD = (By.XPATH, '	//input[@placeholder="Username"]')

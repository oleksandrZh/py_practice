from SeleniumPractice.pages.base_page import *
from SeleniumPractice.locators.locators import *
from SeleniumPractice.locators.element import *


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

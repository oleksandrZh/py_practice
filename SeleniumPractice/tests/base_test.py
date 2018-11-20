import unittest

from SeleniumPractice.helpers.driver_helper import get_webdriver


class BaseTest(unittest.TestCase):

    def setUpMain(self):
        self.driver.get()
        #self.driver = get_webdriver()


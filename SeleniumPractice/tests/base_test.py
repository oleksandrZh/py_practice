import unittest


class BaseTest(unittest.TestCase):

    def setUpMain(self):
        self.driver.get()
        #self.driver = get_webdriver()


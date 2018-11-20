from selenium import webdriver


class Driver:
    # def __init__(self):
    #    self.driver = webdriver

    def get_driver(self):
        if self.driver is None:
            self.driver = webdriver.Chrome("C:/Projects/webdrivers/chromedriver.exe")
            return self.driver
        else:
            return self.driver

    def get_main_page(self, url):
        self.driver.get(url)


def get_webdriver():
    # self.driver = webdriver.Chrome("C:/Projects/webdrivers/chromedriver.exe")
    return webdriver.Chrome("C:/Projects/webdrivers/chromedriver.exe")

from selenium import webdriver


class Driver:

    def get_driver(self):
        if self.driver is None:
            self.driver = webdriver.Chrome("C:/Projects/webdrivers/chromedriver.exe")
            return self.driver
        else:
            return self.driver

    def get_main_page(self, url):
        self.driver.get(url)


def get_webdriver():
    return webdriver.Chrome("C:/Projects/webdrivers/chromedriver.exe")

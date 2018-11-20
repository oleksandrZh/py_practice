class NavigationHelper:

    def __init__(self, driver):
        self.driver = driver

    def open_main_page(self, url):
        self.driver.get(url)



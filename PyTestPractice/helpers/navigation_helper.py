class NavigationHelper:

    def __init__(self, driver):
        self.driver = driver

    def open_main_page(self, url):
        self.driver.get(url)

    # hard code: should be separate method implemented
    def open_balance_page(self):
        self.driver.get("http://demo.guru99.com/v4/manager/BalEnqInput.php")

    def open_deposit_page(self):
        self.driver.get("http://demo.guru99.com/v4/manager/DepositInput.php")

    def open_withdrawal_page(self):
        self.driver.get("http://demo.guru99.com/v4/manager/WithdrawalInput.php")

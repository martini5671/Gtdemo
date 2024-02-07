from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "(//li/a[@class = 'nav-link'])[2]")

    def shopItems(self):
        return self.driver.find_element(*Homepage.shop)

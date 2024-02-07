from pageObjects.HomePage import Homepage
from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getlogger()
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        homePage = Homepage(self.driver)
        homePage.shopItems().click()
        # //a[contains(@href, 'shop')] #można też tak
        list_products = self.driver.find_elements(By.XPATH, "//app-card")

        log.info("getting all products ")

        for z in list_products:
            text = z.find_element(By.CLASS_NAME, "card-title").text
            log.info(text)
            if text == "Blackberry":
                z.find_element(By.CSS_SELECTOR, "div.card-footer > button").click()

        self.driver.find_element(By.XPATH, "//a[contains(@class, 'btn-primary')]").click()
        self.driver.find_element(By.XPATH, "//button[@class = 'btn btn-success']").click()

        log.info("passing the country name")
        self.driver.find_element(By.ID, "country").send_keys("ind")
        # explicit wait
        self.verifyLinkPresence("India")

        ##checkbox2
        self.driver.find_element(By.CSS_SELECTOR, "div.checkbox.checkbox-primary > label").click()
        self.driver.find_element(By.XPATH, "//form/input").click()
        success = self.driver.find_element(By.XPATH, "//div[contains(@class, 'alert-success')]").text

        log.info("text received form application is:" + success)

        assert "Success" in success




import time
import pytest
from selenium.webdriver.common.by import By
import TestData.homepage_data as lol

import TestData.homepage_data
from utilities.BaseClass import BaseClass


class Test_HomePage(BaseClass):

    def test_formSubmission(self, get_data):
        self.driver.get("https://www.w3schools.com/html/html_forms.asp")
        self.insert_name(get_data["firstname"])
        self.insert_surname(get_data["lastname"])
        text_intro = self.driver.find_element(By.CSS_SELECTOR, "#main > p.intro").text
        print(text_intro)
        print(text_intro)
        print(text_intro)
        ## Kim dzong Un
        ## Kim Kardashian
        ## Jeff Bezos
        
        assert "HTML" in text_intro
        time.sleep(5)

    @pytest.fixture(params=lol.HomePageData.test_home_page_data)
    def get_data(self, request):
        return request.param

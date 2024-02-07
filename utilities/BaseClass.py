import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import inspect
import logging



@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresence(self, text_verify):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text_verify))).click()

    def insert_name(self, name):
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div[1]/div[3]/div/form/input[1]").send_keys(
            name)

    def insert_surname(self, surname):
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div[1]/div[3]/div/form/input[2]").send_keys(
            surname)

    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        # filehandler object in whhich file I have to print???  WHat FORMAT and what FILE??
        fileHandler = logging.FileHandler('logfile.log')
        logger.addHandler(fileHandler)

        # format to print
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        # setting level (to filter types of alerts below and display e.g a selection of types of logs)
        # changing logger.setLevel(logging.ERROR) can supress some of the logs
        # only loggs higher or equal to error will be displayed
        logger.setLevel(logging.DEBUG)
        return logger



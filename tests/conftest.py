import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="edge"
    )

# --browser_name chrome ==> cmd line to use spcific browser

@pytest.fixture(scope="class")
def setup(request):
    # this line below will pass browser_name value from cmd terminal
    browser_name = request.config.getoption("browser_name")
    if browser_name == "edge":
        # edge invocation
        service_obj = Service("C:/Users/Marcin/Desktop/webdriver/msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    elif browser_name == "chrome":
        # chrome invocation
        service_obj = Service("C:/Users/Marcin/Desktop/chrome_webdriver/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    else:
        print("some other browsers")

    # driver will be sent to class object and assigned to cls
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver

    yield
    # yield oznacza że wszystko co bedzie pod spodem zostanie wykonane na
    # końcu teardown
    driver.close()

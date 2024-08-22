import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def setup(driver):
    #driver = webdriver.Chrome()
    driver.get("http://13.126.167.255:8088/")
    #driver.maximize_window()
    #driver.implicitly_wait(5)
    yield driver
    #driver.quit()


@pytest.fixture
def prod_setup(driver):
    #driver = webdriver.Chrome()
    #driver.implicitly_wait(5)
    driver.get("http://13.126.167.255:8088/products")
    #driver.maximize_window()
    yield driver
    #driver.quit()



@pytest.fixture(scope="session")

def navigate(driver):

    def _navigate(url):
        driver.get(url)
    return _navigate

@pytest.fixture(scope='session')
def base_url():
    return "http://13.126.167.255:8088"

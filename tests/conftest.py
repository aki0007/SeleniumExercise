import pytest

from base.webdriver import WebDriver


@pytest.fixture(scope="session")
def driver():
    driver = WebDriver()
    return driver


@pytest.fixture(scope="session")
def close_driver(driver):
    yield
    driver.quit()

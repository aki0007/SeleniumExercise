import pytest

from base.webdriver import WebDriver


@pytest.fixture(scope="session")
def driver():
    driver = WebDriver()
    yield driver

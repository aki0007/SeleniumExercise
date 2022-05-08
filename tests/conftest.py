from typing import Iterator

from pytest import fixture

from config import conf_obj, get_driver_options
from base.webdriver import WebDriver


@fixture(scope="session", autouse=False)
def wp() -> Iterator[WebDriver]:
    # Define all the classes
    driver_options = get_driver_options()
    if not conf_obj.LOCAL:
        driver_options.add_argument("--headless")
        driver_options.add_argument("--no-sandbox")
        driver_options.add_argument("--disable-gpu")

    driver = WebDriver(options=driver_options)
    try:
        yield driver
    finally:
        driver.close()

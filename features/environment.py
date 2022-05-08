import os
from typing import Iterator

from config import conf_obj, get_driver_options
from base.webdriver import WebDriver
from base.pom.login import LoginPage
from base.pom.register import RegisterPage
from base.pom.generate_user import GenerateUserPage
from base.pom.manage_customer import ManageCustomerPage
from base.pom.navigation import NavigationPage


def wp() -> Iterator[WebDriver]:
    # Define all the classes
    driver_options = get_driver_options()
    if not conf_obj.LOCAL:
        driver_options.add_argument("--headless")
        driver_options.add_argument("--no-sandbox")
        driver_options.add_argument("--disable-gpu")

    return WebDriver(options=driver_options)


def before_all(context) -> None:
    # Create a screenshot path if it does not exist
    if not os.path.exists(conf_obj.SCREENSHOT_PATH):
        os.makedirs(conf_obj.SCREENSHOT_PATH)

    context.driver = WebDriver()
    context.login_page = LoginPage(context.driver)
    context.register_page = RegisterPage(context.driver)
    context.generate_user_page = GenerateUserPage(context.driver)
    context.manage_customer_page = ManageCustomerPage(context.driver)
    context.navigation_page = NavigationPage(context.driver)


def after_all(context) -> None:
    context.driver.quit()

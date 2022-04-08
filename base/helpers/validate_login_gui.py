import allure

from base.data import LOGIN_DATA
from base.locators import Locators
from base.webdriver import WebDriver


@allure.step
def validate_login(driver: WebDriver) -> None:
    # Validate successful login
    driver.check_if_element_exists(
        Locators.VALIDATE_SUCCESSFUL_LOGIN.format(username=LOGIN_DATA["username"])
    )


@allure.step
def validate_random_user(driver: WebDriver) -> None:
    assert driver.check_if_element_exists(
        Locators.VALIDATE_GENERATED_USER
    ), "validate_random_user(): Generated user not displayed"

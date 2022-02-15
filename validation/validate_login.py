import allure

from library.locators import Locators
from library.data import login_data


@allure.step
def validate_login(driver):
    # Validate successful login
    driver.check_if_element_exists(Locators.VALIDATE_SUCCESSFUL_LOGIN.format(username=login_data["username"]))


@allure.step
def validate_random_user(driver):
    # driver.wait_for_loader_to_load(Locators.LOADING_LOADER)
    assert driver.check_if_element_exists(Locators.VALIDATE_GENERATED_USER), \
        "validate_random_user(): Generated user not displayed"


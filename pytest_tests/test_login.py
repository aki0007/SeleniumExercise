import pytest
from config.config_reader import read_config_data
from helpers.login_helper import *
from validation.validate_login import *


@pytest.mark.register
def test_register_new_user(driver, close_driver):
    # Navigate to page
    driver.set_window(read_config_data("Details", "URL"))
    # Set personal data information
    set_registration_personal_details(driver)
    # Set information from dropdowns
    select_register_dropdown_options(driver)
    # Accept terms and conditions
    accept_terms_and_conditions(driver)
    # Click on sign up button
    click_sign_up_button(driver)
    time.sleep(2)


@pytest.mark.login
def test_login(driver, close_driver):
    # Navigate to page
    driver.set_window(read_config_data("Details", "URL"))
    # Login to page
    login_with_username_and_password(driver)
    # Validate login
    validate_login(driver)
    time.sleep(2)


@pytest.mark.login
@pytest.mark.generate_user
def test_generate_user(driver, close_driver):
    # Navigate to page
    driver.set_window(read_config_data("Details", "URL"))
    # Login to page
    login_with_username_and_password(driver)
    # Validate login
    validate_login(driver)
    # Get random user
    get_random_user(driver)
    # Validate random user
    validate_random_user(driver)
    driver.take_screenshot()
    time.sleep(2)

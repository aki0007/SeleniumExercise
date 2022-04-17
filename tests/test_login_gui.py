import time
import pytest

from base.helpers.login_gui import (
    accept_terms_and_conditions,
    click_sign_up_button,
    get_random_user,
    login_with_username_and_password,
    select_register_dropdown_options,
    set_registration_personal_details,
)
from base.helpers.validate_login_gui import validate_login, validate_random_user


@pytest.mark.register
def test_register_new_user(driver):
    # Navigate to page
    driver.set_window()
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
def test_login(driver):
    # Navigate to page
    driver.set_window()
    # Login to page
    login_with_username_and_password(driver)
    # Validate login
    validate_login(driver)
    time.sleep(2)


@pytest.mark.login
@pytest.mark.generate_user
def test_generate_user(driver):
    # Navigate to page
    driver.set_window()
    # Login to page
    login_with_username_and_password(driver)
    # Validate login
    validate_login(driver)
    # Get random user
    get_random_user(driver)
    # Validate random user
    validate_random_user(driver)
    # Take SS from gui
    driver.take_screenshot()
    time.sleep(2)

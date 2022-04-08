import logging

import allure
from behave import given, then, when
from behave.runner import Context

from base.locators import Locators
from config import config
from tests.helpers.login_helper import (
    accept_terms_and_conditions,
    click_sign_up_button,
    get_random_user,
    login_with_username_and_password,
    select_register_dropdown_options,
    set_registration_personal_details,
)
from tests.validation.validate_login import validate_login, validate_random_user

logging.basicConfig()


@allure.step
@given("Navigate to testing page")
def navigate_to_page_step(context: Context) -> None:
    context.driver.set_window()


@allure.step
@when("Send registration params")
def send_registration_params_step(context: Context) -> None:
    # Set personal data information
    set_registration_personal_details(context.driver)
    # Set information from dropdowns
    select_register_dropdown_options(context.driver)
    # Accept terms and conditions
    accept_terms_and_conditions(context.driver)
    # Click on sign up button
    click_sign_up_button(context.driver)


@allure.step
@when('Login to page with username "{username}" and password "{password}"')
def login_to_page_step(context: Context, username: str, password: str) -> None:
    username = username if username != "None" else config.LOGIN_USERNAME
    password = password if password != "None" else config.LOGIN_PASSWORD

    # Login with username and password
    login_with_username_and_password(context.driver, username, password)


@allure.step
@then("Validate successful login")
def validate_login_step(context: Context) -> None:
    # Validate login
    validate_login(context.driver)


@allure.step
@when("Create random user")
def get_random_user_step(context: Context) -> None:
    # Get random user
    get_random_user(context.driver)


@allure.step
@then("Validate if random user is generated successfully")
def validate_random_user_step(context: Context) -> None:
    # Validate random user
    validate_random_user(context.driver)


@allure.step
@then("Take screenshot")
def take_screenshot_step(context: Context) -> None:
    context.driver.take_screenshot()


@allure.step
@when('Navigate to "{tab}", "{sub_tab}" in navigation tab')
def navigation_tab_step(context: Context, tab: str, sub_tab: str) -> None:
    # Get random user
    context.driver.get_element(Locators.NAVIGATION_TAB.format(tab=tab)).click()
    context.driver.get_element(Locators.SUB_NAVIGATION_TAB.format(tab=sub_tab)).click()


@allure.step
@when('Click on "{text}" button')
def click_on_button_step(context: Context, text: str) -> None:
    # Get random user
    context.driver.get_element(Locators.GENERAL_BUTTON.format(text=text)).click()


@allure.step
@then("Wait for progress loader to load")
def wait_for_progress_loader_to_load(context: Context) -> None:
    context.driver.wait_for_loader_to_load(Locators.PROGRESS_LOADER)


@allure.step
@then("Validate successful download")
def validate_successful_download(context: Context) -> None:
    if not context.driver.check_if_element_exists(Locators.PROGRESS_COMPLETE):
        assert False, "validate_successful_download(): Complete message not displayed"

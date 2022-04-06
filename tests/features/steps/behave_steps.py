from behave import *
import logging

from base.locators import Locators
from base.utils import read_config_data
from tests.helpers.login_helper import (
    set_registration_personal_details,
    select_register_dropdown_options,
    accept_terms_and_conditions,
    click_sign_up_button,
    login_with_username_and_password,
    get_random_user
)
from tests.validation.validate_login import validate_login, validate_random_user

logging.basicConfig()


@given(u'Navigate to testing page')
def navigate_to_page_step(context):
    context.driver.set_window(read_config_data("Details", "URL"))


@when(u'Send registration params')
def send_registration_params_step(context):
    # Set personal data information
    set_registration_personal_details(context.driver)
    # Set information from dropdowns
    select_register_dropdown_options(context.driver)
    # Accept terms and conditions
    accept_terms_and_conditions(context.driver)
    # Click on sign up button
    click_sign_up_button(context.driver)


@when(u'Login to page with username "{username}" and password "{password}"')
def login_to_page_step(context, username, password):
    username = None if username == "None" else username
    password = None if password == "None" else password

    # Login with username and password
    login_with_username_and_password(context.driver, username, password)


@then(u'Validate successful login')
def validate_login_step(context):
    # Validate login
    validate_login(context.driver)


@when(u'Create random user')
def get_random_user_step(context):
    # Get random user
    get_random_user(context.driver)


@then(u'Validate if random user is generated successfully')
def validate_random_user_step(context):
    # Validate random user
    validate_random_user(context.driver)


@then(u'Take screenshot')
def take_screenshot_step(context):
    context.driver.take_screenshot()


@when(u'Navigate to "{tab}", "{sub_tab}" in navigation tab')
def navigation_tab_step(context, tab, sub_tab):
    # Get random user
    context.driver.get_element(Locators.NAVIGATION_TAB.format(tab=tab)).click()
    context.driver.get_element(Locators.SUB_NAVIGATION_TAB.format(tab=sub_tab)).click()


@when(u'Click on "{text}" button')
def click_on_button_step(context, text):
    # Get random user
    context.driver.get_element(Locators.GENERAL_BUTTON.format(text=text)).click()


@then(u'Wait for progress loader to load')
def take_screenshot_step(context):
    context.driver.wait_for_loader_to_load(Locators.PROGRESS_LOADER)


@then(u'Validate successful download')
def take_screenshot_step(context):
    if not context.driver.check_if_element_exists(Locators.PROGRESS_COMPLETE):
        assert False, "take_screenshot_step(): Complete message not displayed"

import logging

import allure
from behave import given, then, when
from behave.runner import Context


logging.basicConfig()


@allure.step
@given("Navigate to testing page")
def navigate_to_page_step(context: Context) -> None:
    context.login_page.set_up_window()


@allure.step
@when('Login to page with username "{username}" and password "{password}"')
def login_to_page_step(context: Context, username: str, password: str) -> None:
    # Login with username and password
    context.login_page.login_with_username_and_password(username, password)


@allure.step
@then("Validate successful login")
def validate_login_step(context: Context) -> None:
    # Validate login
    context.login_page.validate_login()


@allure.step
@when("Create random user")
def get_random_user_step(context: Context) -> None:
    # Get random user
    context.generate_user_page.get_random_user()


@allure.step
@then("Validate if random user is generated successfully")
def validate_random_user_step(context: Context) -> None:
    # Validate random user
    context.generate_user_page.validate_random_user()


@allure.step
@when('Navigate to "{tab}", "{sub_tab}" in navigation tab')
def navigation_tab_step(context: Context, tab: str, sub_tab: str) -> None:
    # Get random user
    context.navigation_page.navigation_tab_step(tab, sub_tab)


@allure.step
@when('Start download')
def start_download_step(context: Context) -> None:
    context.manage_customer_page.start_download()


@allure.step
@then("Wait for progress loader to load")
def wait_for_progress_loader_to_load(context: Context) -> None:
    context.manage_customer_page.wait_for_progress_loader_to_load()


@allure.step
@then("Validate successful download")
def validate_successful_download(context: Context) -> None:
    context.manage_customer_page.validate_successful_download()


@allure.step
@then('Close button')
def close_button_step(context: Context) -> None:
    context.manage_customer_page.close_button()

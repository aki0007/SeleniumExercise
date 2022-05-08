import time
import pytest

from base.pom.login import LoginPage
from base.pom.register import RegisterPage
from base.pom.generate_user import GenerateUserPage


@pytest.mark.register
def test_register_new_user(wp):
    # Navigate to page
    register_page: RegisterPage = RegisterPage(wp)
    register_page.set_up_window()
    # Set personal data information
    register_page.set_registration_personal_details()
    # Set information from dropdowns
    register_page.select_register_dropdown_options()
    # Accept terms and conditions
    register_page.accept_terms_and_conditions()
    # Click on sign up button
    register_page.click_sign_up_button()
    time.sleep(2)


@pytest.mark.login
def test_login(wp) -> None:
    # Login to page
    login_page: LoginPage = LoginPage(wp)
    login_page.set_up_window()
    login_page.login_with_username_and_password()
    # Validate login
    login_page.validate_login()
    time.sleep(2)


@pytest.mark.login
@pytest.mark.generate_user
@pytest.mark.test1
def test_generate_user(wp):
    login_page: LoginPage = LoginPage(wp)
    generate_user_page: GenerateUserPage = GenerateUserPage(wp)
    # Navigate to page
    login_page.set_up_window()
    # Login to page
    login_page.login_with_username_and_password()
    # Validate login
    login_page.validate_login()
    # Get random user
    generate_user_page.get_random_user()
    # Validate random user
    generate_user_page.validate_random_user()


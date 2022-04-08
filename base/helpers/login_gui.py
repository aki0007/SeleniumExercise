import time
from typing import Optional

import allure

from base.data import LOGIN_DATA, REGISTER_DATA
from base.enums import HomeTab, NavigationTab
from base.locators import Locators
from base.webdriver import WebDriver
from base.helpers.utils import select_date


@allure.step
def login_with_username_and_password(
    driver: WebDriver, username: Optional[str] = None, password: Optional[str] = None
) -> None:
    # Check if user is already login
    if not driver.check_if_element_exists(Locators.LOGIN_BUTTON):
        return

    # Choose default username and password if they are not defined
    username = LOGIN_DATA["username"] if not username else username
    password = LOGIN_DATA["password"] if not password else password

    # Click on Login tab
    driver.get_element(Locators.LOGIN_TAB).click()
    # Set username, email and password
    driver.safe_send_keys(username, Locators.LOGIN_USERNAME)
    driver.safe_send_keys(password, Locators.LOGIN_PASSWORD)
    # Click on "Keep me logged in"
    driver.get_element(Locators.LOGIN_KEEP_ME_LOGGED_IN).click()
    driver.get_element(Locators.LOGIN_BUTTON).click()


@allure.step
def set_registration_personal_details(driver: WebDriver) -> None:
    # Set username, email and password
    driver.safe_send_keys(REGISTER_DATA["username"], Locators.REGISTRATION_USERNAME)
    driver.safe_send_keys(REGISTER_DATA["email"], Locators.REGISTRATION_EMAIL)
    driver.safe_send_keys(REGISTER_DATA["password"], Locators.REGISTRATION_PASSWORD)
    driver.safe_send_keys(
        REGISTER_DATA["password"], Locators.REGISTRATION_CONFIRM_PASSWORD
    )
    # Set date
    select_date(driver, REGISTER_DATA["dob"])
    # Set phone, address, address type
    driver.safe_send_keys(REGISTER_DATA["phone"], Locators.REGISTRATION_PHONE)
    driver.safe_send_keys(REGISTER_DATA["address"], Locators.REGISTRATION_ADDRESS)


@allure.step
def select_register_dropdown_options(driver: WebDriver) -> None:
    driver.get_element(
        Locators.REGISTRATION_ADDRESS_TYPE.format(
            address_type=REGISTER_DATA["address_type"][0]
        ),
        highlight=False,
    ).click()
    # Set gender, country, state and city
    driver.select_from_dropdown(Locators.REGISTRATION_GENDER, REGISTER_DATA["gender"])
    driver.select_from_dropdown(Locators.REGISTRATION_COUNTRY, REGISTER_DATA["country"])
    # Page requires 3 seconds sleep
    time.sleep(3.5)
    driver.select_from_dropdown(Locators.REGISTRATION_STATE, REGISTER_DATA["state"])
    time.sleep(3.5)
    driver.select_from_dropdown(Locators.REGISTRATION_CITY, REGISTER_DATA["city"])
    driver.safe_send_keys(REGISTER_DATA["address"], Locators.REGISTRATION_ZIP_CODE)


@allure.step
def accept_terms_and_conditions(driver: WebDriver) -> None:
    # Accept terms and conditions
    driver.get_element(Locators.REGISTRATION_TERMS_AND_CONDITIONS).click()


@allure.step
def click_sign_up_button(driver: WebDriver) -> None:
    driver.get_element(Locators.SIGN_UP_BUTTON).click()


@allure.step
def get_random_user(driver: WebDriver) -> None:
    # Navigate to get random user
    driver.hover_element(Locators.NAVIGATION_TAB.format(tab=NavigationTab.HOME.value))
    driver.get_element(
        Locators.SUB_NAVIGATION_TAB.format(tab=HomeTab.GENERATE_USER.value)
    ).click()
    driver.get_element(Locators.GET_NEW_USER_BUTTON).click()

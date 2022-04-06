import allure
import time

from base.enums import NavigationTab, HomeTab
from base.locators import Locators
from base.data import register_data, login_data
from tests.features.helpers.utils import select_date


@allure.step
def login_with_username_and_password(driver, username=None, password=None):
    # Check if user is already login
    if not driver.check_if_element_exists(Locators.LOGIN_BUTTON):
        return

    # Choose default username and password if they are not defined
    username = login_data["username"] if not username else username
    password = login_data["password"] if not password else password

    # Click on Login tab
    driver.get_element(Locators.LOGIN_TAB).click()
    # Set username, email and password
    driver.safe_send_keys(username, Locators.LOGIN_USERNAME)
    driver.safe_send_keys(password, Locators.LOGIN_PASSWORD)
    # Click on "Keep me logged in"
    driver.get_element(Locators.LOGIN_KEEP_ME_LOGGED_IN).click()
    driver.get_element(Locators.LOGIN_BUTTON).click()


@allure.step
def set_registration_personal_details(driver):
    # Set username, email and password
    driver.safe_send_keys(register_data["username"], Locators.REGISTRATION_USERNAME)
    driver.safe_send_keys(register_data["email"], Locators.REGISTRATION_EMAIL)
    driver.safe_send_keys(register_data["password"], Locators.REGISTRATION_PASSWORD)
    driver.safe_send_keys(register_data["password"], Locators.REGISTRATION_CONFIRM_PASSWORD)
    # Set date
    select_date(driver, register_data["dob"])
    # Set phone, address, address type
    driver.safe_send_keys(register_data["phone"], Locators.REGISTRATION_PHONE)
    driver.safe_send_keys(register_data["address"], Locators.REGISTRATION_ADDRESS)


@allure.step
def select_register_dropdown_options(driver):
    driver.get_element(Locators.REGISTRATION_ADDRESS_TYPE.format(address_type=register_data["address_type"][0]),
                       highlight=False).click()
    # Set gender, country, state and city
    driver.select_from_dropdown(Locators.REGISTRATION_GENDER, register_data["gender"])
    driver.select_from_dropdown(Locators.REGISTRATION_COUNTRY, register_data["country"])
    # Page requires 3 seconds sleep
    time.sleep(3.5)
    driver.select_from_dropdown(Locators.REGISTRATION_STATE, register_data["state"])
    time.sleep(3.5)
    driver.select_from_dropdown(Locators.REGISTRATION_CITY, register_data["city"])
    driver.safe_send_keys(register_data["address"], Locators.REGISTRATION_ZIP_CODE)


@allure.step
def accept_terms_and_conditions(driver):
    # Accept terms and conditions
    driver.get_element(Locators.REGISTRATION_TERMS_AND_CONDITIONS).click()


@allure.step
def click_sign_up_button(driver):
    driver.get_element(Locators.SIGN_UP_BUTTON).click()


@allure.step
def get_random_user(driver):
    # Navigate to get random user
    driver.hover_element(Locators.NAVIGATION_TAB.format(tab=NavigationTab.HOME.value))
    driver.get_element(Locators.SUB_NAVIGATION_TAB.format(tab=HomeTab.GENERATE_USER.value)).click()
    driver.get_element(Locators.GET_NEW_USER_BUTTON).click()

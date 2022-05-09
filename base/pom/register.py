import allure
from datetime import datetime
import time
from typing import Sequence


from base.webdriver import WebDriver
from base.data import REGISTER_DATA
from base.helpers.utils import calculate_number_of_clicks


class RegisterPage:
    __CALENDAR_LEFT_ARROW: str = "//a[@data-handler='prev']"
    __CALENDAR_SELECT_DATE: str = "//td[@data-handler='selectDay']//a[text()='{date}']"
    __REGISTRATION_USERNAME: str = "//input[@placeholder='myusername']"
    __REGISTRATION_EMAIL: str = "//input[@name='fld_email']"
    __REGISTRATION_PASSWORD: str = "//input[@placeholder='Password']"
    __REGISTRATION_CONFIRM_PASSWORD: str = "//input[@placeholder='Confirm password']"
    __REGISTRATION_DOB: str = "//input[@placeholder='Date of birth']"
    __REGISTRATION_PHONE: str = "//input[@placeholder='Phone']"
    __REGISTRATION_ADDRESS: str = "//input[@placeholder='Address']"
    __REGISTRATION_ADDRESS_TYPE: str = "//input[@name='add_type' and @value='{address_type}']"
    __REGISTRATION_GENDER: str = "//select[@name='sex']"
    __REGISTRATION_COUNTRY: str = "//select[@name='country']"
    __REGISTRATION_STATE: str = "//select[@name='state']"
    __REGISTRATION_CITY: str = "//select[@name='city']"
    __REGISTRATION_ZIP_CODE: str = "//input[@name='zip']"
    __REGISTRATION_TERMS_AND_CONDITIONS: str = (
        "//em[text()='I agree with terms and conditions ']/preceding-sibling::input"
    )
    __SIGN_UP_BUTTON: str = "//input[@value='Sign up']"

    def __init__(self, driver) -> None:
        # It is necessary to initialise driver as page class member to implement Webdriver
        self.driver: WebDriver = driver

    @allure.step
    def set_up_window(self) -> None:
        self.driver.set_window()

    @allure.step
    def set_registration_personal_details(self) -> None:
        # Set username, email and password
        self.driver.safe_send_keys(self.__REGISTRATION_USERNAME, REGISTER_DATA["username"])
        self.driver.safe_send_keys(self.__REGISTRATION_EMAIL, REGISTER_DATA["email"])
        self.driver.safe_send_keys(self.__REGISTRATION_PASSWORD, REGISTER_DATA["password"])
        self.driver.safe_send_keys(
            self.__REGISTRATION_CONFIRM_PASSWORD, REGISTER_DATA["password"]
        )
        # Set date
        self.select_date(REGISTER_DATA["dob"])
        # Set phone, address, address type
        self.driver.safe_send_keys(self.__REGISTRATION_PHONE, REGISTER_DATA["phone"])
        self.driver.safe_send_keys(self.__REGISTRATION_ADDRESS, REGISTER_DATA["address"])

    @allure.step
    def select_date(self, date: Sequence[str]) -> None:
        # Open calendar
        self.driver.get_element(self.__REGISTRATION_DOB).click()
        date_obj: datetime = datetime.strptime(str(date), "%d %B %Y")

        # Fetch how many times left calendar arrow needs to be clicked
        number_of_clicks: int = calculate_number_of_clicks(date_obj)
        # Select correct month and year
        self.select_year_and_month_on_calendar(number_of_clicks)
        self.driver.get_element(self.__CALENDAR_SELECT_DATE.format(date=date_obj.day)).click()

    def select_year_and_month_on_calendar(self, number_of_clicks: int) -> None:
        for _ in range(number_of_clicks):
            self.driver.get_element(self.__CALENDAR_LEFT_ARROW).click()

    @allure.step
    def select_register_dropdown_options(self) -> None:
        self.driver.get_element(
            self.__REGISTRATION_ADDRESS_TYPE.format(
                address_type=REGISTER_DATA["address_type"][0]
            ),
            highlight=False,
        ).click()
        # Set gender, country, state and city
        self.driver.select_from_dropdown_by_value(self.__REGISTRATION_GENDER, REGISTER_DATA["gender"])
        self.driver.select_from_dropdown_by_value(self.__REGISTRATION_COUNTRY, REGISTER_DATA["country"])
        # Page requires 3 seconds sleep
        time.sleep(3.5)
        self.driver.select_from_dropdown_by_value(self.__REGISTRATION_STATE, REGISTER_DATA["state"])
        time.sleep(3.5)
        self.driver.select_from_dropdown_by_value(self.__REGISTRATION_CITY, REGISTER_DATA["city"])
        self.driver.safe_send_keys(self.__REGISTRATION_ZIP_CODE, REGISTER_DATA["address"])

    @allure.step
    def accept_terms_and_conditions(self) -> None:
        # Accept terms and conditions
        self.driver.get_element(self.__REGISTRATION_TERMS_AND_CONDITIONS).click()

    @allure.step
    def click_sign_up_button(self) -> None:
        self.driver.get_element(self.__SIGN_UP_BUTTON).click()

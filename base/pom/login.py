import allure
from typing import Optional

from base.webdriver import WebDriver
from base.data import LOGIN_DATA


class LoginPage(object):
    def __init__(self, driver) -> None:
        # It is necessary to initialise driver as page class member to implement Webdriver
        self.driver: WebDriver = driver

    # Locators
    LOGIN_TAB: str = "//li[descendant::input[@id='tab2']]"
    LOGIN_USERNAME: str = "//input[@placeholder='Username']"
    LOGIN_PASSWORD: str = "//input[@placeholder='mypassword']"
    LOGIN_KEEP_ME_LOGGED_IN: str = (
            "//em[text()='Keep me logged in ']/preceding-sibling::input"
        )
    LOGIN_BUTTON: str = "//input[@value='Login']"
    VALIDATE_SUCCESSFUL_LOGIN: str = "//*[text() = ' Welcome Mr. {username}']"

    @allure.step
    def set_up_window(self) -> None:
        self.driver.set_window()

    @allure.step
    def login_with_username_and_password(
            self, username: Optional[str] = None, password: Optional[str] = None
    ) -> None:
        # Check if user is already login
        if not self.driver.check_if_element_exists(self.LOGIN_BUTTON):
            return

        # Choose default username and password if they are not defined
        username: str = LOGIN_DATA["username"] if not username else username
        password: str = LOGIN_DATA["password"] if not password else password

        # Click on Login tab
        self.driver.get_element(self.LOGIN_TAB).click()
        # Set username, email and password
        self.driver.safe_send_keys(self.LOGIN_USERNAME, username)
        self.driver.safe_send_keys(self.LOGIN_PASSWORD, password)
        # Click on "Keep me logged in"
        self.driver.get_element(self.LOGIN_KEEP_ME_LOGGED_IN).click()
        self.driver.get_element(self.LOGIN_BUTTON).click()

    @allure.step
    def validate_login(self) -> None:
        # Validate successful login
        self.driver.check_if_element_exists(
            self.VALIDATE_SUCCESSFUL_LOGIN.format(username=LOGIN_DATA["username"])
        )

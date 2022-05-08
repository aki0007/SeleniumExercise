import allure
from typing import Optional

from base.webdriver import WebDriver
from selenium.webdriver import Chrome
from base.data import LOGIN_DATA


class LoginPage(WebDriver):
    def __init__(self):
        self.driver: Chrome = super().__init__(WebDriver)
        # Locators
        self.LOGIN_TAB: str = "//li[descendant::input[@id='tab2']]"
        self.LOGIN_USERNAME: str = "//input[@placeholder='Username']"
        self.LOGIN_PASSWORD: str = "//input[@placeholder='mypassword']"
        self.LOGIN_KEEP_ME_LOGGED_IN: str = (
            "//em[text()='Keep me logged in ']/preceding-sibling::input"
        )
        self.LOGIN_BUTTON: str = "//input[@value='Login']"

    @allure.step
    def login_with_username_and_password(
            self, username: Optional[str] = None, password: Optional[str] = None
    ) -> None:
        # Check if user is already login
        if not self.driver.check_if_element_exists(self.LOGIN_BUTTON):
            return

        # Choose default username and password if they are not defined
        username = LOGIN_DATA["username"] if not username else username
        password = LOGIN_DATA["password"] if not password else password

        # Click on Login tab
        self.driver.get_element(self.LOGIN_TAB).click()
        # Set username, email and password
        self.driver.safe_send_keys(username, self.LOGIN_USERNAME)
        self.driver.safe_send_keys(password, self.LOGIN_PASSWORD)
        # Click on "Keep me logged in"
        self.driver.get_element(self.LOGIN_KEEP_ME_LOGGED_IN).click()
        self.driver.get_element(self.LOGIN_BUTTON).click()
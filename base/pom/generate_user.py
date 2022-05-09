import allure
import time

from base.webdriver import WebDriver
from base.enums import HomeTab, NavigationTab


class GenerateUserPage:
    __GET_NEW_USER_BUTTON: str = "//button[text()='Get New User']"
    __NAVIGATION_TAB: str = "//li[descendant::a[contains(text(), '{tab}')]]"

    __SUB_NAVIGATION_TAB: str = (
        "//ul[@class='dropdown-menu']//li[descendant::a[contains(text(), '{tab}')]]"
    )
    __VALIDATE_GENERATED_USER: str = "//div[contains(text(), 'First Name')]"

    def __init__(self, driver) -> None:
        # It is necessary to initialise driver as page class member to implement Webdriver
        self.driver: WebDriver = driver

    @allure.step
    def get_random_user(self) -> None:
        # Navigate to get random user
        self.driver.hover_element(self.__NAVIGATION_TAB.format(tab=NavigationTab.HOME.value))
        self.driver.get_element(
            self.__SUB_NAVIGATION_TAB.format(tab=HomeTab.GENERATE_USER.value)
        ).click()
        self.driver.get_element(self.__GET_NEW_USER_BUTTON).click()

    @allure.step
    def validate_random_user(self) -> None:
        self.driver.c_assert(self.driver.check_if_element_exists(
            self.__VALIDATE_GENERATED_USER
        ))
        time.sleep(2)

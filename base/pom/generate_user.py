import allure
import time

from base.webdriver import WebDriver
from base.enums import HomeTab, NavigationTab


class GenerateUserPage(object):
    def __init__(self, driver):
        # It is necessary to initialise driver as page class member to implement Webdriver
        self.driver: WebDriver = driver

    GET_NEW_USER_BUTTON = "//button[text()='Get New User']"
    NAVIGATION_TAB = "//li[descendant::a[contains(text(), '{tab}')]]"

    SUB_NAVIGATION_TAB = (
        "//ul[@class='dropdown-menu']//li[descendant::a[contains(text(), '{tab}')]]"
    )
    VALIDATE_GENERATED_USER = "//div[contains(text(), 'First Name')]"

    @allure.step
    def get_random_user(self) -> None:
        # Navigate to get random user
        self.driver.hover_element(self.NAVIGATION_TAB.format(tab=NavigationTab.HOME.value))
        self.driver.get_element(
            self.SUB_NAVIGATION_TAB.format(tab=HomeTab.GENERATE_USER.value)
        ).click()
        self.driver.get_element(self.GET_NEW_USER_BUTTON).click()

    @allure.step
    def validate_random_user(self) -> None:
        self.driver.c_assert(self.driver.check_if_element_exists(
            self.VALIDATE_GENERATED_USER
        ))
        time.sleep(2)

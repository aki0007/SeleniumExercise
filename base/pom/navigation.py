import allure

from base.webdriver import WebDriver


class NavigationPage:
    def __init__(self, driver) -> None:
        # It is necessary to initialise driver as page class member to implement Webdriver
        self.driver: WebDriver = driver

    __NAVIGATION_TAB: str = "//li[descendant::a[contains(text(), '{tab}')]]"
    __SUB_NAVIGATION_TAB: str = (
        "//ul[@class='dropdown-menu']//li[descendant::a[contains(text(), '{tab}')]]"
    )

    @allure.step
    def navigation_tab_step(self, tab: str, sub_tab: str) -> None:
        # Get random user
        self.driver.get_element(self.__NAVIGATION_TAB.format(tab=tab)).click()
        self.driver.get_element(self.__SUB_NAVIGATION_TAB.format(tab=sub_tab)).click()

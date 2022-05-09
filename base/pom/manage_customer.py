import allure

from base.webdriver import WebDriver


class ManageCustomerPage:
    __CLOSE_DOWNLOAD_BUTTON: str = "//button[text()='Close']"
    __START_DOWNLOAD_BUTTON: str = "//button[text()='Start Download']"
    __PROGRESS_LOADER: str = "//div[contains(text(), 'Current Progress')]"
    __PROGRESS_COMPLETE: str = "//div[text()='Complete!']"

    def __init__(self, driver) -> None:
        # It is necessary to initialise driver as page class member to implement Webdriver
        self.driver: WebDriver = driver

    @allure.step
    def start_download(self) -> None:
        self.driver.get_element(self.__START_DOWNLOAD_BUTTON).click()

    @allure.step
    def close_button(self) -> None:
        self.driver.get_element(self.__CLOSE_DOWNLOAD_BUTTON).click()

    @allure.step
    def wait_for_progress_loader_to_load(self) -> None:
        self.driver.wait_for_loader_to_load(self.__PROGRESS_LOADER)

    @allure.step
    def validate_successful_download(self) -> None:
        self.driver.c_assert(self.driver.check_if_element_exists(self.__PROGRESS_COMPLETE))

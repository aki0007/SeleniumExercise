import allure

from base.webdriver import WebDriver


class ManageCustomerPage(object):
    def __init__(self, driver):
        # It is necessary to initialise driver as page class member to implement Webdriver
        self.driver: WebDriver = driver

    CLOSE_DOWNLOAD_BUTTON: str = "//button[text()='Close']"
    START_DOWNLOAD_BUTTON: str  = "//button[text()='Start Download']"
    PROGRESS_LOADER: str = "//div[contains(text(), 'Current Progress')]"
    PROGRESS_COMPLETE: str = "//div[text()='Complete!']"

    @allure.step
    def start_download(self) -> None:
        self.driver.get_element(self.START_DOWNLOAD_BUTTON).click()

    @allure.step
    def close_button(self) -> None:
        self.driver.get_element(self.CLOSE_DOWNLOAD_BUTTON).click()

    @allure.step
    def wait_for_progress_loader_to_load(self) -> None:
        self.driver.wait_for_loader_to_load(self.PROGRESS_LOADER)

    @allure.step
    def validate_successful_download(self) -> None:
        self.driver.c_assert(self.driver.check_if_element_exists(self.PROGRESS_COMPLETE))


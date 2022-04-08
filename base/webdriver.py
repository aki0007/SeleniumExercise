from datetime import datetime
from typing import Sequence

from selenium.common.exceptions import ElementNotInteractableException, TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from config import config


class WebDriver(Chrome):
    def set_window(self) -> None:
        self.get(config.GLOBAL_URL + config.TESTING_URL)
        self.maximize_window()

    def get_element(self, locator: str, clickable: bool = True, highlight: bool = True):
        try:
            # Wait until element is clickable
            if clickable:
                WebDriverWait(self, 5).until(
                    EC.element_to_be_clickable((By.XPATH, locator))
                )

            # Wait until element is clickable
            element: WebElement = WebDriverWait(self, 5).until(
                EC.presence_of_element_located((By.XPATH, locator))
            )

            # Highlight element
            if highlight:
                self.execute_script(
                    "arguments[0].setAttribute('style', 'background: yellow;');",
                    element,
                )

            return self.find_element(By.XPATH, locator)

        except ElementNotInteractableException:
            return self.find_element(By.XPATH, locator)

    def safe_send_keys(self, input_text: Sequence[str], locator: str) -> None:
        self.get_element(locator).click()
        action: ActionChains = ActionChains(self)
        action.send_keys(input_text)
        action.perform()

    def select_from_dropdown(self, locator: str, dropdown_menu: Sequence[str]) -> None:
        select: Select = Select(self.get_element(locator))
        select.select_by_value(dropdown_menu)

    def check_if_element_exists(self, locator: str) -> bool:
        try:
            WebDriverWait(self, 5).until(
                EC.presence_of_element_located((By.XPATH, locator))
            )
        except TimeoutException:
            return False
        return True

    def hover_element(self, locator: str) -> None:
        element: WebElement = self.get_element(locator)
        hover: ActionChains = ActionChains(self).move_to_element(to_element=element)
        hover.perform()

    def wait_for_loader_to_load(self, locator) -> None:
        try:
            # wait for loading element to appear
            # - required to prevent prematurely checking if element
            #   has disappeared, before it has had a chance to appear
            WebDriverWait(self, 20).until(
                EC.presence_of_element_located((By.XPATH, locator))
            )
            self.get_element(locator)
            # then wait for the element to disappear
            WebDriverWait(self, 20).until_not(
                EC.presence_of_element_located((By.XPATH, locator))
            )

        except TimeoutException:
            # if timeout exception was raised - it may be safe to
            # assume loading has finished, however this may not
            # always be the case, use with caution, otherwise handle
            # appropriately.
            assert False, "wait_for_loader_to_load(): TimeoutException"

    def take_screenshot(self) -> None:
        """
        Take screenshot and save it to reports/screenshot/current_date folder
        """
        screenshot_name: str = (
            "screenshot" + datetime.now().strftime("%H:%M:%S") + ".png"
        )
        self.save_screenshot(config.SCREENSHOT_PATH + "/" + screenshot_name)

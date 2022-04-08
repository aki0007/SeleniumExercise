from datetime import datetime

from config import config
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException
from selenium.webdriver.support.ui import Select


class WebDriver(Chrome):
    def set_window(self):
        self.get(config.GLOBAL_URL + config.TESTING_URL)
        self.maximize_window()

    def get_element(self, locator, highlight=True, clickable=True):
        try:
            # Wait until element is clickable
            if clickable:
                WebDriverWait(self, 5).until(
                    EC.element_to_be_clickable((By.XPATH, locator))
                )

            # Wait until element is clickable
            element = WebDriverWait(self, 5).until(
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

    def safe_send_keys(self, input_text: str, locator):
        self.get_element(locator).click()
        action = ActionChains(self)
        action.send_keys(input_text)
        action.perform()

    def select_from_dropdown(self, locator, dropdown_menu):
        select = Select(self.get_element(locator))
        select.select_by_value(dropdown_menu)

    def check_if_element_exists(self, locator):
        try:
            WebDriverWait(self, 5).until(
                EC.presence_of_element_located((By.XPATH, locator))
            )
        except TimeoutException:
            return False
        return True

    def hover_element(self, locator):
        element = self.get_element(locator)
        hov = ActionChains(self).move_to_element(to_element=element)
        hov.perform()

    def wait_for_loader_to_load(self, locator):
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

    def take_screenshot(self):
        screenshot_name: str = (
                "screenshot" + datetime.now().strftime("%H:%M:%S") + ".png"
        )
        self.save_screenshot(config.SCREENSHOT_PATH + "/" + screenshot_name)

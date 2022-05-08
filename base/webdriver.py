from inspect import stack, FrameInfo
from typing import Any

from selenium.common.exceptions import ElementNotInteractableException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select, WebDriverWait

from config import conf_obj, get_webdriver


class WebDriver(get_webdriver()):  # type: ignore
    def set_window(self) -> None:
        """
        Navigate to url and maximize window
        """
        self.get(conf_obj.GLOBAL_URL + conf_obj.TESTING_URL)
        self.maximize_window()

    def get_element(
            self, locator: str, highlight: bool = True, clickable: bool = True
    ) -> WebElement:
        try:
            # Wait until element is clickable
            if clickable:
                WebDriverWait(self, 5).until(
                    ec.element_to_be_clickable((By.XPATH, locator))
                )

            # Wait until element is present
            element: WebElement = WebDriverWait(self, 5).until(
                ec.presence_of_element_located((By.XPATH, locator))
            )

            # Highlight element for better debugging
            if highlight:
                self.execute_script(
                    "arguments[0].setAttribute(" "'style', 'background: yellow;');",
                    element,
                )
            return self.find_element(By.XPATH, locator)
        # Not intractable element exception
        except ElementNotInteractableException:
            return self.find_element(By.XPATH, locator)

    def safe_send_keys(self, locator: str, input_text: str) -> None:
        """
        :param locator:
        :param input_text:
        """
        self.get_element(locator).click()
        action: ActionChains = ActionChains(self)
        action.send_keys(input_text)
        action.perform()

    def select_from_dropdown_by_value(self, locator: str, dropdown_menu: str) -> None:
        # Used for dropdown by value
        select: Select = Select(self.get_element(locator))
        select.select_by_value(dropdown_menu)

    def check_if_element_exists(self, locator: str, time_to_wait: int = 5) -> bool:
        """
        Validate if element exists on page.
        Mostly used in validation
        :param locator:
        :param time_to_wait: time to wait for element to load
        :return: True/False
        """
        try:
            WebDriverWait(self, time_to_wait).until(
                ec.presence_of_element_located((By.XPATH, locator))
            )
        except TimeoutException:
            return False
        return True

    def hover_element(self, locator: str) -> None:
        """
        # Hover over the element
        :param locator:
        """
        element: WebElement = self.get_element(locator)
        hov: ActionChains = ActionChains(self).move_to_element(to_element=element)
        hov.perform()

    def wait_for_loader_to_load(self, locator: str) -> None:
        """
        Wait for loading element to appear
        required to prevent prematurely checking if element
        has disappeared, before it has had a chance to appear
        """
        try:
            WebDriverWait(self, 20).until(
                ec.presence_of_element_located((By.XPATH, locator))
            )
            self.get_element(locator)
            # then wait for the element to disappear
            WebDriverWait(self, 20).until_not(
                ec.presence_of_element_located((By.XPATH, locator))
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
        function_stack = stack()[2]  # Fetch name of function assertion occurs in

        # Print SS with name that match: function_where_assertion_occurs()_assertion_line_in_that_funtion.png
        screenshot_name: str = f"{function_stack[3]}()_line_{function_stack[2]}.png"
        self.save_screenshot(conf_obj.SCREENSHOT_PATH + "/" + screenshot_name)

    def c_assert(self, value1: Any, value2: Any = True) -> None:
        """
        Custom assert that compares two values and if false then:
        - take screenshot on fail
        - print message with file, function and lines assertion occurs
        """
        # If assert condition is not met take screenshot
        function_stack: FrameInfo = stack()[2]
        assert_stack: FrameInfo = stack()[1]  #

        message: str = (
            f"In file '{assert_stack[1]}'\n"
            f"function: '{function_stack[3]}()': line = {function_stack[2]}\n"
            f"Assertion on line {assert_stack[2]}: \n"
            f"Value is :'{value1}' instead of '{value2}'"
        )
        try:
            assert value1 == value2
        except AssertionError:
            self.take_screenshot()
        finally:
            assert value1 == value2, message

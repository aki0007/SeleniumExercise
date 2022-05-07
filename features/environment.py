import os

from base.webdriver import WebDriver
from config import conf_obj


def before_all(context):
    # Create a screenshot path if it does not exist
    if not os.path.exists(conf_obj.SCREENSHOT_PATH):
        os.makedirs(conf_obj.SCREENSHOT_PATH)

    context.driver = WebDriver()


def after_all(context):
    context.driver.quit()

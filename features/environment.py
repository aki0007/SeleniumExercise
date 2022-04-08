import os

from base.webdriver import WebDriver
from config import config


def before_all(context):
    # Create a screenshot path if it does not exist
    if not os.path.exists(config.SCREENSHOT_PATH):
        os.makedirs(config.SCREENSHOT_PATH)

    context.driver = WebDriver()


def after_all(context):
    context.driver.quit()

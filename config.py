import os
from datetime import datetime
from typing import Union

from selenium import webdriver
from selenium.webdriver import Chrome, Edge, Firefox, Opera
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.opera.options import Options as OperaOptions


from dotenv import load_dotenv

load_dotenv()


class Config:
    # App
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    GLOBAL_URL = os.getenv("GLOBAL_URL", "https://")
    TESTING_URL = os.getenv("TESTING_URL", "/testing")
    LOCAL: bool = os.getenv("LOCAL", "0") == "1"
    SCREENSHOT_PATH = os.path.abspath(
        "reports/screenshots/" + datetime.now().strftime("%d-%m-%Y")
    )

    # Credentials
    LOGIN_USERNAME = os.getenv("LOGIN_USERNAME", "user")
    LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD", "1234")


class ProductionConfig(Config):
    ENVIRONMENT: str = "production"


class StagingConfig(Config):
    ENVIRONMENT: str = "staging"


def get_config() -> Union[Config, ProductionConfig, StagingConfig]:
    env_list: dict = {
        "development": Config,
        "docker": Config,
        "production": ProductionConfig,
        "staging": StagingConfig,
    }
    env: str = os.getenv("ENVIRONMENT", "development")

    if env not in env_list:
        raise Exception("Invalid environment")

    return env_list[env]()


def get_driver_options() -> Union[
    ChromeOptions, FirefoxOptions, OperaOptions, EdgeOptions, None
]:
    # TODO if docker then this else return None
    options_list: dict = {
        "chrome": ChromeOptions(),
        "edge": EdgeOptions(),
        "firefox": FirefoxOptions(),
        "opera": OperaOptions(),
    }

    options: str = os.getenv("BROWSER", "chrome")
    if options not in options_list:
        raise Exception("Invalid browser")

    return options_list[options]


def get_webdriver() -> Union[Chrome, Firefox, Opera, Edge]:
    browser_list: dict = {
        "chrome": Chrome,
        "edge": Edge,
        "firefox": Firefox,
        "opera": Opera,
    }
    browser: str = os.getenv("BROWSER", "chrome")

    if browser not in browser_list:
        raise Exception("Invalid browser")

    if browser == "opera":
        webdriver_service = service.Service("/home/aki/drivers/operadriver")
        webdriver_service.start()
        return webdriver.Remote(webdriver_service.service_url)

    return browser_list[browser]


conf_obj: Union[Config, ProductionConfig, StagingConfig] = get_config()

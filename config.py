import os
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()


class Config:
    # app
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    GLOBAL_URL = os.getenv("GLOBAL_URL", "https://")
    TESTING_URL = os.getenv("TESTING_URL", "/testing")
    LOGIN_USERNAME = os.getenv("LOGIN_USERNAME", "user")
    LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD", "1234")
    SCREENSHOT_PATH = os.path.abspath("reports/screenshots/" + datetime.now().strftime("%d-%m-%Y"))


config = Config()

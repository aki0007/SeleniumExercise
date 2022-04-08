from collections.abc import MutableSequence
from datetime import datetime
from typing import Sequence, Union

from base.locators import Locators
from base.webdriver import WebDriver

MySequenceType = Union[MutableSequence, tuple, set]


def select_date(driver: WebDriver, date: Sequence[str]) -> None:
    # Open calendar
    driver.get_element(Locators.REGISTRATION_DOB).click()
    date_obj: datetime = datetime.strptime(str(date), "%d %B, %Y")

    # Fetch how many times left calendar arrow needs to be clicked
    number_of_clicks: int = parse_from_date(date_obj)
    # Select correct month and year
    select_year_and_month_on_calendar(driver, number_of_clicks)
    driver.get_element(Locators.CALENDAR_SELECT_DATE.format(date=date_obj.day)).click()


def parse_from_date(date_obi: datetime) -> int:
    today: datetime = datetime.now()
    number_of_clicks: int = (today.year - date_obi.year) * 12 + (
        today.month - date_obi.month
    )
    return number_of_clicks


def select_year_and_month_on_calendar(driver: WebDriver, number_of_clicks: int) -> None:
    for _ in range(number_of_clicks):
        driver.get_element(Locators.CALENDAR_LEFT_ARROW).click()

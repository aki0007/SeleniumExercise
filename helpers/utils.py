from library.locators import Locators
from datetime import datetime


def select_date(driver, date):
    # Open calendar
    driver.get_element(Locators.REGISTRATION_DOB).click()
    datetime_obj = datetime.strptime(date, '%m-%d-%Y')

    # Fetch how many times left calendar arrow needs to be clicked
    number_of_clicks = parse_from_date(datetime_obj)
    # Select correct month and year
    select_year_and_month_on_calendar(driver, number_of_clicks)
    driver.get_element(Locators.CALENDAR_SELECT_DATE.format(date=datetime_obj.day)).click()


def parse_from_date(date_obi):
    today = datetime.now()
    number_of_clicks = (today.year - date_obi.year) * 12 + (today.month - date_obi.month)
    return number_of_clicks


def select_year_and_month_on_calendar(driver, number_of_clicks):
    for _ in range(number_of_clicks):
        driver.get_element(Locators.CALENDAR_LEFT_ARROW).click()

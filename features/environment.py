from library.webdriver import WebDriver


def before_all(context):
    context.driver = WebDriver()


def after_all(context):
    context.driver.quit()


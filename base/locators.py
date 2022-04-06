class Locators:
    GET_NEW_USER_BUTTON = "//button[text()='Get New User']"

    CALENDAR_LEFT_ARROW = "//a[@data-handler='prev']"
    CALENDAR_SELECT_DATE = "//td[@data-handler='selectDay']//a[text()='{date}']"

    DROPDOWN_OPTION = "//option[text()='{text}']"

    LOGIN_TAB = "//li[descendant::input[@id='tab2']]"
    LOGIN_USERNAME = "//input[@placeholder='Username']"
    LOGIN_PASSWORD = "//input[@placeholder='mypassword']"
    LOGIN_KEEP_ME_LOGGED_IN = "//em[text()='Keep me logged in ']/preceding-sibling::input"
    LOGIN_BUTTON = "//input[@value='Login']"

    GENERAL_BUTTON = "//button[text()='{text}']"
    LOADING_LOADER = "//div[@id='loading']"
    PROGRESS_LOADER = "//div[contains(text(), 'Current Progress')]"
    PROGRESS_COMPLETE = "//div[text()='Complete!']"

    REGISTRATION_USERNAME = "//input[@placeholder='myusername']"
    REGISTRATION_EMAIL = "//input[@name='fld_email']"
    REGISTRATION_PASSWORD = "//input[@placeholder='Password']"
    REGISTRATION_CONFIRM_PASSWORD = "//input[@placeholder='Confirm password']"
    REGISTRATION_DOB = "//input[@placeholder='Date of birth']"
    REGISTRATION_PHONE = "//input[@placeholder='Phone']"
    REGISTRATION_ADDRESS = "//input[@placeholder='Address']"
    REGISTRATION_ADDRESS_TYPE = "//input[@name='add_type' and @value='{address_type}']"
    REGISTRATION_GENDER = "//select[@name='sex']"
    REGISTRATION_COUNTRY = "//select[@name='country']"
    REGISTRATION_STATE = "//select[@name='state']"
    REGISTRATION_CITY = "//select[@name='city']"
    REGISTRATION_ZIP_CODE = "//input[@name='zip']"
    REGISTRATION_TERMS_AND_CONDITIONS = "//em[text()='I agree with terms and conditions ']/preceding-sibling::input"

    SIGN_UP_BUTTON = "//input[@value='Sign up']"

    NAVIGATION_TAB = "//li[descendant::a[contains(text(), '{tab}')]]"
    SUB_NAVIGATION_TAB = "//ul[@class='dropdown-menu']//li[descendant::a[contains(text(), '{tab}')]]"

    VALIDATE_SUCCESSFUL_LOGIN = "//*[text() = ' Welcome Mr. {username}']"
    VALIDATE_GENERATED_USER = "//div[contains(text(), 'First Name')]"

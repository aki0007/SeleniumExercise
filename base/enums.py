from enum import Enum


class NavigationTab(Enum):
    HOME = "Home"
    MY_ACCOUNT = " My Account"
    HOVER = "Hover"
    DOWNLOAD = "Download"
    LOGOUT = "logout"


class HomeTab(Enum):
    GENERATE_USER = "Generate User"
    SEND_FEEDBACK = "Send Feedback"
    DATA_VALIDATE = "Data validate"
    USER_LIST = "User List"
    AUTOMATION_MODEL = "Automation model"
    BOOTSTRAP_PROGRESS_BAR = "Bootstrap Progress bar"

Project SeleniumExercise consists of some practices to test GUI and API testing.
This is not supposed to be to detailed and coplicated project, but only to show some basic concepts and ideas.
Web page that is tested is: "https://thetestingworld.com/testings/"

Files:
api_testing: consits of testing login with requests library
config: Consists of project configuration files. File config_reader.py has methods that help operate with config files
drivers: chromedriver, TODO geckodriver
features: Consists of everything that needs to be set up to work with behave (BDD testing)
helpers: Reusable python methods. Can be used by pytest, behave...
library: Consits values that are not supposed to be changed such as: data, enums, locators, webdriver.
        webdriver.py has class Driver() that inharitance webdriver.Chrome (TODO gecko), but has more methodes that are
        usefull to work with selenium such as take_screenshot(), wait_for_loader_to_load(), get_element()...
pytest_tests: Consists of tests run with pytest. Pytest fixtures and markers are used as well
validation: simillar to helper files, but those methods are used to validate GUI action.

Project also use pre-commit hook that checks black, safety and flake8

To install dependencies run:
$ pip install -r requirements.txt

To start tests run:
$  pytest  # Markers that are defined in pytest.ini: login, register, generate_user, backend
$  pytest --alluredir=<allure-report>  # run pytest and create allure reports
$  behave # Run tests with behave
$  behave -f allure_behave.formatter:AllureFormatter -o <allure-report>  ./features  # Run behave with allure reports

To generate allure reports run:
$  allure serve allure-report


# Selenium Exercise

## Setup

Copy `.env.example` to `.env` and fill in the variables.

Install `pre-commit`:

    pip install pre-commit
    pre-commit install --install-hooks

## Usage

Install dependencies

    pip-compile -r requirements.in
    pip-install -r requirements.txt

Run behave tests examples:

    behave features # Run all behave tests
    behave features/login.feature  # Run login.feature tests
    behave features/login.feature  # Run login.feature tests

Run test and generate allure report

    behave -f allure_behave.formatter:AllureFormatter -o reports/allure-reports ./tests/features  
    allure serve allure/results

Run api test:
    
    pytest tests/api

Run pytest tests:

    pytest tests/pytest

### Code formatting

Project use [black](https://github.com/ambv/black/) to format the python files.

Install and run `black`, `isort`, `mypy`:

    pip install black
    black .
    pip install isort
    isort .
    pip install mypy
    mypy .

from setuptools import setup

setup(
    name="Selenium Exercise",
    version="1.0",
    description="A useful module",
    author="Jaksa Milanovic",
    author_email="jaksa.milanovic007@gmail.com",
    packages=["foo"],  # same as name
    install_requires=[
        "allure-behave",
        "allure-pytest",
        "allure-python-commons",
        "behave",
        "pytest",
        "selenium",
        "requests",
        "pre-commit",
    ],  # external packages as dependencies
)

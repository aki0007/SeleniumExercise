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
        "allure-gui",
        "allure-python-commons",
        "behave",
        "gui",
        "selenium",
        "requests",
        "pre-commit",
    ],  # external packages as dependencies
)

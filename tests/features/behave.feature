#noinspection CucumberUndefinedStep

Feature: Run tests with behave
  @login @regression
  Scenario: Login to the testing world page
    Given Navigate to testing page
    When Login to page with username "None" and password "None"
    Then Validate successful login

  Scenario: Generate test user
    Given Navigate to testing page
    When Login to page with username "Aki" and password "golubica123"
    Then Validate successful login
    When Create random user
    Then Validate if random user is generated successfully

  Scenario: Manage customer
    Given Navigate to testing page
    When Login to page with username "None" and password "None"
    Then Validate successful login
    When Navigate to "My Account", "Manage Customer" in navigation tab
    And Click on "Start Download" button
    Then Wait for progress loader to load
    And Validate successful download
    When Click on "Close" button

# Selenium-with-python

Sample automated testing project following Andrew Knight's Test Automation University course using Python and Selenium WebDriver. 

Tests will be written for the search engine DuckDuckGo (https://www.duckduckgo.com)in a Page Object Model and use pytest as the test runner, allowing for fixtures and dependency injection of the browser instance. 


## Requirements
- Requires Python 3.8 or higher.
- Pipenv
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) for Chrome
- [geckodriver](https://github.com/mozilla/geckodriver/releases) for Firefox


## Project Setup

1. Clone this repository.
2. Run `cd Selenium-with-python` to enter the project.
3. Run `pipenv install` to install the dependencies.
4. Run `pipenv run python -m pytest` to run tests.


'''
This module contains the page object 
for the DuckDuckGo Search Page
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoSearchPage:

    # URL
    URL = 'https://www.duckduckgo.com'

    # Locators
    SEARCH_INPUT = (By.ID, 'searchbox_input')

    # Initialiser
    def __init__(self, browser):
        self.browser = browser

    # Methods
    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
'''
This module contains the page object 
for the DuckDuckGo Results Page
'''

from selenium.webdriver.common.by import By

class DuckDuckGoResultsPage:

    # Locators
    RESULTS_LINKS = (By.XPATH, '//a[not(contains(@href, \'duckduckgo\')) and @data-testid="result-title-a"]')
    SEARCH_INPUT = (By.ID, 'search_form_input')

    # Initialiser
    def __init__(self, browser):
        self.browser = browser


    def results_link_titles(self):
        results_links = self.browser.find_elements(*self.RESULTS_LINKS)
        results_links_titles = [r.text for r in results_links]
        return results_links_titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')
    
    def title(self):
        return self.browser.title
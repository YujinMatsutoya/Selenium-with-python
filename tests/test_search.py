'''
Tests for DuckDuckGo searches
'''
from pages.search_page import DuckDuckGoSearchPage
from pages.results_page import DuckDuckGoResultsPage
import pytest

@pytest.mark.parametrize('query', ['panda', 'brunch', 'poodle'])
def test_basic_duckduckgo_search(browser, query):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultsPage(browser)
    #query = "panda"

    # Given the DuckDuckGo homepage is displayed
    search_page.load()

    # When the user searches 'panda'
    search_page.search(query)

    # Then the search result title contains 'panda'
    assert query in result_page.title()

    # Then the search query is 'panda'
    assert result_page.search_input_value() == query

    # Then the search result links pertain to 'panda'
    for title in result_page.results_link_titles():
        assert  query.lower() in title.lower()

    #raise Exception("Incomplete Test")

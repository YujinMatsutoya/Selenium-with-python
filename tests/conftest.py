'''
This module contains shared fixtures
'''

import pytest 
import selenium.webdriver

@pytest.fixture
def browser():
    # initialise a ChromeDriver Instance
    b = selenium.webdriver.Chrome()

    # wait for elements to appear up to 10 secs
    b.implicitly_wait(10)
    print('dsfkjhgasksdalkfhas;dhfa;s')

    # return WebDriver instance for the setup
    yield b

    # quit WebDriver Instance for cleanup
    b.quit()
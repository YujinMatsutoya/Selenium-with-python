'''
This module contains shared fixtures
'''

import pytest 
import selenium.webdriver
import json

@pytest.fixture
def config(scope='session'):
    with open('config.json') as config_file:
        config = json.load(config_file)
    
    print('\n\n\n\n\n', config['browser'], '\n\n\n\n' )
    assert config['browser'] in ['Chrome', 'Firefox', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)

    return config



@pytest.fixture
def browser(config):
    
    # initialise a ChromeDriver Instance
    if config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()    
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)    

    # wait for elements to appear up to 10 secs
    b.implicitly_wait(config['implicit_wait'])
    print('\n\n\n\n\ndsfkjhgasksdalkfhas;dhfa;s\n\n\n\n')

    # return WebDriver instance for the setup
    yield b

    # quit WebDriver Instance for cleanup
    b.quit()
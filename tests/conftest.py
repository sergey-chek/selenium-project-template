"""
Shared fixtures for project.
"""
import pytest
import selenium.webdriver
import json


@pytest.fixture
def config(scope='session'):
    """This fixture reads and returns configuration file like a dictionary"""

    with open('config.json') as f:
        config = json.load(f)

    return config


@pytest.fixture
def driver(config):
    """Initializing the WebDriver instance and tearing it down after use."""

    # Initialize a WebDriver instance for different browsers
    try:
        if config['browser'] == 'Chrome':
            driver = selenium.webdriver.Chrome()
        elif config['browser'] == 'Headless Chrome':
            browser_options = selenium.webdriver.ChromeOptions()
            browser_options.headless = True
            browser_options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = selenium.webdriver.Chrome(options=browser_options)
        else:
            raise Exception(f'The browser "{config["browser"]}" is not supported')
    except KeyError:
        raise Exception('There is no "browser" parameter in the config file')

    # Define implicit wait time
    try:
        if isinstance(config['implicit_wait'], int) and (config['implicit_wait'] > 0):
            driver.implicitly_wait(config['implicit_wait'])
        else:
            raise Exception('The "implicit_wait" parameter is incorrect')
    except KeyError:
        pass  # Continue without implicit wait time

    # Return WebDriver instance
    yield driver

    # Quit the WebDriver instance
    driver.quit()

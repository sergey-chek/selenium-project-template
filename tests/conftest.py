"""Shared fixtures for project."""

import json
import os.path
import pytest
import selenium.webdriver


def pytest_addoption(parser):
    """Add parameters to a command line"""
    parser.addoption('--screen', action='store', default='n', help='Do you want to save screenshots? y/n')


@pytest.fixture
def config(scope='session'):
    """This fixture reads and returns configuration file like a dictionary"""
    with open('config.json') as f:
        config = json.load(f)
    return config


@pytest.fixture
def driver(config, request):
    """Initializing the WebDriver instance and tearing it down after use."""

    # Initialize a WebDriver instance for different browsers --------------------------------------------------------
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

    # Define implicit wait time -------------------------------------------------------------------------------------
    try:
        if isinstance(config['implicit_wait'], int) and (config['implicit_wait'] > 0):
            driver.implicitly_wait(config['implicit_wait'])
        else:
            raise Exception('The "implicit_wait" parameter is incorrect')
    except KeyError:
        pass  # Continue without implicit wait time

    # Define the path for screenshots -------------------------------------------------------------------------------
    command_opt_screenshots = request.config.getoption('--screen').lower().strip()
    if command_opt_screenshots == 'n':
        driver.is_screenshot_activated = False
    elif command_opt_screenshots == 'y':
        driver.is_screenshot_activated = True
        if os.path.isdir(config['screenshots_folder_path']):
            driver.screenshots_folder_path = config['screenshots_folder_path']
        else:
            raise Exception('Invalid path in the config file (screenshots_folder_path).')
    else:
        raise Exception('Invalid value for the parameter --screen (y/n).')

    # Return WebDriver instance -------------------------------------------------------------------------------------
    yield driver

    # Quit the WebDriver instance -----------------------------------------------------------------------------------
    driver.quit()

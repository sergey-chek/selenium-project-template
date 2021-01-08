"""
Shared fixtures for project.
"""


import pytest
import selenium.webdriver


@pytest.fixture
def driver():
    """Initializing the WebDriver instance and tearing it down after use."""

    # Initialize a WebDriver instance
    driver = selenium.webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver

    # Quit the WebDriver instance
    driver.quit()

"""
This module contains GoogleSearchPage class,
the page object for an initial www.google.com search page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GoogleSearchPage:
    """The page object for an initial www.google.com search page"""

    URL = 'https://www.google.com/'
    SEARCH_FIELD_LOCATOR = (By.CSS_SELECTOR, 'input.gsfi')

    def __init__(self, driver):
        self.driver = driver

    def load_page(self) -> None:
        self.driver.get(self.URL)

    def search_phrase(self, phrase: str) -> None:
        search_field = self.driver.find_element(*self.SEARCH_FIELD_LOCATOR)
        search_field.clear()
        search_field.send_keys(phrase + Keys.ENTER)

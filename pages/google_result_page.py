"""
This module contains GoogleResultPage class,
the page object for a search result page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GoogleResultPage:
    """The page object for a Google search result page"""

    SEARCH_FIELD_LOCATOR = (By.CSS_SELECTOR, 'input.gsfi')
    RESULT_LINKS_LOCATOR = (By.TAG_NAME, 'h3')

    def __init__(self, driver) -> None:
        self.driver = driver

    def get_page_title(self) -> str:
        return self.driver.title

    def get_search_field_text(self) -> str:
        search_field = self.driver.find_element(*self.SEARCH_FIELD_LOCATOR)
        return search_field.get_attribute('value')

    def get_result_link_titles(self) -> list[str, ...]:
        links = self.driver.find_elements(*self.RESULT_LINKS_LOCATOR)
        link_titles = [link.text for link in links]
        return link_titles

    def search_phrase(self, phrase: str) -> None:
        search_field = self.driver.find_element(*self.SEARCH_FIELD_LOCATOR)
        search_field.clear()
        search_field.send_keys(phrase + Keys.ENTER)

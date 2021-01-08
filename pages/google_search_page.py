"""
This module contains GoogleSearchPage class,
the page object for an initial www.google.com search page
"""


class GoogleSearchPage:
    """The page object for an initial www.google.com search page"""

    def __init__(self, driver):
        self.driver = driver

    def load_page(self) -> None:
        # TODO
        pass

    def search_phrase(self, phrase: str) -> None:
        # TODO
        pass

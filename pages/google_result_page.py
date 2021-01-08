"""
This module contains GoogleResultPage class,
the page object for a search result page
"""


class GoogleResultPage:
    """The page object for a search result page"""

    def __init__(self, driver) -> None:
        self.driver = driver

    def get_page_title(self) -> str:
        # TODO
        return ''

    def get_search_query_text(self) -> str:
        # TODO
        return ''

    def get_result_link_titles(self) -> list[str, ...]:
        # TODO
        return ['', '']

    def search_phrase(self, phrase: str) -> None:
        # TODO
        pass

"""
These tests cover searching on Google (for example...)
Any additional information about functionality...
"""

import pytest
from pages.google_search_page import GoogleSearchPage
from pages.google_result_page import GoogleResultPage

@pytest.mark.parametrize('phrase', ['python', 'java', 'ruby', 'javascript', 'abap'])
def test_basic_search(driver, phrase):
    """
    Given the Google page is displayed
    When the user searches for "python"
        Then the search result title contains "python"
            And the search result query is "python"
            And the search result links in lower case contain "python"
    """

    search_page = GoogleSearchPage(driver)
    result_page = GoogleResultPage(driver)

    # Given the Google page is displayed
    # When the user searches for "python"
    search_page.load_page()
    search_page.search_phrase(phrase)

    # Then the search result title contains "python"
    assert phrase in result_page.get_page_title()

    # And the search result query is "python"
    assert phrase == result_page.get_search_field_text()

    # And the search result links in lower case contain "python"
    counter = 0
    for title in result_page.get_result_link_titles():
        if phrase.lower() in title.lower():
            counter += 1
    assert counter > 0


def test_search_on_result_page(driver):
    """
    Given the Google page is displayed
    Given the user searches for "python" and presses Enter
    Given the search result page is displayed
    When the user searches for "java" on the search result page
        Then the search result title contains "java"
            And the search result query is "java"
            And the search result links in lower case contain "java"
    """

    search_page = GoogleSearchPage(driver)
    result_page = GoogleResultPage(driver)
    phrase_python = "python"
    phrase_java = "java"

    # Given the Google page is displayed
    # Given the user searches for "python" and presses Enter
    # Given the search result page is displayed
    search_page.load_page()
    search_page.search_phrase(phrase_python)

    # When the user searches for "java" on the result page
    result_page.search_phrase(phrase_java)

    # Then the search result title contains "java"
    assert phrase_java in result_page.get_page_title()

    # And the search result query is "java"
    assert phrase_java == result_page.get_search_field_text()

    # And the search result links in lower case contain "java"
    counter = 0
    for title in result_page.get_result_link_titles():
        if phrase_java.lower() in title.lower():
            counter += 1
    assert counter > 0

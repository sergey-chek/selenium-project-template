"""
These tests cover searching on Google.
Any additional information about functionality...
"""

import pytest
import inspect
from pages.google_search_page import GoogleSearchPage
from pages.google_result_page import GoogleResultPage
from utils.screenshot import Screenshot


@pytest.mark.parametrize('phrase', ['python', 'java', 'ruby', 'javascript', 'abap'])
def test_basic_search(driver, phrase):
    """
    Given the Google page is displayed

    When the user searches for a "phrase"

    Then the search result title contains "phrase"
    And the search result query is "phrase"
    And the search result links in lower case contain "phrase"
    """

    search_page = GoogleSearchPage(driver)
    result_page = GoogleResultPage(driver)

    # Given the Google page is displayed
    # When the user searches for "phrase"
    search_page.load_page()
    search_page.search_phrase(phrase)

    # Then the search result title contains "phrase"
    assert phrase in result_page.get_page_title()

    # And the search result query is "python"
    assert phrase == result_page.get_search_field_text()

    # And the search result links in lower case contain "phrase"
    counter = 0
    for title in result_page.get_result_link_titles():
        if phrase.lower() in title.lower():
            counter += 1
    assert counter > 0

    test_name_for_screenshot = inspect.stack()[0].function
    Screenshot(driver, f'{test_name_for_screenshot}-{phrase}').save()


def test_search_on_result_page(driver):
    """
    Given the Google page is displayed
    And the user searches for "python"
    And the search result page is displayed

    When the user searches for "java"

    Then the search result title contains "java"
    And the search result query is "java"
    And the search result links in lower case contain "java"
    """

    search_page = GoogleSearchPage(driver)
    result_page = GoogleResultPage(driver)
    phrase_python = "python"
    phrase_java = "java"

    # Given the Google page is displayed
    # Given the user searches for "python"
    # Given the search result page is displayed
    search_page.load_page()
    search_page.search_phrase(phrase_python)

    test_name_for_screenshot = inspect.stack()[0].function
    Screenshot(driver, test_name_for_screenshot).save()

    # When the user searches for "java"
    result_page.search_phrase(phrase_java)

    Screenshot(driver, test_name_for_screenshot).save()

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

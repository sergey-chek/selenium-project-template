"""
Common utils for tests in project
"""
import datetime


def generate_screenshot_file_name(test_name: str, file_extension: str) -> str:
    """
    This function generates file name for a screenshot.
    Format: "YYYY-MM-DD-HH-MM-SS-MMMMMM-test_name.file_extention".
    For example, "2021-01-15-09-32-12-123654-test_basic_search.png".
    """
    t = datetime.datetime.now()
    return f"{t.year}-{t.month}-{t.day}-{t.hour}-{t.second}-{t.minute}-{t.microsecond}-{test_name}.{file_extension}"


def generate_screenshot_folder_name(test_name: str, file_extension: str) -> dict[str, str]:
    """
    This function generates folder name for a screenshot.
    Format: "YYYY-MM-DD".
    For example, "2021-01-15".
    """
    t = datetime.datetime.now()
    return f"{t.year}-{t.month}-{t.day}"

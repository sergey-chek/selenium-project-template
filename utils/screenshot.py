import os
from datetime import datetime


class Screenshot:
    def __init__(self, driver, name: str):
        """Сlass for creating and saving screenshots
            Parameters:
                driver      - selenium WebDriver instance
                name: str   - text for a file name
            Returns:
                None
        """
        self.driver = driver

        # Functionality works only if there is a flag in the command line ("--screen=yes")
        if self.driver.is_screenshot_activated:
            dt = datetime.now()
            self.file_name = f"{name}-{dt.hour:02d}-{dt.minute:02d}-{dt.second:02d}-{dt.microsecond:06d}.png"
            self.subfolder_name = f"{dt.year:04d}-{dt.month:02d}-{dt.day:02d}"
            self.screenshots_folder_path = driver.screenshots_folder_path

    def _create_subfolder(self):
        """Create a subfolder with name 'YYYY-MM-DD' inside the main folder for screenshots."""
        if self.driver.is_screenshot_activated:
            try:
                subfolder_path = os.path.join(self.screenshots_folder_path, self.subfolder_name)
                os.mkdir(subfolder_path)
            except FileExistsError:
                pass  # The folder has already created. Nothing to do

    def save(self):
        """Save screenshot in a subfolder."""
        if self.driver.is_screenshot_activated:
            self._create_subfolder()
            file_path = os.path.join(self.screenshots_folder_path, self.subfolder_name, self.file_name)
            self.driver.save_screenshots(file_path)

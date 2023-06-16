import pytest

from data.test_data import TestData
from pages.check_box_page import CheckBoxPage
from utils.tools import take_screenshot


class TestCheckBoxes:

    @pytest.fixture
    def test_setup(self, new_session):
        self.driver = new_session
        self.checkboxes = CheckBoxPage(self.driver)

        # click elements button on the homepage
        self.checkboxes.click_elements_button()

        # click checkboxes section from the sidebar
        self.checkboxes.go_to_check_box_section()

    @pytest.mark.regression
    def test_checkboxes(self, test_setup):
        """Test to verify the checkboxes on the page

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.checkboxes.expand_home_directory()

        self.checkboxes.expand_desktop_directory()

        self.checkboxes.expand_documents_directory()

        self.checkboxes.expand_downloads_directory()

        for item in TestData.checkboxes:
            self.checkboxes.select_checkbox(item)

        results = self.checkboxes.get_checkbox_text()

        for item in TestData.checkboxes:
            assert item.lower() in results, f'Expected {item} to be in {results}'

        take_screenshot(self.driver, "checkboxes_result")

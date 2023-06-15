import time

import pytest

from data.test_data import TestData
from pages.web_table_page import WebTablePage
from utils.tools import take_screenshot


class TestWebTables:

    @pytest.fixture
    def test_setup(self, new_session):
        self.driver = new_session
        self.table = WebTablePage(self.driver)

        # click elements button on the homepage
        self.table.click_elements_button()

        # click checkboxes section from the sidebar
        self.table.go_to_web_tables_section()

    @pytest.mark.one
    def test_web_tables(self, test_setup):
        """Test to verify interaction with web table on the page

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        self.table.add_new_user(
            first_name=TestData.user["first_name"],
            last_name=TestData.user["last_name"],
            email=TestData.user["email"],
            age=TestData.user["age"],
            salary=TestData.user["salary"],
            department=TestData.user["department"],
        )

        index, text = self.table.get_row_number()
        for value in TestData.user.values():
            assert value in text


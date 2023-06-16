import pytest

from pages.text_box_page import TextBoxPage
from data.test_data import TestData
from utils.tools import take_screenshot


class TestTextBoxes:

    @pytest.fixture
    def test_setup(self, new_session):
        self.driver = new_session
        self.text_box = TextBoxPage(self.driver)

        # click elements button on the homepage
        self.text_box.click_elements_button()

        # click test boxes section from the sidebar
        self.text_box.go_to_text_box_section()

    @pytest.mark.regression
    def test_text_boxes(self, test_setup):
        """Test to verify the input fields and output form on the page

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.text_box.set_username(TestData.username)
        self.text_box.set_email(TestData.email)
        self.text_box.set_current_address(TestData.current_address)
        self.text_box.set_permanent_address(TestData.permanent_address)
        take_screenshot(self.driver, "submitted_form")

        self.text_box.submit_form()

        take_screenshot(self.driver, "resulting_form")

        # check the result
        actual_username = self.text_box.get_username()
        actual_email = self.text_box.get_user_email()
        actual_current_address = self.text_box.get_current_address()
        actual_permanent_address = self.text_box.get_permanent_address()

        assert actual_username == f'Name:{TestData.username}'
        assert actual_email == f'Email:{TestData.email}'
        assert actual_current_address == f'Current Address :{TestData.current_address}'
        assert actual_permanent_address == f'Permananet Address :{TestData.permanent_address}'

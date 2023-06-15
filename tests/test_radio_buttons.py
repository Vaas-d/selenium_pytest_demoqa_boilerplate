import time

import pytest

from pages.radio_button_page import RadioButtonsPage
from utils.tools import take_screenshot


class TestRadioButtons:

    @pytest.fixture
    def test_setup(self, new_session):
        self.driver = new_session
        self.radio = RadioButtonsPage(self.driver)

        # click elements button on the homepage
        self.radio.click_elements_button()

        # click radio buttons section from the sidebar
        self.radio.go_to_radio_button_section()

        time.sleep(3)

    @pytest.mark.one
    def test_radio_buttons(self, test_setup):
        """Test to verify the radio buttons on the page

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.radio.select_radio_button('Yes')
        actual_message = self.radio.get_result_message()
        assert actual_message == 'Yes'

        self.radio.select_radio_button('Impressive')
        actual_message = self.radio.get_result_message()
        assert actual_message == 'Impressive'

        take_screenshot(self.driver, "radio_buttons_result")
        